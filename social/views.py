from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from upload.models import Form

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request,'로그인에 실패하였습니다.')
            return render(request, 'signin.html')

    #소셜로그인 성공할 시에 
    elif request.user.is_authenticated:
         return redirect('home')

    else:        
        return render(request, 'signin.html')

def kakao_login(request):
    app_rest_api_key = os.environ.get("KAKAO_REST_API_KEY")
    redirect_uri = main_domain + "users/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={'c867c4f396bb856e3bf6af90501d44f2'}&redirect_uri={'http://127.0.0.1:8000/accounts/kakao/login/callback/'}&response_type=code"
    )