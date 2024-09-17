from django.http import JsonResponse

def DataSerializer(data = {}):
    return JsonResponse(data)