from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from core.forms import JoinForm, LoginForm
from django.db.models import Q  #for OR queries
from posts.models import Post

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def search(request):
    user = request.user
    if request.method == 'GET':
        search_input = request.GET.get('search_content')
        if user.is_authenticated:
            results = Post.objects.filter(
                Q(title__icontains=search_input) | Q(tags__name__in=[search_input])
            ).distinct()
        else:
            results = Post.objects.filter(
                Q(title__icontains=search_input) | Q(tags__name__in=[search_input]),
                private_status__exact=False
            ).distinct()
        context = {
            "search_results":results,
            "search_input":search_input,
        }
        return render(request, 'core/search.html', context)
    else:
        return render(request, 'core/search.html')

def join(request):
    if(request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            user = join_form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/login/')
        else:
            context = {
            "join_form":join_form,
            }
            return render(request, 'core/join.html',context)
    #else request is GET
    else:
        join_form = JoinForm()
        context = {
        "join_form":join_form,
        }
        return render(request, 'core/join.html', context)

def user_login(request):
    if(request.method == "POST"):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            #get user and password
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            #Built in Django auth function
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    #this does the login
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/login/')
            else:
                print("User login failed.")
                print("Attempted with username: {} and password: {}".format(username, password))
                return render(request, 'core/login.html', {"login_form":LoginForm})
    else:
        return render(request, "core/login.html", {"login_form":LoginForm})

@login_required(login_url="/login/")
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def about(request):
    return render(request, 'core/about.html')
