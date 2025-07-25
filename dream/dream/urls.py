"""dream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from market import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('elements',views.elements,name='elements'),
    path('generic', views.generic, name='generic'),
    path('landing',views.landing,name='landing'),
     path('signup',views.signup , name='signup'),
    path('signin',views.signin,  name= 'signin'),
    path('logout',views.logoutUser,name='logout'),
    path('sendletter',views.sendletter, name='sendletter'),
    path('prost',views.prost, name='prost'),
    path('Genre/<int:genre_id>/' , views.show_category, name='Genre'),
    path('admin/',views.adminPage ,name='user-page'),
    path('post/<int:post_id>/',views.show_post,name='post'),
    path('profile',views.profile, name='profile'),
    path('<int:pk>/edit', views.edit, name='edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
