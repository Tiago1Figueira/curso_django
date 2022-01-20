from django.http import HttpResponse

# Create your views here.

# HTML simples somente para abrir o django debug toolbar


def home(request):
    return HttpResponse('<html><body>Olá Django!</body></html>', content_type='text/html')
