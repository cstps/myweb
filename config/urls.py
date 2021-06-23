"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from config import views
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    # http://localhost/admin/ => 관리자 페이지로
    path('admin/', admin.site.urls),
    # http://localhost => views.py의 home 함수 호출
    path('',views.home),
    # address/urls.py 를 포함시킴
    path('address/',include('address.urls')),
    path('memo/',include('memo.urls')),

    # survey/urls.py
    path('survey/',include('survey.urls')),
    
    path('guestbook/',include('guestbook.urls')),

    path('member/',include('member.urls')),
]

if settings.DEBUG: #디버그 모드일 경우
    import debug_toolbar
    # 디버그를 위한 url pattern 추가
    urlpatterns +=[
        # r 정규표현식 시작표시, 
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]