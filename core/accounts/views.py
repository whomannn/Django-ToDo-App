import requests
from django.http.response import HttpResponse,JsonResponse
from django.views.decorators.cache import cache_page
# Create your views here.

@cache_page(60)
def testMockServer(request):
    response = requests.get('https://3ff88dfe-6ab2-4957-8df4-ee239e5e6886.mock.pstmn.io/test/delay/5')
    return JsonResponse(response.json())