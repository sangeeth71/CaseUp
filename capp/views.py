from django.shortcuts import render,redirect
from capp.models import CategoryDb,CaseDb
from webapp.models import MessageDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def dashboard(request):
    return render(request,"index.html")
def add_category(request):
    return render(request,"add_category.html")
def save_category(request):
    if request.method=="POST":
        mt=request.POST.get('material')
        desc=request.POST.get('description')
        img=request.FILES['mat_image']
        obj=CategoryDb(Material_Name=mt,Description=desc,Image=img)
        obj.save()
        return redirect(add_category)
def display_category(request):
    data=CategoryDb.objects.all()
    return render(request,"display_category.html",{'data':data})
def edit_category(request,cat_id):
    cat=CategoryDb.objects.get(id=cat_id)
    return render(request,"edit_category.html",{'cat':cat})
def save_cat_edit(request,cat_id):
    if request.method=="POST":
        mt = request.POST.get('material')
        desc = request.POST.get('description')
        try:
            g=request.FILES['mat_image']
            xy=FileSystemStorage()
            file=xy.save(g.name,g)
        except MultiValueDictKeyError:
            file=CategoryDb.objects.get(id=cat_id).Image
        CategoryDb.objects.filter(id=cat_id).update(Material_Name=mt,Description=desc,Image=file)

    return redirect(display_category)
def delete_category(request,cat_id):
    obj=CategoryDb.objects.filter(id=cat_id)
    obj.delete()
    return redirect(display_category)


# ==========================================================================================================================
def add_case(request):
    cate=CategoryDb.objects.all()
    return render(request,"add_case.html",{'cate':cate})
def save_case(request):
    if request.method=="POST":
        cover=request.POST.get('c_name')
        phone=request.POST.get('c_model')
        price=request.POST.get('c_price')
        material=request.POST.get('material')
        desc=request.POST.get('description')
        img=request.FILES['c_image']
        qua=request.POST.get('quantity')
        obj=CaseDb(Cover_Name=cover,Phone_Model=phone,Price=price,Material=material,Description=desc,Cover_Image=img,Quantity=qua)
        obj.save()
        return redirect(add_case)
def display_cases(request):
    data=CaseDb.objects.all()
    return render(request,"display_cases.html",{'data':data})
def edit_cases(request,case_id):
    case=CaseDb.objects.get(id=case_id)
    category=CategoryDb.objects.all()
    return render(request,"edit_cases.html",{'case':case,'category':category})
def save_case_edit(request,case_id):
    if request.method=="POST":
        cover = request.POST.get('c_name')
        phone = request.POST.get('c_model')
        price = request.POST.get('c_price')
        material = request.POST.get('material')
        desc = request.POST.get('description')
        qua = request.POST.get('quantity')
        try:
            g=request.FILES['c_image']
            xy=FileSystemStorage()
            file=xy.save(g.name,g)
        except MultiValueDictKeyError:
            file=CaseDb.objects.get(id=case_id).Cover_Image
        CaseDb.objects.filter(id=case_id).update(Cover_Name=cover,Phone_Model=phone,Price=price,Material=material,Description=desc,Cover_Image=file,Quantity=qua)
        return redirect(display_cases)
def delete_cases(request,case_id):
    obj=CaseDb.objects.filter(id=case_id)
    obj.delete()
    return redirect(display_cases)

def admin_login(request):
    return render(request,"admin_login.html")

def login_fn(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pswd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            data=authenticate(username=un,password=pswd)
            if data is not None:
                login(request, data)
                request.session['username']=un
                request.session['password']=pswd
                return redirect(dashboard)
            else:
                return redirect(admin_login)
        else :
            return redirect(admin_login)
def logout_fn(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)
def display_messages(request):
    data=MessageDb.objects.all()
    return render(request,"display_messages.html",{'data':data})
def del_message(request,m_id):
    obj=MessageDb.objects.filter(id=m_id)
    obj.delete()
    return redirect(display_messages)