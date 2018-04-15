from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)
from django.utils import timezone

#### USER MODELS ##############################################################

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
    module_perms = models.BooleanField(default=True)
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
    @property
    def is_staff(self):
        return self.staff

    @property
    def has_module_perms(self):
        return self.module_perms

##############################################################################

#### GAME MODELS #############################################################

# class Game(models.Model):
#     # Username has maximum of 20 characters
#     developer       = models.ForeignKey('marjamehu.CustomUser', on_delete=models.CASCADE)
#     # game_highscores = models.ForeignKey('marjamehu.HighScores', on_delete=models.CASCADE)
#     # game_saves      = models.ForeignKey('marjamehu.Saves', on_delete=models.CASCADE)

#     game_url        = models.CharField(max_length=255)
#     game_name       = models.CharField(max_length=100, unique=True)
#     game_price      = models.PositiveIntegerField()
#     published_date  = models.DateTimeField(default=timezone.now)

#     def publish(self):
#         self.published_date = timezone.now()

#     # Save user game to Saves model
#     # def save_game(self, username, game_info):
#         pass

#     # Save highscores to HighScores model
#     # def save_highscores(self, username, highscore):
#         pass

#     def __str__(self):
#         return self.game_name



# class HighScores(models.Model):
    #

# class Saves(models.Model):
