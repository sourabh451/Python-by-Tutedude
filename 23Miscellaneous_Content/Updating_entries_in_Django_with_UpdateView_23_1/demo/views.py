from django.shortcuts import render
from django.views import generic
from .models import Student
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'demo/index.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        return Student.objects.all()

class StudentUpdate(generic.UpdateView):
    model = Student
    fields =['name']
    template_name = 'demo/student_update_form.html'
