from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('', views.home, name='home'),
    path('profile/', include('profiles.urls')),
    path('search/', include('games.urls')),
    path("about/", views.about, name="about"),
    path("faq/", views.faq, name="faq"),
]

handler404 = 'core.views.handler404'
handler500 = 'core.views.handler500'
