from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='properties/')
    location = models.CharField(max_length=100)
    rooms = models.IntegerField()
    staff_count = models.IntegerField(default=0)
    bookings_count = models.IntegerField(default=0)
    has_issues = models.BooleanField(default=False)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Issue(models.Model):
    property = models.ForeignKey(Property, related_name='issues', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_reported = models.DateField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} at {self.property.name}"

class Staff(models.Model):
    name = models.CharField(max_length=100)
    property = models.ForeignKey(Property, related_name='staff_members', on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
