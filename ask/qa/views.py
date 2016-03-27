from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.http import require_GET
from qa.forms import AskForm, AnswerForm
from qa.models import Question


def test(request, *args, **kwargs):
    resp = 'OK'
    for par in args:
        resp = resp + ', ' + par
    return HttpResponse(resp)


def question(request, q_id):
    q = get_object_or_404(Question, id=q_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        form.question = q.id
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(q.get_url())
    else:
        form = AnswerForm(initial={'question': q.id})
    return render(request, 'qa/question.html',
                  {'question': q,
                   'answers': q.answer_set.all(),
                   'answer': form})


@require_GET
def index(request, *args, **kwargs):
    questions = Question.objects.all()
    questions = questions.order_by('-added_at')
    return pagination(request, questions, '/?page=')


@require_GET
def popular(request, *args, **kwargs):
    questions = Question.objects.all()
    questions = questions.order_by('-rating')
    return pagination(request, questions, '/popular/?page=')


def ask(request, *args, **kwargs):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(form.save().get_url())
    else:
        form = AskForm()
    return render(request, 'qa/ask.html',
                  {
                      'form': form
                  })


# TODO: move this helper function somewhere
def pagination(request, questions, url):
    num = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)
    paginator = Paginator(questions, limit)
    if len(paginator.page_range) < int(num) or int(num) < 1:
        raise Http404()
    paginator.baseurl = url
    page = paginator.page(num)
    return render(request, 'qa/page.html',
                  {'posts': page.object_list,
                   'paginator': paginator,
                   'page': page,
                   'question_url': '/question/'})