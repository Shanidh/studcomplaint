from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.newfunction,name='index'),
    path('login',views.newfunction1,name='login'),
    path('signup',views.newfunction2,name='signup'),
    path('base',views.newfunction3,name='base'),
    path('addcomplaints',views.newfunction4,name='addcomplaints'),
    path('changepassword',views.newfunction5,name='changepassword'),
    path('editprofile',views.newfunction6,name='editprofile'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)