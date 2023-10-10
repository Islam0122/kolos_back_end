from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('distributor', views.DistributorViewSet, 'api_distributor')


urlpatterns = router.urls