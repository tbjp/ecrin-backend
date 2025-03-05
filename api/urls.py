from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PropertyViewSet, IssueViewSet, StaffViewSet,
    BookingViewSet, RevenueViewSet, ExpenseViewSet
)

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'issues', IssueViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'revenues', RevenueViewSet)
router.register(r'expenses', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
