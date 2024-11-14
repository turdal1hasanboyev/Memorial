from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, SubEmail, Contact, Genre, Category, Tag, Award, Book, Review, MyBook, Banner, About


admin.site.site_header = "Memorial Admin Paneli"
admin.site.site_title = "Memorial Admin Paneli"
admin.site.index_title = "Memorial Boshqaruv Paneliga Xush Kelibsiz!"


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    ordering = ('-id',)
    list_display = (
        'id',
        'get_full_name',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'gender',
        'image',
        'video',
        'birthday',
        'age',
        'is_staff',
        'is_superuser',
        'is_active',
        'last_login',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'gender',
        'is_active',
        'is_staff',
        'is_superuser',
        'birthday',
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'gender',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
        'age',
        'last_login',
        "date_joined",
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'phone_number', 'gender', 'description', 'note', 'image', 'video', 'adress',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser',)
        }),
        ('Important Dates', {
        'fields': ('created_at', 'updated_at', "date_joined", 'last_login', 'birthday', 'age',)
        }),
    )
    add_fieldsets = (
        ('Create Super User', {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'phone_number', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser',)}
        ),
    )
    
    
@admin.register(SubEmail)
class SubEmailAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'email',
        'is_active',
        'created_at',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    list_filter = ('is_active',)
    search_fields = ('email',)
    
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'name',
        'email',
        'phone_number',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'name',
        'email',
        'phone_number',
    )
    list_filter = ('is_active',)
    
    
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    list_display = ('id', 'name', 'is_active', 'created_at', 'updated_at',)
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    list_filter = ('is_active',)
    search_fields = ('name',)
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ('-name',)
    list_display = ('id', 'name', 'is_active', 'created_at', 'updated_at',)
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    list_filter = ('is_active',)
    search_fields = ('name',)
    prepopulated_fields = {
        'slug': ('name',),
    }
    
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    list_display = ('id', 'name', 'is_active', 'created_at', 'updated_at',)
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    list_filter = ('is_active',)
    search_fields = ('name',)
    
    
@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('id', 'name', 'date', 'is_active', 'created_at', 'updated_at',)
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    list_filter = ('is_active', 'date',)
    search_fields = ('name',)
    
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'title',
        'sub_title',
        'author',
        'published_date',
        'isbn',
        'page_count',
        'cover_image',
        'cover_video',
        'is_available',
        'language',
        'category',
        'views',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = ('is_active', 'is_available', 'language', 'category', 'author', 'published_date',)
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'title',
        'sub_title',
        'author__first_name',
        'author__last_name',
        'isbn',
        'language',
        'category__name',
    )
    prepopulated_fields = {
        'slug': ('title',),
    }
    
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    list_display = (
        'id',
        'author',
        'book',
        'rate',
        'review',
        'bookshelve',
        'date_started',
        'date_ended',
        'is_active',
        'created_at',
        'updated_at',
        )
    search_fields = (
        'author__first_name',
        'author__last_name',
        'book__title',
        'rate',
        'bookshelve',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'author',
        'book',
        'rate',
        'bookshelve',
        'date_started',
        'date_ended',
    )
    
    
@admin.register(MyBook)
class MyBookAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'user',
        'book',
        'date_read',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'user',
        'book',
        'date_read',
        'is_active',
    )
    search_fields = (
        'user__first_name',
        'user__last_name',
        'book__title',
    )
    
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'title',
        'image',
        'is_active',
        'created_at',
        'updated_at',
        )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    search_fields = ('title',)
    list_filter = ('is_active',)
    
    
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    ordering = ('-id',)
    list_display = (
        'id',
        'title',
        'image',
        'is_active',
        'created_at',
        'updated_at',
        )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    search_fields = ('title',)
    list_filter = ('is_active',)