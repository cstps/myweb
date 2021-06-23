from django.shortcuts import render,redirect
from guestbook.models  import Guestbook
from django.db.models import Q
# Create your views here.

def list(request):

    try:
        searchkey = request.POST['searchkey']
    except :
        searchkey = 'name'
    try:
        search = request.POST['search']
    except :
        search = ''
    try:
        msg =request.GET['msg']
    except:
        msg=""
    # gbList = Guestbook.objects.order_by('-idx')
    if searchkey =="name_content":
        gbList = Guestbook.objects.filter(Q(name__contains=search) | Q(content__contains=search)).order_by('-idx')
    elif searchkey == "name":
        gbList= Guestbook.objects.filter(Q(name__contains=search)).order_by('-idx')
    elif searchkey == "content":
        gbList= Guestbook.objects.filter(Q(content__contains=search)).order_by('-idx')
    
    # gbCount = Guestbook.objects.count()

    if searchkey =="name_content":
        gbCount = Guestbook.objects.filter(Q(name__contains=search) | Q(content__contains=search)).count()
    elif searchkey == "name":
        gbCount= Guestbook.objects.filter(Q(name__contains=search)).count()
    elif searchkey == "content":
        gbCount= Guestbook.objects.filter(Q(content__contains=search)).count()

    return render(
        request, 
        'guestbook/list.html', 
        {'gbList':gbList, 'gbCount':gbCount, 'msg':msg , 'searchkey':searchkey, 'search':search},
    )
    
def write(request):

    return render(request,'guestbook/write.html')
    
def gb_insert(request):
    row = Guestbook(
        name = request.POST['name'],
        email = request.POST['email'],
        passwd = request.POST['passwd'],
        content = request.POST['content']
    )
    row.save()
    return redirect('/guestbook/')
    
def passwd_check(request):
    id = request.POST['idx'] 
    pwd = request.POST['passwd']
    row = Guestbook.objects.get(idx=id)
    if row.passwd == pwd:
        return render(request, 'guestbook/edit.html',{'row':row})
    else:
        return redirect('/guestbook/?msg=error')

def gb_detail(request):
    pass

def gb_update(request):
    id = request.POST['idx']
    row = Guestbook(
        idx=id,
        name = request.POST['name'],
        email = request.POST['email'],
        content = request.POST['content'],
        )
    row.save()
    return redirect('/guestbook')

def gb_delete(request):
    id = request.POST['idx']
    row = Guestbook(idx = id)
    # Guestbook.objects.get(idx=id).delete()
    row.delete()
    return redirect('/guestbook')

