from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from ckeditor.fields import RichTextField
import re
from datetime import date
from django.utils.text import slugify
from django.urls import reverse
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        verbose_name = 'Asosiy Model'
        verbose_name_plural = 'Asosiy Modellar'
        
        
class CustomUserManager(UserManager):
    def create_user(self, email, phone_number, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('Email address must be provided.')
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise ValueError('Invalid email address format.')
        if not phone_number:
            raise ValueError('Phone number must be provided.')
        if not re.match(r'^\+?[0-9]{1,15}$', phone_number):
            raise ValueError('Invalid phone number format.')
        if not first_name:
            raise ValueError('First name must be provided.')
        if not last_name:
            raise ValueError('Last name must be provided.')
        if not password:
            raise ValueError("Password must be provided.")
        
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, phone_number, first_name, last_name, password=None, **extra_fields):
        extra_fields.update({'is_staff': True, 'is_superuser': True})
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if not email:
            raise ValueError('Email address must be provided.')
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise ValueError('Invalid email address format.')
        if not phone_number:
            raise ValueError('Phone number must be provided.')
        if not re.match(r'^\+?[0-9]{1,15}$', phone_number):
            raise ValueError('Invalid phone number format.')
        if not first_name:
            raise ValueError('First name must be provided.')
        if not last_name:
            raise ValueError('Last name must be provided.')
        if not password:
            raise ValueError("Password must be provided.")
        
        user = self.create_user(email=email, phone_number=phone_number, first_name=first_name, last_name=last_name, password=password, **extra_fields)
        return user
    

class CustomUser(AbstractUser, BaseModel):
    GENDER = (
        ('Ayol', ('Ayol')),
        ('Erkak', ('Erkak')),
    )
    username = None
    email = models.EmailField(unique=True)
    description = RichTextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='profile_images/', default='images/user-default-image.png')
    video = models.FileField(blank=True, null=True, upload_to='profile_videos/')
    gender = models.CharField(max_length=10, choices=GENDER, default=None, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    adress = models.CharField(max_length=250, null=True, blank=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'phone_number',
        ]
    
    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'
        
    def __str__(self):
        if self.get_full_name():
            return f"{self.get_full_name()}"
        return f"{self.email}"
    
    def age(self):
        if not isinstance(self.birthday, date):
            return None
        today = date.today()
        age = today.year - self.birthday.year
        if (today.month, today.day) < (self.birthday.month, self.birthday.day):
            age -= 1
        return age
    
    
class SubEmail(BaseModel):
    email = models.EmailField(unique=True, max_length=55, db_index=True)
    
    def __str__(self):
        return f"{self.email}"
    
    class Meta:
        verbose_name = 'Sub Email'
        verbose_name_plural = 'Sub Emaillar'
    
    
class Contact(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    message = RichTextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Biz bilan aloqa'
        verbose_name_plural = "Biz bilan aloqa"
        
        
class Genre(BaseModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Janr'
        verbose_name_plural = "Janrlar"
    
    
class Category(BaseModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, db_index=True)
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalər"
    
    
class Tag(BaseModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Hashtag"
        verbose_name_plural = "Hashtaglar"


class Award(BaseModel):
    name = models.CharField(max_length=250, db_index=True, unique=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Yutuq'
        verbose_name_plural = "Yutuqlar"
        
class Book(BaseModel):
    LANGUAGE = (
        ('English', ('English')),
        ("Russian", ("Russian")),
        ("Turkish", ("Turkish")),
        ("Uzbek", ("Uzbek")),
    )
    title = models.CharField(max_length=250, unique=True, db_index=True)
    sub_title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True, db_index=True, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="book_author")
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True)  # ISBN-13 standard
    page_count = models.IntegerField(default=0)
    cover_image = models.ImageField(upload_to='book_cover_images/', default='images/default-image.jpg', blank=True, null=True)
    cover_video = models.FileField(upload_to='book_cover_videos/', blank=True, null=True)
    is_available = models.BooleanField(default=False)
    language = models.CharField(max_length=15, choices=LANGUAGE, default=("Uzbek", ("Uzbek")))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="book_category")
    tags = models.ManyToManyField(Tag, blank=True)
    awards = models.ManyToManyField(Award, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.title} {self.sub_title}"
    
    class Meta:
        verbose_name = 'Kitob'
        verbose_name_plural = "Kitoblar"
        
    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = f"{slugify(self.title)}-{uuid.uuid4()}"
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self, *args, **kwargs):
        return reverse("book-single", kwargs={"slug": self.slug})
    
    
class Review(BaseModel):
    STATUS = (
        ('read', ("read")),
        ('currently-reading', ("currently-reading")),
        ('to-read', ("to-read")),
    )
    author = models.ForeignKey(
        "memorial.CustomUser",
        on_delete=models.SET_NULL,
        null=True,
        related_name="reviews",
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_reviews")
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    review = RichTextField(null=True, blank=True)
    bookshelve = models.CharField(default=None, choices=STATUS, max_length=50)
    date_started = models.DateField(null=True, blank=True)
    date_ended = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.author.get_full_name()}-{self.book}"
    
    class Meta:
        verbose_name = 'Izoh'
        verbose_name_plural = "Izohlar"


class MyBook(BaseModel):
    user = models.ForeignKey("memorial.CustomUser", on_delete=models.CASCADE, related_name="my_books")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="favorites")
    date_read = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.book}"
    
    class Meta:
        verbose_name = 'Mening Kitobim'
        verbose_name_plural = "Mening Kitoblarim"
        
        
class About(BaseModel):
    title = models.CharField(max_length=250, db_index=True)
    description = RichTextField()
    image = models.ImageField(upload_to='about_images/', default='images/default-image.jpg')
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'Haqqimda'
        verbose_name_plural = "Haqqimda"
        
        
class Banner(BaseModel):
    title = models.CharField(max_length=250, db_index=True)
    description = models.TextField()
    image = models.ImageField(upload_to='banner_images/', default='images/default-image.jpg')
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = "Bannerlar"