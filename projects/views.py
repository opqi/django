from django.shortcuts import render
from projects.models import Project
from projects.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def home_index(request):
    # projects = Project.objects.all()
    # context = {
        # 'projects' : projects
    # }
    return render(request, 'home_index.html')#, context)


@login_required
def special(request):
    return HttpResponse("You are logged in!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResposeRedirect(reverse('home_index'))


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile.pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }

    return render(request, 'registration.html', context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active():
                login(request, user)
                return HttpResposeRedirect(reverse('home_index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print(f"They used username: {username} and password: {password}")
            return HttpResponse("Invalid logn details given")
    else:
        return render(request, 'login.html', {})


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project' : project
    }
    return render(request, 'project_detail.html', context)
