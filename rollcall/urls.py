from django.urls import path
from.import views

urlpatterns =[
    path('students/',views.students,name="students"),
    path('students/details/<int:id>',views.details,name='views'),
    path('',views.main,name="main"),
]
