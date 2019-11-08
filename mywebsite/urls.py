from django.contrib import admin
from django.urls import path
from jadwal.views import IndexView, TentukanView, ImportExcelView, HasilView

urlpatterns = [
    path('hasil', HasilView.as_view(template_name='jadwal/hasil.html')),
    path('import_excel', ImportExcelView.as_view(template_name='jadwal/import_excel.html')),
    path('tentukan', TentukanView.as_view(template_name='jadwal/tentukan.html')),
    path('', IndexView.as_view(template_name='jadwal/index.html')),
    path('admin/', admin.site.urls),
]
