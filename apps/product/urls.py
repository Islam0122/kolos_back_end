from django.urls import path
from .api import views
from .api.views import MoveDefectiveToNormalAPIView, MoveNormalToDefectiveAPIView

urlpatterns = [

    path('', views.ProductItemViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),

    path('<int:pk>/', views.ProductItemViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    })),

    path('defect/', views.ProductDefectItemViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),

    path('defect/<int:pk>/', views.ProductDefectItemViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
    })),
    path('move_defect_to_normal/', MoveDefectiveToNormalAPIView.as_view() ),
    path('move_normal_to_defect/', MoveNormalToDefectiveAPIView.as_view()),

    path('archive/', views.ArchivedProductView.as_view({
        'get': 'list'
    })),

    path('archive/<int:pk>/', views.ArchivedProductView.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'restore'
    })),

    # product-> search
    path('search/', views.Search.as_view()),

]