from django.shortcuts import render,redirect
from capp.models import CategoryDb,CaseDb
from webapp.models import RegistrationDb, CartDB
from webapp.models import MessageDb
from django.contrib import messages


# Create your views here.
def home_page(request):
    cart_count=0
    uname = request.session.get('username')
    if uname:
        cart_count=CartDB.objects.filter(Username=request.session['username']).count
    categories=CategoryDb.objects.all()
    return render(request,"home.html",{'categories':categories,'cart_count':cart_count})
def all_products(request):
    categories = CategoryDb.objects.all()
    cart_count = 0
    uname = request.session.get('username')
    if uname:
        cart_count = CartDB.objects.filter(Username=request.session['username']).count
    cases=CaseDb.objects.all()
    return render(request,"products.html",{'cases':cases,'categories':categories,'cart_count':cart_count})
def all_materials(request):
    categories=CategoryDb.objects.all()
    cart_count = 0
    uname = request.session.get('username')
    if uname:
        cart_count = CartDB.objects.filter(Username=request.session['username']).count
    return render(request,"materials.html",{'categories':categories,'cart_count':cart_count})
def about_us(request):
    categories = CategoryDb.objects.all()
    cart_count = 0
    uname = request.session.get('username')
    if uname:
        cart_count = CartDB.objects.filter(Username=request.session['username']).count
    return render(request,"about_us.html",{'categories':categories,'cart_count':cart_count})
def contact_page(request):
    categories = CategoryDb.objects.all()
    cart_count = 0
    uname = request.session.get('username')
    if uname:
        cart_count = CartDB.objects.filter(Username=request.session['username']).count
    return render(request,"contact.html",{'categories':categories,'cart_count':cart_count})


def cart_page(request):

    cases=CartDB.objects.filter(Username=request.session['username'])
    # count in cart icon
    cart_count = 0
    uname = request.session.get('username')
    if uname:
        cart_count = CartDB.objects.filter(Username=request.session('username')).count

    # calculating total amount
    sub_total=0
    discount=0
    delivery_charge=0
    total_amount=0
    for i in cases:
        sub_total+=i.Total_Price
        if sub_total>500:
            delivery_charge=50
        else :
            delivery_charge=100
        total_amount=sub_total+delivery_charge

    return render(request,"cart_page.html",{'cases':cases,'cart_count':cart_count,
                                            'sub_total':sub_total,'delivery_charge':delivery_charge,
                                            'total_amount':total_amount,'discount':discount})


def filtered_page(request,model):
    cover=CaseDb.objects.filter(Phone_Model=model )
    cart_count = 0
    uname = request.session.get('username')
    if uname:
        cart_count = CartDB.objects.filter(Username=request.session['username']).count
    return render(request,"filtered.html",{'cover':cover,'cart_count':cart_count})
def material_filter_page(request,mate):
    categories = CategoryDb.objects.all()
    cart_count = 0
    uname = request.session.get('username')
    if uname:
        cart_count = CartDB.objects.filter(Username=request.session['username']).count
    material=CaseDb.objects.filter(Material=mate)
    return render(request, "mate_filtered.html",{'material': material,'categories':categories,'cart_count':cart_count})
def single_case(request,case_name):
    categories = CategoryDb.objects.all()
    cart_count = 0
    uname = request.session.get('username')
    if uname:
        cart_count = CartDB.objects.filter(Username=request.session['username']).count
    single=CaseDb.objects.get(Cover_Name=case_name)
    return render(request,"single_case.html",{'single':single,'categories':categories,'cart_count':cart_count})

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

def save_cart(request):
    if request.method=="POST":
        cover_name=request.POST.get('covername')
        qty=int(request.POST.get('quantity'))
        price=int(request.POST.get('price'))
        total=int(request.POST.get('total'))
        uname=request.POST.get('user_name')
        case=CaseDb.objects.filter(Cover_Name=cover_name).first()
        img=case.Cover_Image if case else None
        obj=CartDB(Username=uname,CoverName=cover_name,Quantity=qty,Price=price,
                   Total_Price=total,Case_Image=img)
        obj.save()
        messages.success(request, "Added to Cart")


        return redirect(home_page)