import requests
from django.http.response import HttpResponse,JsonResponse
from django.views.decorators.cache import cache_page
# Create your views here.

@cache_page(60)
def testMockServer(request):
    response = requests.get('https://3ff88dfe-6ab2-4957-8df4-ee239e5e6886.mock.pstmn.io/test/delay/5')
    return JsonResponse(response.json())
@cache_page(20 * 60)
def GetWheatherData(request):
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=35.747142&lon=51.413209&appid=1402a199f4c50bab2131b141bfe318d9')
    return JsonResponse(response.json())