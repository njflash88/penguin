from django.urls import path
from . import views
from courses.models import Course

urlpatterns = [
    path('', views.index, name='courses'),
    path('<int:course_id>', views.listing, name='course'),
]
#print("** URL=", urlpatterns[1])