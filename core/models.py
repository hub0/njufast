from django.db import models
from django.contrib.auth.models import (
        AbstractBaseUser,
        BaseUserManager,
)
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """

        if not email:
            raise ValueError('Users must have an email address')
        
        #if not name:
        #    raise ValueError('Users must have a name')

        user = self.model(
                name=name,
                email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password=None):
        """
        Create and saves a superuser with the given email and password.
        """
        user = self.create_user(
                name, 
                email,
                password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# Create your models here.
class User(AbstractBaseUser):
    name = models.CharField(_('full name'), max_length=100, blank=False)
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_admin = models.BooleanField(_('admin'), default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return f'{self.name} {self.email}'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        return self.is_admin

