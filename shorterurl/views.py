# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import URLs
import hashlib
from .forms import PostForm


def home(request):
    form = PostForm()
    return render(request, 'shorter/index.html', {'form': form})


def shorter(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('targetURL', None)
            hash_object = hashlib.md5(url)
            shorted_url = hash_object.hexdigest()[:15]

            try:
                URLs.objects.get(shortedURL=shorted_url)
            except URLs.DoesNotExist:
                entry = URLs(shortedURL=shorted_url, targetURL=url)
                entry.save()

            return render(request, 'shorter/index.html', {'shortedURL': shorted_url})
        else:
            return render(request, 'shorter/index.html', {'error_message':  "The url is not valid"})


def retrieve(request, input_url):

    target = get_object_or_404(URLs, shortedURL=input_url)

    target_url = target.targetURL

    if target_url[:4] != 'http':
        target_url = 'http://{}'.format(target_url)

    return redirect(target_url)
