from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from .models import Questions
from .forms import UserForm

# Create your views here.


def index(request):
    all_questions = Questions.objects.all()
    context = {'all_questions':all_questions}
    return render(request, 'music/index.html', context)
#
#   html= ''
#    for questions in all_questions:
#        url ='/music/'+ str(questions.id) + '/'
#        html +='<a href="' + url +'">' + questions.album_title + '</a><br>'
#    return HttpResponse(html)

def detail(request, question_id):
    #        questions= Questions.objects.get(pk=question_id)

    questions = get_object_or_404(Questions, pk=question_id)
    return render(request, 'music/detail.html', {'questions':questions})


class AlbumCreate(CreateView):
    model = Questions
    fields=['question_text', 'question_title', 'category']

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/index.html'
    
    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized data)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns user objects if credentials are correct

            user = authenticate(username= username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)

                    return redirect('music/index.html')

        return render(request, self.template_name, {'form':form})













