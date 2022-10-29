from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class UserAccountManager(BaseUserManager):

    def _create_user(self, email, first_name, last_name, is_staff, is_superuser, account_type, phone, address, password=None,
                     **extra_fields):
        if not email:
            raise ValueError('Email is mandatory')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            account_type=account_type,
            phone=phone,
            address=address,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, account_type, phone, address, **extra_fields):
        return self._createg_user(email, first_name, last_name, False, False, account_type, phone, address, **extra_fields)

    def create_superuser(self, email, first_name, last_name, account_type, phone, address, **extra_fields):
        user = self._create_user(email, first_name, last_name, True, True, account_type, phone, address, **extra_fields)
        return user


class AccountType(models.Model):
    account_type = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.account_type


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=256, unique=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.CharField(max_length=8, blank=True)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    address = models.TextField()
    profile_picture = models.ImageField(default="images/default.png", upload_to="images/")

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'account_type', 'phone', 'address']

    objects = UserAccountManager()

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    def get_abstract_url(self):
        return '/users/%i/' % self.pk
