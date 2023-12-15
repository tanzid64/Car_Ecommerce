from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.models import User
from .forms import SignUpForm, ChangeUserForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from . models import History
# Create your views here.
# Sign Up
class UserSignUpView(CreateView):
    template_name = 'user.html'
    form_class = SignUpForm
    model = User
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Congratulations, SignUp successfull..!!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Sign Up'
        return context

# Profile
@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    template_name = 'profile.html'
    model = User
    def get_object(self):
        return self.request.user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["history"] = History.objects.filter(user = self.request.user)
        return context
    
    # context_object_name = 'history'
    # def get_queryset(self):
    #     user = self.request.user
    #     return History.objects.filter(user=user)


# Edit Profile
@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView):
    model = User
    template_name = 'user.html'
    form_class = ChangeUserForm
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Profile Updated Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.danger(self.request, 'Information Incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Update Your Profile'
        return context 

# Edit Password
@method_decorator(login_required, name='dispatch')
class EditPasswordView(PasswordChangeView):
    template_name = 'user.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Password Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Update Your Password'
        return context
    
# Log in
class UserLogInView(LoginView):
    template_name = 'user.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.danger(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Log In'
        return context
    
# Log Out
@method_decorator(login_required, name='dispatch')
class UserLogoutView(LogoutView):
    def get_success_url(self):
        messages.success(self.request, 'Logged out successfully')
        return reverse_lazy('login')