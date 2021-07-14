from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dept/',views.department,name='department'),
    path('dep_detail/<slug:slug>/', views.dep_detail,name='dep_detail'),
    path('doc_detail/<slug:slug>/', views.doc_detail,name='doc_detail'),
    path('doc/',views.doctor,name='doctor'),
    path('signup/',views.user_signup,name='user_signup'),
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('appnmnt/',views.appoinment,name='appoinment'),


]
