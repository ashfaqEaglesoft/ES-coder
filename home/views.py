from django import http
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import query
from django.http.response import HttpResponseServerError
from django.shortcuts import render , HttpResponse ,redirect
from home.models import contact as con
from blog.models import post as po
from django.contrib import messages

# Create your views here.
def index(request):
    allPost=po.objects.all()
    conext={'allPost':allPost}
    return render(request,'home/index.html',conext)
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        msg=request.POST.get('msg')
        if name=='' or email=='':
            messages.error(request, 'Please fill the form carefully')
        else:
            contact=con(name=name,email=email,phone=phone,msg=msg)
            contact.save()
            messages.success(request, 'Congrates! your data submit success fully')
    return render(request,'home/contact.html')

def search(request):
    query=request.GET['query']
    postTitle=po.objects.filter(post_title__contains=query)
    postContent=po.objects.filter(post_content__contains=query)
    allPost=postTitle.union(postContent)
    if len(allPost)<1:
        messages.warning(request, 'Search with precise Queries')
    data={
        "allPost":allPost
    }
    return render(request,"home/search.html",data)
def about(request):
    return render(request,'home/about.html')

def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        # check for user 
        if len(username)>10:
                messages.error(request,"Username must be under 10 character! ")
                return redirect('/') 
        if not username.isalnum():
                messages.error(request,"Username must be Alpha & numeric character! ")
                return redirect('/') 
        if pass1!=pass2:
                messages.error(request,"Password Does not match")
                return redirect('/') 
        # create user account
        user=User.objects.create_user(username, email, pass1)
        # user.first_name = fname
        # user.last_name = lname
        user.save()
        messages.success(request,"Your Account created successfully")
        return redirect('/')
    return HttpResponse("404- Page not Found")

def handlelogin(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginuserpassword=request.POST['loginuserpassword']
        user = authenticate(username=loginusername, password=loginuserpassword)
        if user is not None:
            login(request,user)
            messages.success(request,f"your are login in as {loginusername}")
            return redirect("/")
        else:
            messages.error(request,"Invalid Credentionls! Please Try again")
            return redirect("/")
    return HttpResponse("404 Error")
def handlelogout(request):
    logout(request)
    messages.success(request,"Your are logout")
    return redirect("home")
