from django.contrib import admin
from django.urls import path, include
from . import views as accountsView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('users', accountsView.UserCreateAPIView, basename='users')

urlpatterns = [
    #path('createUser/', accountsView.UserCreateAPIView.as_view()),
    
    path('',include(router.urls)),
]
