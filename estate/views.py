from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout


        
# Create your views here.
def home(request):
    if request.method=="POST":
        email = request.POST.get('email_address')
        print(email)
        s_emails = Email(email=email)
        s_emails.save()
    properties= Propertie.objects.all()
    context = {"properties":properties[:12]}
    if request.user.is_authenticated:
        requested_user_id = request.user.id
        try:
            eli = Dealer_Register.objects.filter(request_by=str(requested_user_id)).first()
            eligible = eli.eligible
        except:
            eligible = "NO"
        context.update({"eligible":eligible, "eli":eli})
    return render(request, "home.html", context)



# Create your views here.
def single_property_page(request,sno):
    property1= Propertie.objects.get(sno=sno)
    property1.views = property1.views+1
    property1.save()
    context = {"property":property1}
    return render(request, "single_property_page.html", context)



# Create your views here.
def all_properties(request):
    properties= Propertie.objects.all()
    context = {"properties":properties}
    return render(request, "all_properties.html", context)


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect("/")
        else:
            # return redirect("/login")
            messages.success(request, 'Please Enter a Valid Account!')


    return render(request, "login.html")



# Create your views here.
def signup(request):
    if request.method == "POST":
        email_address = request.POST.get('email_address')
        password = request.POST.get('password')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(email_address,f_name,l_name,username, password1, password2)
        try:
            ma_username = User.objects.get(username=username)
        except:
            ma_username = None
        print(ma_username)
        if ma_username != None:
            messages.error(request, 'Please Choice a Unique Username!')
            return redirect("/signup")
        if password1 != password2:
            messages.error(request, 'Password Does not Match')
        else:
            user = User.objects.create_user(username, email_address, password2)
            user.last_name = l_name
            user.first_name = f_name
            user.save()
            return redirect("/login")

    return render(request, "signup.html")


def logout(request):
    dj_logout(request)
    return redirect("/")

def dealer_register(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    requested_user_id = request.user.id
    eli = Dealer_Register.objects.filter(request_by=str(requested_user_id)).first()
    if eli:
        return redirect("/dealer-dashboard")
    if request.method=="POST":
        age = request.POST.get("age")
        c_phone_num = request.POST.get("c_phone_num")
        address = request.POST.get("address")
        address_2 = request.POST.get("address_2")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip = request.POST.get("zip")
        s_dealer_re = Dealer_Register(age=age, current_phone_number=c_phone_num, address=address, address_2=address_2, city=city, state=state, zip=zip, request_by=request.user.id)
        s_dealer_re.save()
        return redirect("/dealer-dashboard")
    

    return render(request, "dealer_register.html")

def dealer_dashboard(request):
    if request.user.is_authenticated:
        requested_user_id = request.user.id
        try:
            eli = Dealer_Register.objects.filter(request_by=str(requested_user_id)).first()
            eligible = eli.eligible
        except:
            eligible = "NO"
        all_dealer_properties = Propertie.objects.filter(posted_by=requested_user_id)
        context = {
            "eligible":eligible,
            "all_dealer_properties":all_dealer_properties}
        print(context)
        return render(request, "d_dashboard.html",context)
    
    return redirect("/login")


def create_property(request):
    if request.user.is_authenticated:
        requested_user_id = request.user.id
        try:
            eli = Dealer_Register.objects.filter(request_by=str(requested_user_id)).first()
            eligible = eli.eligible
        except:
            eligible = "NO"
    context = {
            "eligible":eligible}
    
    if request.method == "POST":
        purpose = request.POST.get('purpose')
        title = request.POST.get('title')
        area = request.POST.get('area')
        unit = request.POST.get('unit')
        price = request.POST.get('price')
        category = request.POST.get('category')
        city = request.POST.get('city')
        full_location = request.POST.get('full_location')
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        image = request.FILES['image']
        propertie_details = Propertie(purpose=purpose, title=title, area=area, unit=unit, price=price, category=category,city=city, full_location=full_location, name=name, email=email, description=desc, posted_by=requested_user_id, image=image)
        propertie_details.save()
        return redirect("/dealer-dashboard")
    
    return render(request, "create_property.html", context)

def delete_property(request, sno):
    del_property= Propertie.objects.get(sno=sno)
    if request.user.id == del_property.posted_by:
        linked =  "YES"
        del_property.delete()
        return redirect("/dealer-dashboard")
    else:
        linked =  "NO"
    context = {
        "linked":linked,
    }
    return render(request, "delete_property.html", context)

def edit_property(request, sno):
    ed_property= Propertie.objects.get(sno=sno)
    if request.user.id == ed_property.posted_by:
        linked =  "YES"
    else:
        linked =  "NO"
    context = {
        "linked":linked,
        "property":ed_property,
    }
    if request.method == "POST":
        rk = Propertie()
        purpose = request.POST.get('purpose')
        title = request.POST.get('title')
        area = request.POST.get('area')
        unit = request.POST.get('unit')
        price = request.POST.get('price')
        category = request.POST.get('category')
        city = request.POST.get('city')
        full_location = request.POST.get('full_location')
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        try:
            ed_property.image = request.FILES['image']
        except:
            pass
        ed_property.purpose=purpose
        ed_property.title=title
        ed_property.area=area
        ed_property.unit=unit
        ed_property.price=price
        ed_property.category=category
        ed_property.city=city
        ed_property.full_location=full_location
        ed_property.name=name
        ed_property.email=email
        ed_property.description=desc
        ed_property.posted_by=request.user.id
        # propertie_details = ed_property(, , , , , category=category,city=city, full_location=full_location, =name, email=email, description=desc, posted_by=request.user.id)
        ed_property.save()
        return redirect("/dealer-dashboard")

    return render(request, "edit_property.html", context)

def search(request):
    if request.method == "POST":
        search_query = request.POST.get('search')
        print(search_query)
        search_pro0 = Propertie.objects.filter(title=search_query)
        search_pro1 = Propertie.objects.filter(description=search_query)
        search_pro2 = Propertie.objects.filter(city=search_query)
        search_pro = search_pro0.union(search_pro1,search_pro2)
        context = {"properties":search_pro}
    return render(request, "search.html", context)



def buy(request):
    search_query = Propertie.objects.filter(purpose="BUY")
    context = {"properties":search_query}
    return render(request, "buy.html", context)

def sell(request):
    search_query = Propertie.objects.filter(purpose="SELL")
    context = {"properties":search_query}
    return render(request, "sell.html", context)

def rent(request):
    search_query = Propertie.objects.filter(purpose="RENT")
    context = {"properties":search_query}
    return render(request, "rent.html", context)