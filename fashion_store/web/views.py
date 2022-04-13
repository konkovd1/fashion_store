from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

from fashion_store.web.forms import CreateProfileForm
from fashion_store.web.mixins import RedirectToHome
from fashion_store.web.models import Products, Profile


class HomePageView(views.TemplateView):
    template_name = 'home_page.html'


class UserLoginView(auth_views.LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class ProductListView(views.ListView):
    model = Products
    template_name = 'products_page.html'
    context_object_name = 'item'

    def get_queryset(self):
        return super() \
            .get_queryset()


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'profile_details.html'
    context_object_name = 'profile'
