from django.shortcuts import render
import random

def home(request):
    return render(request, 'mate/home.html')

def result(request):
    num = random.sample(range(1,47),6)
    member = ('송주연', '윤정인', '박도윤', '강윤서', '최진영', '유수화', '김도이', '전수현', '김세은', '이혜인', '박지연')
    friends = random.sample(member, 2)

    return render(request, 'mate/result.html',{'friends':friends})