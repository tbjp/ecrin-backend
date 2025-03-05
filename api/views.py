from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from datetime import datetime

from properties.models import Property, Issue, Staff
from bookings.models import Booking
from financials.models import Revenue, Expense
from .serializers import (
    PropertySerializer, IssueSerializer, StaffSerializer,
    BookingSerializer, RevenueSerializer, ExpenseSerializer
)

# Property ViewSets
class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    filterset_fields = ['property', 'resolved']

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    filterset_fields = ['property']

# Booking ViewSet
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filterset_fields = ['property', 'status']

# Financial ViewSets
class RevenueViewSet(viewsets.ModelViewSet):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer

    @action(detail=False, methods=['get'])
    def monthly_summary(self, request):
        year = request.query_params.get('year', datetime.now().year)
        monthly_data = Revenue.objects.filter(month__year=year) \
                         .values('month__month') \
                         .annotate(total=Sum('amount')) \
                         .order_by('month__month')

        return Response(monthly_data)

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        year = request.query_params.get('year', datetime.now().year)
        category_data = Expense.objects.filter(month__year=year) \
                         .values('category') \
                         .annotate(total=Sum('amount'))

        return Response(category_data)
