""" URLConf """


from django.urls import path
from tasks import views


# Create your URLConf here.
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

    # Lists
    path('lists/', views.ListView.as_view(), name='lists'),
    path('lists/new/', views.ListCreateView.as_view(), name='create_list'),
    path('lists/<int:pk>/', views.ListDetailView.as_view(), name='list_detail'),
    path('lists/<int:pk>/update/', views.ListUpdateView.as_view(), name='update_list'),
    path('lists/<int:pk>/delete/', views.ListDeleteView.as_view(), name='delete_list'),


    # Tasks
    path('tasks/new/', views.TaskCreateView.as_view(), name='create_task'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='update_task'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete_task'),
]