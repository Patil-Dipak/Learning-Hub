from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("servises",views.servises, name='servise'),
    path("contact",views.contact, name='contact'),
    path("bca",views.bca, name='bca'),
    path("imca",views.imca, name='imca'),
    path("mca",views.mca, name='mca'),
    path("login",views.userlogin, name='login'),
    path("signup",views.signup, name='signup'),
    path("user_home",views.user_home, name='user_home'),
    path("user_profile",views.user_profile, name='user_profile'),
    path("upload_notes",views.upload_notes, name='upload_notes'),
    path("adlogin",views.adlogin, name='adlogin'),
    path("changepass",views.changepass, name='changepass'),
    path("admin_profile",views.admin_profile, name='admin_profile'),
    path("logout",views.Logout, name='logout'),
    path("edit_user_profile",views.edit_user_profile, name='edit_user_profile'),
    path("view_notes",views.view_notes, name='view_notes'),
    
    path("view_all_notes",views.view_all_notes, name='view_all_notes'),
    #delete notes for admin
    path("delete_notes/<int:pid>",views.delete_notes, name='delete_notes'),
    #view user for admin
    path("view_user",views.view_user, name='view_user'),
    #delete user
    path("delete_user/<int:pid>",views.delete_user, name='delete_user'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
