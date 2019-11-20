from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from jadwal.views import IndexView, TentukanView, HasilView, importExcel
from jadwal.hdpso import HDPSO

urlpatterns = [
    path('hdpso', HDPSO.as_view(), name='hdpso'),
    path('hasil', HasilView.as_view(), name='hasil'),
    # path('import_excel', ImportExcelView.as_view(), name='import_excel'),
    path('import_excel', importExcel, name='import_excel'),
    path('tentukan', TentukanView.as_view(), name='tentukan'),
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)