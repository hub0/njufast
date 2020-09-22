from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from info.forms import MemberUpdateForm



@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        m_form = MemberUpdateForm(
            request.POST, 
            instance=request.user.teammember)
        if u_form.is_valid():
            u_form.save()
        if m_form.is_valid():
            m_form.save()
            messages.success(request, f'Profile updated')
            return redirect('user_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        m_form = MemberUpdateForm(instance=request.user.teammember)

    context = {
        'u_form': u_form,
        'm_form': m_form,
    }

    return render(request, 'core/user_profile.html', context)
