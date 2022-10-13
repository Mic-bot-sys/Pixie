from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def login(request):
    if request.method == "POST":
        # username = request.POST['username']
        # password = request.POST['password']
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html')
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'login/login.html')

    else:
        return render(request, 'login/login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'index.html')



def register(request):

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return render(request, 'login/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return render(request, 'login/register.html')          
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                user.save();
                print("{} account Created".format(user.first_name))
                return render(request, 'login/login.html')
            
        else:
            print("Passwords not matching")
            messages.info(request, "Passwords not matching")
            return render(request, "login/register.html")
        return render(request, 'login/index.html')
    else:
        return render(request, 'login/register.html')
