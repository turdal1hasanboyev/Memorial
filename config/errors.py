from django.shortcuts import render

def custom_page_not_found_view(request, exception, *args, **kwargs):
    return render(request, '404.html', status=404)