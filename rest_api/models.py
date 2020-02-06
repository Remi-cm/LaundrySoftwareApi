from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_client(self, email, name, sex, address, gpsLat, gpsLng, avatarUrl, phone, country, town, is_client, password=None):
        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, sex=sex, address=address, gpsLat=gpsLat, gpsLng = gpsLng, avatarUrl=avatarUrl, is_client=is_client, phone=phone, country=country, town=town)
        user.is_client = True
        user.staff = False
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_agency(self, name, email, phone, cni_number, address, gpsLat, gpsLng, avatarUrl, country, town, is_client, password):
        if name is None:
            raise TypeError('User must have a name')
        user = self.model(name=name,
                         email=self.normalize_email(email),
                         phone=phone,
                         cni_number=cni_number,
                         address=address,
                         gpsLat=gpsLat,
                         gpsLng = gpsLng, 
                         avatarUrl=avatarUrl, 
                         country=country, 
                         town=town,
                         is_client=is_client
                        )
        user.staff = True
        user.is_client = False
        user.set_password(password)
        user.save()
        
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.staff = True

        user.save(using=self._db)

        return user
    

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a UserProfile inside this system"""

    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    gpsLat = models.FloatField(blank=True, null=True)
    gpsLng = models.FloatField(blank=True, null=True)
    avatarUrl = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    town = models.CharField(max_length=30, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    cni_number = models.CharField(max_length=100, blank=True, null=True, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    is_client = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    def has_perm(self, perm, obj=None):
            return True

    def has_module_perms(self, app_label):
        return True

    def token(self):
        return self._generate_jwt_token()

    def is_staff(self):
        return self.staff

    def is_active(self):
        return self.active

    def _generate_jwt_token(self):
        token = Token.objects.get_or_create(user=self)
        return token



class Shipper(models.Model):
    agent = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    cni_number = models.CharField(max_length=100, unique=True, blank=True, null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Laundry(models.Model):
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE, blank=True, default=4)
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, default=8)
    agency = models.IntegerField(blank=True, default=2)
    description = models.TextField(default="No description")
    time_submitted = models.DateTimeField(auto_now_add=True)
    time_expected = models.DateTimeField(blank=True, null=True)
    imgUrl = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    onDelivery = models.BooleanField(default=False)
    price_estimated = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)
    
    def __str__(self):
        return self.description


class Clothe(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=0)
    
    def __str__(self):
        return self.name

class OrderLine(models.Model):
    laundry = models.ForeignKey(Laundry, on_delete=models.CASCADE)
    clothe = models.ForeignKey(Clothe, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, default="No description")
    price = models.DecimalField(max_digits=6, decimal_places=0)
    color = models.CharField(max_length=20,default="Not specified")
    quantity = models.IntegerField(default=1)
    laundry_key = models.IntegerField(default=0)

    def __str__(self):
        return self.clothe.name

class Order(models.Model):
    laundry = models.ForeignKey(Laundry, on_delete=models.CASCADE)
    reference = models.CharField(max_length=60)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=9, decimal_places=0)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return self.reference
   