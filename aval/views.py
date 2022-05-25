from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from .models import Avaliation
from users.forms import UserUpdateForm
from .forms import AvaliationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    # UpdateView,
    # DeleteView
)


@login_required
def user_list(request):
    context = {
        'users_t': User.objects.all()
    }
    return render(request, 'user_list.html', context)


class UserAvalListView(LoginRequiredMixin, ListView):
    context = {
        'ua_list': Avaliation.objects.all(),
    }
    model = User
    # slug_field = 'username'
    # slug_url_kwarg = 'username'
    template_name = 'user_aval_list.html'
    context_object_name = 'ua_list'
    ordering = ['-date_posted']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Avaliation.objects.filter(user=user).order_by('-date_posted')

    @property
    def media(self, a, b, c, d, e, f, g, h, i, j):
        result = int(a+b+c+d+e+f+g+h+i+j)
        return result


class UserAvalDetailView(LoginRequiredMixin, DetailView):
    context = {
        'ua_detail': Avaliation.objects.all()
    }
    model = Avaliation
    context_object_name = 'ua_detail'
    template_name = 'user_aval_detail.html'

@login_required()
def UserAvalCreateView(request, *args, **kwargs):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        uac_form = AvaliationForm(request.POST, instance=request.user)
        if uac_form.is_valid():
            u_form.save()
            uac_form.save()
            messages.success(request, f'Your avaliation has been created!')
            print('eu passo por aqui?')
            return redirect('../../<int:pk>')
    else:
        u_form = UserUpdateForm(instance=request.user)
        uac_form = AvaliationForm(instance=request.user)
        print('eu passo por aqui em algum instante??')

    context = {
        # 'u_form': u_form,
        'uac_form': uac_form,
    }
    print('Por aqui eu passo!')
    return render(request, 'user_aval_create.html', context)









# class UserAvalCreateView(LoginRequiredMixin, CreateView):
#     model = Avaliation
#     context = {
#         'uac_detail': Avaliation.objects.all()
#     }
#     slug_field = 'username'
#     slug_url_kwarg = 'username'
#     template_name = 'user_aval_create.html'
#     context_object_name = 'uac_detail'
#     fields = ['tee', 'pro', 'lid', 'fle', 'ini', 'pon', 'com',
#               'cup', 'pst', 'err', 'org', 'cpi', 'p_pos', 'p_neg']
#
#     def form_valid(self, uac_form):
#         uac_form.instance.user = self.request.user
#         return super().form_valid(uac_form)
