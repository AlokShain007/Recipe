from django.urls import path
from vege.views import *


urlpatterns = [
    path('',receipes,name="receipes"),
    path('delete_receipe/<id>/',delete_receipe),
    path('update_receipe/<id>/',update_receipe,name="update_receipe"),
    path("login/",login_page,name="login_page"),
    path("register/",register_page,name="register_page"),
    path('logout/',logout_page,name="logout_page"),
    path("amazone",amazone_view),
    path('get_student/',get_student,name="get_student"),
    path('see_marks/<str:id>/', see_marks, name='see_marks')

]


