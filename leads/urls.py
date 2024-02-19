from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('profiles/', views.UserProfileListCreateView.as_view(), name='userprofile-list'),
    path('profiles/<int:pk>/', views.UserProfileRetrieveUpdateDestroyView.as_view(), name='userprofile-detail'),
    path('leads/', views.LeadListCreateView.as_view(), name='lead-list'),
    path('leads/<int:pk>/', views.LeadRetrieveUpdateDestroyView.as_view(), name='lead-detail'),
    path('followups/', views.FollowUpListCreateView.as_view(), name='followup-list'),
    path('followups/<int:pk>/', views.FollowUpRetrieveUpdateDestroyView.as_view(), name='followup-detail'),
    path('agents/', views.AgentListCreateView.as_view(), name='agent-list'),
    path('agents/<int:pk>/', views.AgentRetrieveUpdateDestroyView.as_view(), name='agent-detail'),
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
]