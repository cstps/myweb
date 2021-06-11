from django.db import models

# Create your models here.
# 설문 문항 
class Survey(models.Model):
    survey_idx = models.AutoField(primary_key=True)
    question = models.TextField(null=False)
    