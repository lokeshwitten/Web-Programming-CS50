from django.urls import path
from . import views
urlpatterns=[
    path("/",views.index,name='index'),
    path("/lokesh",views.lokesh,name='lokesh'),
    path("/lok",views.lok,name='lok'),
    path("/<str:name>",views.greet,name='greet')
]