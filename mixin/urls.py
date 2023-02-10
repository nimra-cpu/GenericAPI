from django.contrib import admin
from django.urls import path
from mixin import views

urlpatterns = [
    path('studentapigen/', views.StudentList.as_view()),
    path('studentapigenCreate/', views.StudentCreate.as_view()),
    path('studentapigenRet/<int:pk>', views.StudentRetreive.as_view()),
    path('studentapigenUpd/<int:pk>', views.StudentUpdate.as_view()),
    path('studentapigenDel/<int:pk>', views.StudentDestroy.as_view()),
    path('studentapigenLC/', views.LCStudent.as_view()),
    path('studentapigenRUD/<int:pk>', views.RUDStudent.as_view()),
]