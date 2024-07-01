from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='homepage'),
    path('home/', views.home, name='home'),
    path('update_user/', views.Profile, name='update-user'),
    path('list/', views.list_view, name='list_without_id'),  
    path('list/<int:id>/', views.list_view, name='list_view'),  
    path('item/<int:item_id>/', views.item_info, name='item'),  
    path('my-bookings/', views.student_bookings, name='student-bookings'),

    path('delete-item/', views.delete_item, name='delete_item'),  
    path('index', views.index, name='index'),  
]

