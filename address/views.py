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

# http://localhost/address/detail 회원상세화면 
def detail(request):
    # 쿼리스트링으로 전달된 변수(get 방식)
    id = request.GET['idx']
    # address 테이블의 레코드 중에서 idx 값으로 조회
    addr = Address.objects.get(idx = id)
    # detail.html로 넘어가서 출력됨
    return render(
        request, 
        'address/detail.html',
        {'addr':addr}
    )

def update(request):
    id = request.POST['idx'] #hidden으로 전달된 글번호
    # 수정할 내용을 편집
    addr = Address(
        idx = id,
        name = request.POST['name'],
        tel = request.POST['tel'],
        email = request.POST['email'],
        address = request.POST['address'],
    )
    addr.save()
    return redirect('/address')

def delete(request):
    id = request.POST['idx'] #hidden으로 전달된 글번호
    # 수정할 내용을 편집
    addr = Address.objects.get(idx = id)
    addr.delete()
    return redirect('/address')