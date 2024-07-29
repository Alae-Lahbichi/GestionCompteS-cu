from django.urls import path
from .views import  main_page , sign_up_page , login_page
from django.contrib.auth import views as auth_views


app_name = "app1"


urlpatterns = [
    path('signup/', sign_up_page , name="signup"),
    path('main/' , main_page , name="main") , 
    path('login/', login_page , name="login"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
