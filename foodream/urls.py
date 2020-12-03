"""foodream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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


from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import social.views 
import myapp.views
import upload.views
import mileage.views
import mypage.views
import cart.views
from upload.views import FormLike, FormFavorite

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', social.views.signin, name="signin"),
    path('accounts/', include('allauth.urls')),
    path('home/', myapp.views.home, name="home"),

    path('upload/',upload.views.upload, name = "upload"),
    path('form/<int:form_id>/', upload.views.detail , name= "detail"),
    path('create', upload.views.create, name= 'create'),
    path('list/', upload.views.list , name= "list"),
    #좋아요구현
    path('like/<int:form_id>/', FormLike.as_view(), name="like"),     # upload.views.FormLike
    path('favorite/<int:form_id>/', FormFavorite.as_view(), name="favorite"), # upload.views.FormFavorite
    path('donate_li/', mileage.views.donate_li , name= "donate_li"),
    path('create', myapp.views.create , name= "create"),
    path('form/<int:form_id>/delete/', myapp.views.delete , name= "delete"),
    path('form/<int:form_id>/edit', myapp.views.edit , name= "edit"),
    path('form/<int:form_id>/update', myapp.views.update , name= "update"),



    path('mileage/<int:mileage_id>', mileage.views.content, name= "content"),
    path('mileage/<int:mileage_id>/donate', mileage.views.donate, name= "donate"),
    path('mileage/popup', mileage.views.popup, name = "popup"),
    
    path('mypage/', mypage.views.mypage, name="mypage"),
    # path('sell/', mypage.views.sell, name="sell"), 
    path('buy/', mypage.views.buy, name="buy"),  
    path('wish/', mypage.views.wish, name="wish"),
    # path('accounts/kakao/login/callback/', myapp.views.home, name="kakao callback"),
    path('cart/', include('cart.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

