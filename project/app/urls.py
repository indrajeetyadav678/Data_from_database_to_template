from django.urls import path
from . import views

urlpatterns=[
    path("home/",views.home,name='home'),
    # path("home1/",views.home1,name='home1'),
    # path("dateTime/",views.filter_datetime,name='dateTime'),
    # path("float/",views.float_format,name='float'),
    # path("if_tag/",views.if_tag,name="if_tag") 
]