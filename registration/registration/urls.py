"""
URL configuration for registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup.html/', views.signup, name='signup'),
    path('login.html/', views.login, name='login'),
    path('home.html/', views.home, name='home'),
    path('form.html/', views.form, name='form'),
    path('logout.html/',views.Logout,name='logout'),
    # path('signup2.html/', views.signup2, name='signup2'),
    path('login2.html/', views.login2, name='login2'),
    path('home2.html/', views.home2, name='home2'),
    # path('form2.html/', views.form, name='form2'),
    path('logout2.html/',views.Logout,name='logout'),

    
]
# Static file serving during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  
