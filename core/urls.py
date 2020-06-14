from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ProfessionViewSet, DataSheetViewSet, DocumentViewSet

# Created router instance & use it to register the end points.
router = DefaultRouter()

# need to add basename since we added custom get_queryset method in the CustomerViewSet
router.register('customers', CustomerViewSet, basename="customers")

router.register('professions', ProfessionViewSet)
router.register('data-sheet', DataSheetViewSet)
router.register('documents', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
