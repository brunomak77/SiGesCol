from django.urls import path
from . import views
from .views import (UserAvalListView,
                    UserAvalDetailView,
                    UserAvalCreateView,
                    # PostUpdateView,
                    # PostDeleteView,
                    # UserPostListView
                    )


urlpatterns = [
    path('', views.user_list, name='user-list'),
    path('user_aval/<str:username>/list/', UserAvalListView.as_view(), name='user-aval-list'),
    path('user_aval/<int:pk>/detail/', UserAvalDetailView.as_view(), name='user-aval-detail'),
    path('user_aval/<str:username>/new/', UserAvalCreateView, name='user-aval-create'),
]
