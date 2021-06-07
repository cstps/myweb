from django.shortcuts import render

# http://localhost => home 함수 호출
# request: 사용자가 입력한 내용, 요청사항을 저장하고 있는 변수

def home(request):
    # return render_to_response('index.html')
    # index.html 페이지로 넘어가서 출력됨
    msg = '안녕하세요'
    # render(request객체, url, 전달할 데이터(dict type))
    return render(request,'index.html',{'msg':msg})
