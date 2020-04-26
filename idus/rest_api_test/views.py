from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


class IndexView(View):
    
    def get(self, request):
        dummy_data = {
            'name': '죠르디',
            'type': '공룡',
            'job': '편의점알바생',
            'age': 5
        }
        return JsonResponse(dummy_data)
    @csrf_exempt
    def post(self, request):
        return HttpResponse("Post 요청을 잘받았다")
    @csrf_exempt
    def put(self, request):
        return HttpResponse("Put 요청을 잘받았다")
    @csrf_exempt
    def delete(self, request):
        return HttpResponse("Delete 요청을 잘받았다")