from django.urls import include, re_path
from django.contrib.auth import views as auth_views
from .views import ProfilePageView, DeleteAccountView, register_user, edit_username, edit_emailaddress


app_name = 'accounts'

urlpatterns = [
    re_path('login/', auth_views.LoginView.as_view(), name='login'),
    re_path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    re_path('change-password/', auth_views.PasswordChangeView.as_view(), name='change_password'),
    re_path('change-password-done/', auth_views.PasswordChangeDoneView.as_view(), name='change_password_done'),
    re_path('profile/', ProfilePageView.as_view(), name='profile'),
    re_path('register-user/', register_user, name='register_user'),
    re_path('edit-username/', edit_username, name='edit_username'),
    re_path('edit-emailaddress/', edit_emailaddress, name='edit_emailaddress'),
    re_path('delete-account/(?P<pk>\d+)/', DeleteAccountView.as_view(), name='delete_account')
]
