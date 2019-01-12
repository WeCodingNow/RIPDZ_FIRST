from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.views.generic.edit import FormMixin, ModelFormMixin

from .forms import LoginForm, RegistrationForm, ProgramCreateForm
from .models import Profile, Program

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class ProgrammerLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form_action'] = reverse('login')
        return data

    def get_success_url(self):
        return reverse('programs')


class ProgrammerLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return HttpResponseRedirect(reverse('login'))


class ProgrammerRegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'

    def get_success_url(self):
        return reverse('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProgrammListView(LoginRequiredMixin, ListView):
    model = Program
    template_name = 'programs.html'
    context_object_name = "abc"
    success_url = 'index.html'
    fields = []

    def post(self, request, *args, **kwargs):
        form = ProgramCreateForm(self.request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/programs')
            #self.form_valid(form)
        else:
            return HttpResponseRedirect('/programs')
            #return self.form_invalid(form)


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form_create'] = ProgramCreateForm()
        return data

    def get_queryset(self):
        return self.model.objects.order_by('-id').filter(programmers = self.request.user)
