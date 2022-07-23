from decimal import Context
from django.shortcuts import get_object_or_404, render, HttpResponse, redirect, reverse
from dashboard.forms import ExamcalendarForm, ExammarkForm, HomeworkForm, ToDoForm, QuestionForm
from dashboard.models import Examcalendar, Exammarks, Homework, ToDo, Question, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,"index.html")

@login_required(login_url = "user:login")
def homeworks(request):
    if request.method == "POST":
        form = HomeworkForm(request.POST)
        if form.is_valid():
            homework = form.save(commit = False)
            homework.user = request.user
            homework.is_finished = False
            homework.save()
            return redirect("homeworks")

    homeworks = Homework.objects.filter(user = request.user)
    form = HomeworkForm()

    finishedNumber = 0
    notFinishedNumber = 0
    
    for i in homeworks:
        if i.is_finished == True:
            finishedNumber += 1
        else:
            notFinishedNumber += 1
    context = {
        'homeworks':homeworks,
        'finishedNumber':finishedNumber,
        'notFinishedNumber':notFinishedNumber,
        'form':form,
    }
    return render(request,"homeworks.html",context)

def update_homeworks(request,pk=None):
    homework = Homework.objects.get(id=pk)
    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True
    homework.save()
    return redirect('homeworks')

def delete_homeworks(request,pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect("homeworks")

@login_required(login_url = "user:login")
def exammarks(request):
    if request.method == "POST":
        form = ExammarkForm(request.POST)
        if form.is_valid():
            exammark = form.save(commit = False)
            exammark.user = request.user
            exammark.save()
            return redirect("exammarks")

    exammarks = Exammarks.objects.filter(user = request.user)
    form = ExammarkForm() 

    for i in exammarks:
        i.average = int(((i.firstExam*3)/10) + ((i.secondExam*3)/10) + ((i.final*4)/10))
        print(i.average)
        i.save()
    
    if len(exammarks) == 0:
        isthereexam = True
    else:
        isthereexam = False

    percent = 70

    context = {
        'exammarks':exammarks,
        'isthereexam' : isthereexam,
        'form':form,
        'percent':percent,
    }

    return render(request,"exammarks.html",context)

def update_exammarks(request,pk=None):
    exammark = get_object_or_404(Exammarks,id=pk)
    form = ExammarkForm(request.POST or None,instance = exammark)

    if form.is_valid():
        exammark = form.save(commit = False)
        exammark.user = request.user
        exammark.save()
        messages.success(request, "Not başarıyla güncellendi.")
        return redirect("exammarks")
    return render(request,"updateexammarks.html",{'form':form})


def delete_exammarks(request,pk=None):
    Exammarks.objects.get(id=pk).delete()
    return redirect("exammarks")

@login_required(login_url = "user:login")
def examcalendar(request):
    if request.method == "POST":
        form = ExamcalendarForm(request.POST)
        if form.is_valid():
            examdate = form.save(commit = False)
            examdate.user = request.user
            examdate.save()
            return redirect("examcalendar")    

    examdates = Examcalendar.objects.filter(user = request.user)
    form = ExamcalendarForm()

    finishedNumber = 0
    notFinishedNumber = 0
    
    for i in examdates:
        if i.is_finished == True:
            finishedNumber += 1
        else:
            notFinishedNumber += 1

    context = {
        'form':form,
        'examdates':examdates,
        'finishedNumber':finishedNumber,
        'notFinishedNumber':notFinishedNumber,
    }

    return render(request,"examcalendar.html",context)

def update_examcalendar(request,pk=None):
    exam = Examcalendar.objects.get(id=pk)
    if exam.is_finished == True:
        exam.is_finished = False
    else:
        exam.is_finished = True
    exam.save()
    return redirect('examcalendar')

def delete_examcalendar(request,pk=None):
    Examcalendar.objects.get(id=pk).delete()
    return redirect("examcalendar")

@login_required(login_url = "user:login")
def todolist(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid:
            todo = form.save(commit = False)
            todo.user = request.user
            todo.is_finished = False
            todo.save()
            return redirect("todolist")
    form = ToDoForm()
    todo = ToDo.objects.filter(user = request.user)

    finishedNumber = 0
    notFinishedNumber = 0
    
    for i in todo:
        if i.is_finished == True:
            finishedNumber += 1
        else:
            notFinishedNumber += 1

    if len(todo) == 0:
        todos_done = True
    else:
        todos_done = False

    context = {
        'form':form,
        'todos':todo,
        'todos_done':todos_done,
        'finishedNumber':finishedNumber,
        'notFinishedNumber':notFinishedNumber
    }
    return render(request,"todolist.html",context)

def update_todo(request,pk=None):
    todo = ToDo.objects.get(id=pk)
    if todo.is_finished == True:
        todo.is_finished = False
    else:
        todo.is_finished = True
    todo.save()
    return redirect('todolist')

def delete_todo(request,pk=None):
    ToDo.objects.get(id=pk).delete()
    return redirect("todolist")

@login_required(login_url = "user:login")
def timer(request):
    return render(request,"timer.html")

@login_required(login_url = "user:login")
def music(request):
    return render(request,"music.html")

def questions(request):
    keyword = request.GET.get("keyword")
    if keyword:
        questions = Question.objects.filter(title__contains = keyword)
        return render(request, "questions.html", {"questions" : questions})
    questions = Question.objects.filter()
    context = {
        "questions" : questions
    }
    return render(request, "questions.html", context)

@login_required(login_url = "user:login")
def askquestion(request):
    form = QuestionForm(request.POST)
    if form.is_valid():
        question = form.save(commit = False)
        question.author = request.user
        question.save()
        return redirect("questions")

    context = {
        "form" : form
    }
    return render(request, "askquestion.html", context)

def question_detail(request, id):
    question = get_object_or_404(Question, id = id)
    comments = question.comments.all()
    return render(request, "question_detail.html", {"question":question, "comments" : comments})

def question_delete(request, id):
    question = get_object_or_404(Question, id = id)
    question.delete()
    return redirect("questions")

def addComment(request, id):
    question = get_object_or_404(Question, id = id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author = comment_author, comment_content = comment_content)
        newComment.question = question
        newComment.save()
    return redirect(reverse("question_detail", kwargs = {"id":id}))
