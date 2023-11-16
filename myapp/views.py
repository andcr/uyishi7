from django.shortcuts import render, redirect

from .models import models

def create_post(request):
    if request.method == 'POST':
        form = models(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # post_list - sizning postlar ro'yxati manzilingiz
    else:
        form = models()
    return render(request, 'create_post.html', {'form': form})