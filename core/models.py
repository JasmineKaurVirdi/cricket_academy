from django.db import models

# Coach Model
class Coach(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    image = models.ImageField(upload_to='coaches/')

    def __str__(self):
        return self.name

# Program Model
class Program(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='programs/')

    def __str__(self):
        return self.title

# Gallery Image Model
class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title

# Contact Message Model
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Admission Model
class Admission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    address = models.TextField()
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Student Fee Model
class StudentFee(models.Model):
    student = models.ForeignKey(Admission, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Pending', 'Pending')])
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.status}"
