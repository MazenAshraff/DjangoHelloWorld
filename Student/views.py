from django.shortcuts import render
from .form import StudentForm,RawStudentForm
# Create your views here.

from .models import Student


def student_detail_view(request):
    obj = Student.objects.get(id=1)
    context = {'name': obj.name,
               'gpa': obj.gpa,
               'student_id': obj.student_id,
               'age': obj.age}
    return render(request, 'Student/student_detail_view.html', context)

'''
def student_create_view(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = StudentForm()
    context = {'form':  form}
    return render(request, 'Student/student_create_view.html', context)
'''
def student_create_view(request):
    form = RawStudentForm()
    if request.method == 'POST':
        form = RawStudentForm(request.POST)
        if(form.is_valid()):
            print(form.cleaned_data)
            Student.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
   # form =RawStudentForm()
    context = {'form': form}
    return render(request, 'Student/student_create_view.html', context)

def dynamic_lookup_view(request, sid):
    obj = Student.objects.get(id=sid)
    context = {'obj': obj}
    return render(request, 'Student/student_detail_view.html', context)
