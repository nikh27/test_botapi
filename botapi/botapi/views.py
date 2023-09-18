
from django.http import HttpResponse,JsonResponse

def home_page(request):
    friends=['ankit','ravi','uttam','nikhil']
    return JsonResponse(friends,safe=False)