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
    path('move_defect_to_normal/<int:pk>/', MoveDefectiveToNormalAPIView.as_view() ),
    path('move_normal_to_defect/<int:pk>/', MoveNormalToDefectiveAPIView.as_view()),

    # path('normal/', views.ArchivedProductView.as_view({
    #     'get': 'list'
    # })),

    path('archive/', views.CombinedProductView.as_view(), name='combined-products'),

    path('archive-normal/<int:pk>/', views.ArchivedProductView.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'restore'
    })),

    # path('archive/', views.ArchivedProductView.as_view(), name='archived-products'),

    # path('defect/archive/', views.ArchivedDefectProductView.as_view({
    #     'get': 'list'
    # })),

    path('archive-defect/<int:pk>/', views.ArchivedDefectProductView.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'restore'
    })),

    # product-> search
    path('clue-products/', views.Search.as_view()),
    path('clue-defect-products/', views.SearchDefect.as_view({
        'get': 'list', 'post': 'create'
    })),

    path('category-name/', views.CategoryListAPIView.as_view()),

    # path('combined-products/', CombinedProductView.as_view(), name='combined-products')
]