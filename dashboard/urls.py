from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('categories/',views.categories,name='categories'),
    path('categories/add_category/',views.add_category,name="add_category"),
    path('categories/edit_categoty/<int:pk>/',views.edit_category,name='edit_category'),
    path('categories/delete_categoty/<int:pk>/',views.delete_category,name='delete_category'),
    path('posts/',views.posts,name='posts'),
    path('posts/add_posts/',views.add_posts,name='add_posts'),
    path('posts/edit_posts/<int:pk>/',views.edit_posts,name='edit_posts'),
    path('posts/delete_posts/<int:pk>/',views.delete_posts,name='delete_posts'),
    path('logout/',views.logout,name='logout')
]
