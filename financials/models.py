from django.db import models
from properties.models import Property

class Revenue(models.Model):
    property = models.ForeignKey(Property, related_name='revenues', on_delete=models.CASCADE, null=True, blank=True)
    month = models.DateField()  # Store the first day of the month
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        if self.property:
            return f"{self.property.name} - {self.month.strftime('%b %Y')}"
        return f"Total - {self.month.strftime('%b %Y')}"

class Expense(models.Model):
    EXPENSE_CATEGORIES = (
        ('cleaning', 'Cleaning'),
        ('maintenance', 'Maintenance'),
        ('utilities', 'Utilities'),
        ('staff', 'Staff'),
        ('other', 'Other'),
    )

    property = models.ForeignKey(Property, related_name='expenses', on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=20, choices=EXPENSE_CATEGORIES)
    month = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True)
