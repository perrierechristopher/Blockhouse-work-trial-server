from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework import status
from .serializer import DataSerializer
from .helpers import get_last_segment

mockedData = {
    'bar': {
        'labels': ["Product A", "Product B", "Product C"],
        'data': [100, 150, 200],
    },
    'line': {
                'labels': ["Jan", "Feb", "Mar", "Apr",],
        'data': [10, 20, 30, 40],
    },
    'pie':{
            'labels': ["Red", "Blue", "Yellow"],
        'data': [300, 50, 100],
        }
}

# Create your views here.
@api_view(['GET'])
def get_chart_data(request):
    lastSegment = get_last_segment(request.path)
    for key in mockedData:
        if key in lastSegment:
            return DataSerializer(mockedData[key])
    return DataSerializer({'labels': '', 'data': ''})
            
