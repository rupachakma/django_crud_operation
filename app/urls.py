from django.urls import path

from app import views

urlpatterns = [
    path('',views.home,name="homepage"),
    path('signuppage',views.signuppage,name="signuppage"),
    path('loginpage',views.loginpage,name="loginpage"),
    path('logoutpage',views.logoutpage,name="logoutpage"),
    path('addpage',views.addpage,name="addpage"),
    path('deletepage<int:id>',views.deletepage,name="deletepage"),
    path('updatepage<int:id>',views.updatepage,name="updatepage"),
]
