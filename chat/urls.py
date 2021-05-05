from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('profile/<str:username>', views.profile, name="profile"),
    path("addition1", views.addition1, name="addition1"),
    path("addition2", views.addition2, name="addition2"),
    path("multiplication", views.multiplication, name="multiplication"),
    # api
    path('record/<str:skill>', views.record)
    ]