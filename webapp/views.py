from django.shortcuts import render,redirect
from capp.models import CategoryDb,CaseDb
from webapp.models import RegistrationDb
from webapp.models import MessageDb


# Create your views here.
def home_page(request):
    categories=CategoryDb.objects.all()
    return render(request,"home.html",{'categories':categories})
def all_products(request):
    categories = CategoryDb.objects.all()
    cases=CaseDb.objects.all()
    return render(request,"products.html",{'cases':cases,'categories':categories})
def all_materials(request):
    categories=CategoryDb.objects.all()
    return render(request,"materials.html",{'categories':categories})
def about_us(request):
    categories = CategoryDb.objects.all()
    return render(request,"about_us.html",{'categories':categories})
def contact_page(request):
    categories = CategoryDb.objects.all()
    return render(request,"contact.html",{'categories':categories})
def cart_page(request):
    return render(request,"cart_page.html")
def filtered_page(request,model):
    cover=CaseDb.objects.filter(Phone_Model=model )
    return render(request,"filtered.html",{'cover':cover})
def material_filter_page(request,mate):
    categories = CategoryDb.objects.all()
    material=CaseDb.objects.filter(Material=mate)
    return render(request, "mate_filtered.html",{'material': material,'categories':categories})
def single_case(request,case_name):
    categories = CategoryDb.objects.all()
    single=CaseDb.objects.get(Cover_Name=case_name)
    return render(request,"single_case.html",{'single':single,'categories':categories})

def sign_up(request):
    return render(request,"sign_up.html")

def add_user(request):
    if request.method=="POST":
        name=request.POST.get('full_name')
        mail=request.POST.get('email')
        pswd=request.POST.get('password')
        c_pswd=request.POST.get('confirm')
        if RegistrationDb.objects.filter(User_Name=name).exists():
            return redirect(sign_up)
        elif RegistrationDb.objects.filter(Email=mail).exists():
            return redirect(sign_up)
        else:
            obj=RegistrationDb(User_Name=name,Email=mail,Password=pswd,Confirm_Password=c_pswd)
            obj.save()
            return redirect(log_in)
def log_in(request):
    return render(request,"sign_in.html")
def user_login_fn(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pswd=request.POST.get('password')
        if RegistrationDb.objects.filter(User_Name=un,Password=pswd).exists():
            request.session['username'] = un
            request.session['password'] = pswd
            return redirect(home_page)
        else:
            return redirect(log_in)
    return redirect(log_in)
def log_out(request):
    del request.session['username']
    del request.session['password']
    return redirect(log_in)
def save_message(request):
    if request.method=="POST":
        name=request.POST.get('fullName')
        email=request.POST.get('email')
        msg=request.POST.get('message')
        obj=MessageDb(Name=name,Email=email,Message=msg)
        obj.save()
        return redirect(contact_page)