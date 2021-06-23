from django.shortcuts import render,redirect
from memo.models import Memo

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
# Create your views here.
def home(request):
    # -key 내림차순
    memoList = Memo.objects.order_by('-idx')
    memoCount = Memo.objects.all().count()
    return render(
        request,
        'memo/list.html',
        {
            'memoList':memoList,
            'memoCount':memoCount,
        } 
    )


def insert_memo(request):
    memo = Memo(writer=request.POST['writer'], memo=request.POST['memo'])
    memo.save()
    return redirect('/memo')

def detail_memo(request):
    memo = request.GET['idx']
    row = Memo.objects.get(idx=memo)
    return render(request, 'memo/detail.html', {'row':row})


def update_memo(request):

    id = request.POST['idx'] 
    memo = Memo(idx=id, writer=request.POST['writer'], memo=request.POST['memo'])
    memo.save()
    return redirect('/memo')

def delete_memo(request):
    
    id = request.POST['idx'] 
    memo = Memo.objects.get(idx=id)
    memo.delete()
    return redirect('/memo')

