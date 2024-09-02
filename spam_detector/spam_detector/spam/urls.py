from django.urls import path
from django.shortcuts import render
from .views import register, user_login, user_logout, submit_spam_number, spam_success, search_spam_numbers, logged_out

urlpatterns = [
    path("register/", register, name='register'),
    path("login/", user_login, name='login'),
    path("logout/", user_logout, name='logout'),
    path("submit/", submit_spam_number, name='submit_spam_number'),
    path("success/", spam_success, name='spam_success'),
    path("logged_out1/", logged_out, name="logged_out1"),
    path("search/", search_spam_numbers, name='search_spam_numbers'),
]