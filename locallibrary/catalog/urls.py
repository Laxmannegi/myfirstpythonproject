from django.urls import path

from . import views

urlpatterns = [
      path('', views.index, name='index'),
      path('authors/', views.AuthorListView.as_view(), name='authors'),
      path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail')
]


# Add URLConf to create, update, and delete authors
urlpatterns += [  
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]