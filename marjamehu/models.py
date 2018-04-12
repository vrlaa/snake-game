from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)

class CustomUserManager(BaseUserManager):

    #Create player or developer user and save it
    def create_user(self, username, developer, password=None):
    #def create_user(self, username, password=None):
        #Raise Error
        if not username:
            raise ValueError('Give a username to your account')

        user = self.model(
            username=username,
            developer=developer,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    # Create super user and save it
    def create_superuser(self, username, developer, password):
    #def create_superuser(self, username, password):

        user = self.create_user(
            username=username,
            developer=developer,
            password=password)

        user.admin = True
        user.save(using=self._db)
        return user

# Create your models here.
class CustomUser(AbstractBaseUser):
    username     = models.CharField(max_length=20, unique=True)
    developer    = models.BooleanField(default=False) # Developer account type
    admin        = models.BooleanField(default=False) # Superuser account type
    staff        = models.BooleanField(default=False) # Staff for admin site
    #email        = models.EmailField()

    objects = CustomUserManager()
    #objects = UserManager()

    USERNAME_FIELD = 'username'
    #Required fields
    #REQUIRED_FIELDS = ['developer']

    def __str__(self):
        return self.username

    # @property
    # def is_developer(self):
    #     return self.developer
    #
    # #@property
    # def is_admin(self):
    #     return self.admin
    #
    # #@property
    # def get_username(self):
    #     return self.username
    #
    # #@property
    # def is_staff(self):
    #     return self.staff
