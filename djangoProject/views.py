from django.http import HttpResponse
from datetime import datetime
import os


def home_view(request):
    return HttpResponse(
        "<h1>Добро пожаловать!</h1>"
        "<ul>"
        "<li><a href='/current_time/'>Текущее время</a></li>"
        "<li><a href='/workdir/'>Содержимое рабочей директории</a></li>"
        "</ul>"
    )


def current_time_view(request):
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Текущее время: {formatted_time}")

def workdir_view(request):
    files = os.listdir('.')  # Получаем список файлов текущей директории
    file_list = "<br>".join(files)  # Преобразуем список в строку с переносами
    return HttpResponse(f"Содержимое рабочей директории:<br>{file_list}")




