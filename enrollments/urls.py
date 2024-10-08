from django.urls import path
from . import views
app_name= 'enrollments'
urlpatterns = [
  #  path('', views.listing, name='listing'),
    path('<int:course_id>', views.enroll, name='enroll'),
]