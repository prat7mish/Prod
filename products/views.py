from django.shortcuts import get_object_or_404, render,HttpResponseRedirect,reverse
from django.http import HttpResponse
from .models import Question,Choice

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'products/index.html', context)

def detail(request, id=None):
    question = get_object_or_404(Question, pk=id)
    return render(request, 'products/detail.html', {'question': question})

def results(request, id):
    question = get_object_or_404(Question, pk=id)
    return render(request, 'products/results.html', {'question': question})

def vote(request, id):
    question = get_object_or_404(Question, pk=id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'products/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('products:results', args=(question.id,)))