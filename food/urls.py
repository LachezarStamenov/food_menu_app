from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    # /food/
    path('', views.index, name='index'),
    # /food1
    path('<int:item_id>/', views.detail, name='detail'),
    path('item/', views.item, name='item'),
    # add items
    path('add', views.create_item, name='create_item'),
    # edit items
    path('update/<int:id>', views.update_item, name='update_item'),
    # delete
    path('delete/<int:id>', views.delete_item, name='delete_item'),
]
