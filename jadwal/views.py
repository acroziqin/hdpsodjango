from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.core.files.storage import FileSystemStorage

class IndexView(TemplateView):
    template_name='jadwal/index.html'

class TentukanView(TemplateView):
    template_name='jadwal/tentukan.html'

class HasilView(TemplateView):
    template_name='jadwal/hasil.html'

    def get_context_data(self):
        hasil = [
            ('Senin', [
                ('101', [
                    ['Bahasa Arab', 2, 'Moh. Nadhif', 'PGMI', 'A'],
                    ['', 1, '', '', ''],
                    ['Takhrijul Hadits', 2, 'Damanhuri', 'PAI', 'A'],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', '']
                ]),
                ('102', [
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['IAD & ABD', 2, 'Misbahul Munir', 'PAI', 'A'],
                    ['', 1, '', '', '']
                ]),
                ('103', [
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['Pancasila', 2, 'Ali Rifan', 'PAI', 'A'],
                    ['Studi Al-Quran', 2, 'Mokhamat Nafi', 'MPI', 'A'],
                    ['', 1, '', '', '']
                ]),
                ('305', [
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['Bahasa Indonesia', 2, 'Handoko', 'MPI', 'A'],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', '']
                ]),
                ('306', [
                    ['Takhrijul Hadits', 2, 'Damanhuri', 'PAI', 'B'],
                    ['Ushul Fiqih', 2, 'Kasuwi Saiban', 'MPI', 'A'],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', '']
                ]),
            ]),
            ('Rabu', [
                ('101', [
                    ['', 1, '', '', ''],
                    ['Bahasa Indonesia', 2, 'Handoko', 'PAI', 'A'],
                    ['', 1, '', '', ''],
                    ['Bahasa Inggris', 2, 'Hilman Wajdi', 'PAI', 'A'],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', '']
                ]),
                ('102', [
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['Qowaidul Fiqih', 3, 'Zaenu Zuhdi', 'PAI', 'A'],
                    ['Bahasa Arab', 2, 'Moh. Nadhif', 'PAI', 'A']
                ]),
                ('304', [
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['Studi Al-Quran', 2, 'Mokhamat Nafi', 'PGMI', 'A'],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', '']
                ]),
                ('305', [
                    ['Ushul Fiqih', 2, 'Kasuwi Saiban', 'PAI', 'B'],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['IAD & IBD', 2, 'Misbahul Munir', 'PAI', 'B'],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', '']
                ]),
            ]),
            ('Jumat', [
                ('101', [
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['Pengantar Studi Islam', 2, 'Umi Salamah', 'PAI', 'B'],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', '']
                ]),
                ('102', [
                    ['', 1, '', '', ''],
                    ['Pengantar Studi Islam', 2, 'Umi Salamah', 'MPI', 'A'],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', '']
                ]),
                ('305', [
                    ['Bahasa Indonesia', 2, 'Handoko', 'PAI', 'B'],
                    ['', 1, '', '', ''],
                    ['Takhrijul Hadits', 2, 'Damanhuri', 'PAI', 'B'],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', '']
                ]),
                ('306', [
                    ['', 1, '', '', ''],
                    ['Ushul Fiqih', 2, 'Kasuwi Saiban', 'PAI', 'A'],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', ''],
                    ['', 1, '', '', '']
                ]),
            ]),
        ]

        context = {
            'hasil'  : hasil
        }

        return context

def importExcel(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['jadwal']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'jadwal/import_excel.html')