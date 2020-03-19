# backend/urls.py
# This code specifies the URL path for the API:

from django.contrib import admin
from django.urls import path, include, re_path                 # add this
from rest_framework import routers                    # add this
from todo import views as todo_views
from students import views as students_views
from django.conf.urls import url                           # add this

router = routers.DefaultRouter()                      # add this
router.register(r'todos', todo_views.TodoView, 'todo')     # add this

urlpatterns = [
	path('admin/', admin.site.urls),         
	path('api/', include(router.urls)),
	re_path(r'^api/todo/$', todo_views.TodoView),
	re_path(r'^api/students/$', students_views.students_list),
	re_path(r'^api/students/(?P<pk>[0-9]+)$', students_views.students_detail),
	]
 
