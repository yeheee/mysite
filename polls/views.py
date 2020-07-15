from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question

# Create your views here.
def index(request):
    q_list = Question.objects.order_by('pub_date')[:5]
    # str_list = [q.question_text for q in q_list]
    # html = ', '.join(str_list)
    # return HttpResponse(html)
    return render(request, 'polls/index.html', {'latest_question_list':q_list})
    
def detail(request, question_id): # 질문 상세 페이지
    # question = Question.objects.get(pk=question_id)
    question = Question.objects.get(id=question_id)
    return render(request, 'polls/detail.html', {'question':question})  
    # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id): # 투표 결과 페이지
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# 연습문제 2번 관련
def reset(request, question_id):
    question = Question.objects.get(id=question_id)
    choice_list = question.choice_set.all()
    for choice in choice_list:
        choice.votes = 0
        choice.save()
    return HttpResponse('ok')


def vote(request, question_id): # 투표 페이지
    # request.POST['choice'] - 이 방법 보다는 아래의 방법이 조금 더 부드러운 방법이다. 
    choice_id = request.POST.get('choice')
    # 질문 조회
    question = Question.objects.get(id=question_id)
    # 보기 조회
    choice = question.choice_set.get(id=choice_id)
    # 투표 수 증가
    choice.votes +=1
    # 저장
    choice.save()

    # return HttpResponse("You're voting on question %s." % question_id)
    # return HttpResponseRedirect('/polls/%s/' %question_id)  ==> 변수 출처 확인해보기
    return HttpResponseRedirect(reverse('detail', args=(question.id,)))  # ==> 변수 출처 확인해보기