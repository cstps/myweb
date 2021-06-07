from django.shortcuts import render,redirect
from address.models import Address
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.
# http://localhost/address
def home(request):
    # address 테이블의 모든 레코드를 name 오름차순으로 저장 (-name 내림차순)
    items = Address.objects.order_by('idx')
    # address 테이블의 레코드 갯수를 저장
    address_count = Address.objects.all().count()
    # list.html로 이동(데이터도 같이 전달됨)
    return render(request, 'address/list.html', {'items':items,'address_count':address_count})
    

def write(request):
    return render(request, 'address/write.html')


# 크로스 사이트 스크립팅 공격을 방지하기 위한 코드
@csrf_exempt  
# request : 사용자가 입력한 내용들이 저장된 변수
def insert(request):
    # post 방식으로 전달된 값들을 Address 클래스에 저장
    addr = Address(name = request.POST['name'],
    tel = request.POST['tel'],
    email = request.POST['email'],
    address = request.POST['address']
    )
    # 레코드가 추가됨
    addr.save()
    # 리다이렉트 http://localhost/address 로 이동
    return redirect('/address')