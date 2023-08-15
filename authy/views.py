from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from authy.forms import SignUpForm,SignInForm
from django.urls import reverse

def signin_view(request):
    form=SignInForm(request.POST or None)
    msg=None
    if request.method=="POST":
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(reverse('home'))
            else:
                msg="Invalid Credntials"
                form=SignInForm()
        else:
            msg="Validation Error"

    return render(request,'account/signin.html',{"form":form,"msg":msg})


def signup_view(request):
    msg=None
    success=True
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            true_password=form.cleaned_data.get("password1")
            print(username,true_password)
            user=authenticate(username=username,password=true_password)
            #msg = 'User created - please <a href="/auth/login">login</a>.'
            success = True
            return redirect(reverse("login"))
        else:
            msg="Error registering user"
    else:
        form=SignUpForm()
    return render(request,"account/signup.html",{"form":form,"msg":msg,"success":success})

def signout_view(request):
    logout(request)
    bye_msg="'Thanks for reading our post. See Yah!<a style='color:green;' href='/auth/login'> <b>LogIn Again</b></a>'"
    return render(request,"account/signout.html",{'msg':bye_msg})