from django.db import models
from datetime import date

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Amenity(models.Model):
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, blank=True, help_text="Enter the Bootstrap or FontAwesome icon class.")

    def __str__(self):
        return self.name


class Home(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bathrooms = models.IntegerField()
    address = models.CharField(max_length=200)
    rating = models.FloatField()
    amenities = models.ManyToManyField(Amenity, related_name="homes")
    subheading = models.TextField()
    available_from = models.DateField(null=True, blank=True, default=date.today)
    available_to = models.DateField(default=date(2099, 12, 31))  # Example default value

    def __str__(self):
        return f"Home ID: {self.id}, Description: {self.description}, Guests: {self.guests}"
    
class HomeImage(models.Model):
    home = models.ForeignKey(Home, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Website/static/image_uploads')

    def __str__(self):
        return f"Image for {self.home.title}"



class Reservation(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)  # Links to Home model
    check_in_date = models.DateField()
    check_in_time = models.TimeField()
    check_out_date = models.DateField()
    check_out_time = models.TimeField()
    guests = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    additional_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.home.title} from {self.check_in_date} to {self.check_out_date}"


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email} says {self.message} Phone number is {self.phone_number}"

