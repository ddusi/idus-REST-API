from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

def main (request):
    return render(request, 'member/main.html', {})

def signuppage (request):
    return render(request, 'member/signup.html', {})

def signup(request):
    if request.method == "POST":
        # 비번 확인
        if request.POST["user_pw"] == request.POST["user_pw2"]:
            #POST 처리 코드
            name = request.POST.get('name')
            nick_name = request.POST.get('nick_name')
            user_id = request.POST.get('user_id')
            user_pw = request.POST.get('user_pw')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            gender = request.POST.get('gender')
            

            #DB에 저장
            creat_user = member(
                name = name,
                nick_name = nick_name,
                user_id = user_id,
                user_pw = user_pw,
                phone = phone,
                email = email,
                gneder = gender,)
            creat_user.save()
            return redirect('/main')

        else:
            return render(request, 'member/sigup.html', {'error': 'username or password is incorrect'})
    
    return render(request, 'member/signup.html')