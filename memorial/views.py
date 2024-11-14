from django.shortcuts import render, redirect, get_object_or_404
from .models import Banner, About, Book, SubEmail, Contact, Review, CustomUser
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home_page_view(request):
    search = request.POST.get('search')
    
    banner = Banner.objects.filter(is_active=True).order_by('id')[:3]
    about = About.objects.filter(is_active=True, id=1).first()
    books = Book.objects.filter(is_active=True).order_by('title')[:10]
    our_library = Book.objects.filter(is_active=True, is_available=True).order_by('-title')[:3]
    
    if search:
        books = books.filter(title__icontains=search)
        our_library = our_library.filter(title__icontains=search)
        
    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')
        
        SubEmail.objects.create(email=sub_email)
        
        return redirect('home')
    
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST.get('name')
        contact.phone_number = request.POST.get('phone_number')
        contact.email = request.POST.get('email')
        contact.message = request.POST.get('message')
        contact.save()
        
        return redirect('/')
    
    context = {
        'banners': banner,
        'about': about,
        'books': books,
        'our_library': our_library,
    }
    
    return render(request, 'index.html', context)

def about_page_view(request):
    # previous_url = request.META.get('HTTP_REFERER') # oldingi sahifani qaytarish
    # return redirect(request.path) # hozirgi sahifaga qaytarish
    # previous_url = request.META.get('HTTP_REFERER', request.path) oldingi sahifani qaytaradi agar u mavjud bolmasa hozirgi sahifani qaytaradi
    search = request.POST.get('search')
    
    about = About.objects.filter(is_active=True, id=1).first()
    
    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')
        sub_email = SubEmail.objects.create(email=sub_email)
        sub_email.save()
        
        return redirect(request.path)
    
    return render(request=request, template_name='about.html', context={'about': about})

def books_page_view(request):
    search = request.POST.get('search')
    
    books = Book.objects.filter(is_active=True).order_by('-title')
    
    if search:
        books = books.filter(title__icontains=search)
        
    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')
        
        SubEmail.objects.create(email=sub_email)
        
        return redirect('books')
    
    return render(request, 'books.html', context={'books': books[:6]})

def library_page_view(request):
    search = request.POST.get('search')
    
    our_library = Book.objects.filter(is_active=True, is_available=True).order_by('id')
    
    if search:
        our_library = our_library.filter(title__icontains=search)
        
    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')
        
        SubEmail.objects.create(email=sub_email)
        
        return redirect(request.path)
    
    return render(request, 'library.html', context={'our_library': our_library[:10]})

def book_detail_page_view(request, slug):
    search = request.POST.get('search')
    
    book = get_object_or_404(Book, is_active=True, slug__iexact=slug)
    reviews = Review.objects.filter(is_active=True, book_id=book.id).order_by('-id')
    
    context = {
        'book': book,
        'reviews': reviews,
    }
    
    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')
        
        SubEmail.objects.create(email=sub_email)
        
        return redirect('book-single', book.slug)
    
    if request.method == 'POST':
        rate = request.POST.get('rate')
        review = request.POST.get('review')
        bookshelve = request.POST.get('bookshelve')
        date_started = request.POST.get('date_started')
        date_ended = request.POST.get('date_ended')
        
        Review.objects.create(
            author_id=request.user.id,
            book_id=book.id,
            rate=rate,
            review=review,
            bookshelve=bookshelve,
            date_started=date_started,
            date_ended=date_ended,
            is_active=True,
        )
        
        return redirect('book-single', book.slug)
    
    return render(request, 'book-single.html', context=context)

def contact_page_view(request):
    search = request.POST.get('search')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        
        Contact.objects.create(
            name=name,
            phone_number=phone_number,
            email=email,
            message=message,
            subject=subject,
            is_active=True,
        )
        
        return redirect('contact')
    
    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')
        
        SubEmail.objects.create(email=sub_email)
        
        return redirect(request.path)
    
    return render(request, 'contact.html')

def register_page_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        confirm_password = request.POST.get('confirm_password')
        
        if password!= confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        else:
            user = CustomUser.objects.filter(email=email).first()
            
            if user:
                messages.error(request, "Email already exists.")
                return redirect('register')
            
        if not all([email, password, first_name, last_name, phone_number]):
            messages.error(request, "All fields are required.")
        else:
            user = CustomUser.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                is_active=True,
                is_staff=False,
                is_superuser=False,
            )
            user.save()
            login(request, user)
            return redirect('home')
            
    return render(request, 'register.html')

def login_page_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password.")
            
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Tizimdan muvaffaqiyatli chiqdingiz.")
    return redirect('home')