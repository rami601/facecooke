from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('login',views.login,name="login"),
    path('protected',views.scan,name="protected"),
    path('successs',views.successs,name="successs"),

    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)