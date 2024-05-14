import json

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.utils import Translator

# Create your views here.
@csrf_exempt
@api_view(['POST',])
def endpoint_view(request):
    data = json.loads(request.body)['data']
    form_input = data['formInputValue']
    form_select = data['formSelectValue']
    instance = Translator(form_input)
    if form_select == 'early':
        instance.to_early_modern_english()
    elif form_select == 'modern':
        instance.to_current_modern_english()
    translate_dict = {'translate':instance.text}
    return Response(translate_dict)