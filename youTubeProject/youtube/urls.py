from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comment/<int:pk>/', views.CommentsDetail.as_view()),
]
