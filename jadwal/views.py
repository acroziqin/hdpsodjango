from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.core.files.storage import FileSystemStorage

class IndexView(TemplateView):
    template_name='jadwal/index.html'

class TentukanView(TemplateView):
    template_name='jadwal/tentukan.html'

class HasilView(TemplateView):
    template_name='jadwal/hasil.html'

def importExcel(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['jadwal']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'jadwal/import_excel.html')