from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm, UserCompleteForm, UserRegisterForm


def register(request):
    if request.method == 'POST':
        form_r = UserRegisterForm(request.POST)
        if form_r.is_valid():
            form_r.save()
            username = form_r.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login, {username}!')
            return redirect('login')
    else:
        form_r = UserRegisterForm()
    return render(request, 'register.html', {'form_r': form_r})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        uc_form = UserCompleteForm(request.POST, instance=request.user.usercomplete)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)


        if u_form.is_valid() and uc_form.is_valid() and p_form.is_valid():
            u_form.save()
            uc_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        else:
            messages.warning(request, f"Your account hasn't been updated!")
    else:
        u_form = UserUpdateForm(instance=request.user)
        uc_form = UserCompleteForm(instance=request.user.usercomplete)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'uc_form': uc_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)
