from django.urls import path

from .views import UserRegistrationView, SuperUserRegistration, UserLoginView, PasswordChangeView, UpdateRoleView

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name='register'),
    path('register-admin', SuperUserRegistration.as_view(), name='register-admin'),
    path('login', UserLoginView.as_view(), name='login'),
    path('change-password', PasswordChangeView.as_view(), name='change-password'),
    path('update-role', UpdateRoleView.as_view(), name='update_role'),
    # path('users', UserListView.as_view(), name='users')
]
