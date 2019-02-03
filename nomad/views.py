from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
import os

#장고 generic view를 불러오고, http response, 장고 base.py의 세팅을 불러옴
class ReactAppView(View):
    def get(self, request):
        try:
            with open(os.path.join(str(settings.ROOT_DIR), 'frontend', 'build', 'index.html')) as file:
                return HttpResponse(file.read())
        except:
            return HttpResponse(
                """
            index.html not found ! build your React app !!
            """,
                status=501,
            )