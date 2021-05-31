from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

def mobile_max_len(phone):
    #print(f'============={phone}=======')
    if not (type(phone) == int and len(str(phone)) == 10):    
        raise ValidationError('%(phone)s must be 10 digits and must be a number only', 
                params={'phone': phone},)
# Create your models here.
class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        unique=True,
        max_length=254,
    )
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    mobile = models.IntegerField(unique=True, validators=[mobile_max_len],
            default = 1234567890)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)