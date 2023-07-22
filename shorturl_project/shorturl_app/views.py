from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ShortURLForm
from .models import ShortURL
from django.conf import settings

def create_short_url(request):
    if request.method == 'POST':
        form = ShortURLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']

            # Check if the long URL already exists in the database
            try:
                short_url = ShortURL.objects.get(original_url=original_url)
                full_short_url = f"{settings.BASE_URL}/{short_url.short_id}/"
                return HttpResponse(f"Short URL Already Exists: {full_short_url}")
            except ShortURL.DoesNotExist:
                # If the long URL doesn't exist, create a new short URL
                short_url = ShortURL(original_url=original_url)
                short_url.save()

            # Construct the full short URL using the server's address and the short ID
            full_short_url = f"{settings.BASE_URL}/{short_url.short_id}/"
            return HttpResponse(f"Short URL Created: {full_short_url}")
    else:
        form = ShortURLForm()
    return render(request, 'shorturl/create_shorturl.html', {'form': form})

def redirect_to_original(request, short_id):
    try:
        short_url = ShortURL.objects.get(short_id=short_id)
        return redirect(short_url.original_url)
    except ShortURL.DoesNotExist:
        return render(request, 'shorturl/not_found.html')
