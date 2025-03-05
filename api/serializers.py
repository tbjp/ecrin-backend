from rest_framework import serializers
from properties.models import Property, Issue, Staff
from bookings.models import Booking
from financials.models import Revenue, Expense

# Property Serializers
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'name', 'position', 'joined_date']

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'name', 'date_reported', 'resolved']

class PropertySerializer(serializers.ModelSerializer):
    staff_members = StaffSerializer(many=True, read_only=True)
    issues = IssueSerializer(many=True, read_only=True)
    issue_count = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = [
            'id', 'name', 'image', 'location', 'rooms',
            'staff_count', 'bookings_count', 'has_issues',
            'issue_count', 'issues', 'staff_members', 'added_date'
        ]

    def get_issue_count(self, obj):
        return obj.issues.filter(resolved=False).count()

# Booking Serializers
class BookingSerializer(serializers.ModelSerializer):
    property_name = serializers.CharField(source='property.name', read_only=True)
    nights = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = [
            'id', 'property', 'property_name', 'guest_name',
            'check_in', 'check_out', 'nights', 'price_per_night',
            'total_price', 'status'
        ]

    def get_nights(self, obj):
        return (obj.check_out - obj.check_in).days

# Financial Serializers
class RevenueSerializer(serializers.ModelSerializer):
    property_name = serializers.CharField(source='property.name', read_only=True)
    month_name = serializers.SerializerMethodField()

    class Meta:
        model = Revenue
        fields = ['id', 'property', 'property_name', 'month', 'month_name', 'amount']

    def get_month_name(self, obj):
        return obj.month.strftime('%b')

class ExpenseSerializer(serializers.ModelSerializer):
    property_name = serializers.CharField(source='property.name', read_only=True)
    month_name = serializers.SerializerMethodField()

    class Meta:
        model = Expense
        fields = ['id', 'property', 'property_name', 'category', 'month', 'month_name', 'amount', 'description']

    def get_month_name(self, obj):
        return obj.month.strftime('%b')
