from django.shortcuts import render, redirect
from user.forms import UserRegistrationForm, LoginForm, ProfileForm
from django.contrib.auth.models import auth
from django.contrib.auth import login, logout
from user.models import Profile


def login_page(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.data.get('username'), password=form.data.get('password'))
            if user is not None:
                login(request, user)
                try:
                    Profile.objects.get(owner_id=user.id)
                except:
                    profile = Profile(owner_id=user.id)
                    profile.save()
                return redirect('/')
            else:
                return render(request, 'user/login.html', {'form': form})
        else:
            return render(request, 'user/login.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect('/auth/login')


def register_page(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, 'user/register.html', {'form': form})
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            profile = Profile(owner_id=user.id)
            profile.save()
            return redirect('/auth/login/')
        else:
            return render(request, 'user/register.html', {'form': form})


def settings_page(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            profile = Profile.objects.get(owner_id=request.user.id)
            form = ProfileForm(data={'bio': profile.bio, 'image': profile.image})
            return render(request, 'user/settings.html', {'form': form, 'profile': profile})
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            profile = Profile.objects.get(owner_id=request.user.id)
            print(form.files)
            if form.is_valid():
                bio = form.data.get('bio')
                image = form.files.get('image')
                resume = form.files.get('resume')
                profile.bio = bio
                profile.image = image
                profile.resume = resume
                profile.save()
                return redirect('/auth/settings/')
            else:
                return render(request, 'user/settings.html', {'form': form, 'profile': profile})
    else:
        return redirect('/')
