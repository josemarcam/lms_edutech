from django.db import models
from django.contrib.auth.models import AbstractUser


class customUser(AbstractUser):
    USER_LEVEL = (
        (1,"administrator"), 
        (2,"professor"), 
        (3,"studant")
    )
    
    user_level = models.CharField(max_length=9,
                  choices=USER_LEVEL,
                  default=1)