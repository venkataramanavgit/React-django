from django.http import JsonResponse

# Create your views here.
def home(request):
    return JsonResponse({'info':'venkat','id':'190030966'})