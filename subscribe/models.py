from django.db import models

# Create your models here.



NEWSLETTER_OPTION = [
    ('W', 'Weekly'),
    ('M', 'Monthly')
    
    
]
class Subscribe(models.Model):
    first_name = models.CharField(max_length=200)
    last_name=  models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    option = models.CharField(max_length=2,choices=NEWSLETTER_OPTION, default='M')