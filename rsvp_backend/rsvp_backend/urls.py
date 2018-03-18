from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from rsvp import views

router = routers.DefaultRouter()
router.register(r'people', views.PersonViewSet)
router.register(r'invitations', views.InvitationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
]
