from django.urls import path
from . import views

app_name = 'forums'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:forum_id>', views.forums, name='forums'),
    path('post', views.post, name='post'),
    path('add', views.add, name='add'),
]