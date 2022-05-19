from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.static import serve
from django.urls import re_path as url

urlpatterns = [
    path('change_user/',views.change_user,name="changeuser"),
    path('change_pass/',views.change_pass,name="changepass"),
    path('sendcode/',views.sendcode,name="sendcode"),
    path('verify_code/',views.verify_code,name="verify_code"),
    path('login/',views.__login__,name="login"),
    path('logout/',views.__logout__,name="logout"),
    path('signup/',views.signin,name="signup"),
    path('about/',views.about,name="about"),
    path('admin/', admin.site.urls),
    path('',views.index,name="main"),
    path('blog/',include('blog.urls')),
    path('contact/',include('contact.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]