from django.http import JsonResponse

# Create your views here.
def api(request):
    html = [
        {
            'motor' : 'supra'
        }
    ]
    return JsonResponse({'html':html})
    