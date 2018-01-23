from django.shortcuts import render
from .models import DownloadableFile
# Create your views here.


def list(request):
    """Shows list of all Downloadablefile's objects"""
    file_list = DownloadableFile.objects.all()
    context = { 'file_list': file_list }
    return render(request, "downloads/list.html", context)
