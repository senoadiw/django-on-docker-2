from django.shortcuts import render
from django.core.files.storage import FileSystemStorage, default_storage
from django.conf import settings


def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        storage = FileSystemStorage()
        # use django-storages for production
        if settings.DEBUG == 0:
            storage = default_storage
        filename = storage.save(image_file.name, image_file)
        image_url = storage.url(filename)
        print(image_url)
        return render(request, "upload.html", {"image_url": image_url})
    return render(request, "upload.html")
