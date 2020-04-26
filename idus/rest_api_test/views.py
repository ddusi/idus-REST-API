from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Member
import json
from django.core.serializers import serialize

class IndexView(View):
    def get(self, request):
        data = Member.objects.all().order_by('-id')
        res = json.loads(serialize('json', data))
        return JsonResponse({
            'status' : 'OK',
            'message' : '요청에 성공 하셨습니다.',
            'result': res
                            
                        })

    def post(self, request):
        if request.META['CONTENT_TYPE'] == "application/json":
            request = json.loads(request.body)
            data = Member(name = request.POST['name'],
                            nick_name = request.POST['nick_name'],
                            user_id = request.POST['user_id'],
                            user_pw = request.POST['user_pw'],
                            phone = request.POST['phone'],
                            email = request.POST['email'],
                            gender = request.POST['gender'])
        else:
            data = Member(name = request.POST['name'],
                            nick_name = request.POST['nick_name'],
                            user_id = request.POST['user_id'],
                            user_pw = request.POST['user_pw'],
                            phone = request.POST['phone'],
                            email = request.POST['email'],
                            gender = request.POST['gender'])
        data.save()
        return HttpResponse(status=200)

    # def put(self, request):
    #     request = json.loads(request.body)
    #     id = request['id']
    #     phone = request['phone']
    #     data = get_object_or_404(Member, pk=id)
    #     data.phone = phone
    #     data.save()
    #     return HttpResponse(status=200)
    def put(self, request):
        if request.META['CONTENT_TYPE'] == "application/json":
            request = json.loads(request.body)
            id = request['id']
            phone = request['phone']
        else:
            id = request.PUT['id']
            phone = request.PUT['phone']
        data = get_object_or_404(Member, pk=id)
        data.phone = phone
        data.save()
        return HttpResponse(status=200)

    def delete(self, request):
        # data = Member.objects.get(pk=id)
        request = json.loads(request.body)
        id = request['id']
        data = get_object_or_404(Member, pk=id)
        data.delete()
        return HttpResponse(status=200)
    
    # def delete(self, request):
    # if request.META['CONTENT_TYPE'] == "application/json":
    #     request = json.loads(request.body)
    #     id = request['id']
    # else:
    #     id = request.PUT['id']
    #     data = get_object_or_404(Member, pk=id)
    #     data.delete()
    # return HttpResponse(status=200)