from django.db import models

# Create your models here.
# django의 Model 클래스를 상속받은 클래스
# 클래스에 정의한 변수명과 자료형을 기반으로 데이터베이스에 테이블이 만들ㄹ어짐
class Address(models.Model):
    # 자동증가 필드, 기본키
    idx = models.AutoField(primary_key=True)
    # 최대사이즈, 빈값허용, null 허용
    name = models.CharField(max_length=50,blank=True, null=True)
    tel = models.CharField(max_length=50,blank=True, null=True)
    email = models.CharField(max_length=50,blank=True, null=True)
    address = models.CharField(max_length=500,blank=True, null=True)
    # 