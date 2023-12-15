from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    path('login/', views.UserLogInView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit', views.EditProfileView.as_view(), name='edit_profile'),
    path('profile/changePassword', views.EditPasswordView.as_view(), name='edit_password'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]
