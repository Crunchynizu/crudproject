from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_details.html', {'student': student})

def student_list(request):
    students = Student.objects.all()  # Fetch all student records
    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to student list after saving
    else:
        form = StudentForm()
    
    return render(request, 'student_form_add.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()  # Delete student from database
        return redirect('student_list')
    
    return render(request, 'student_confirm_delete.html', {'student': student})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save() # Updates the student's data
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'student_form_edit.html', {'form': form, 'student': student})