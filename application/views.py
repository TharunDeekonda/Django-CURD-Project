from django.shortcuts import render,redirect
from .forms import *
from django.views.generic import *
from django.urls import reverse
# Create your views here.
def add_form(request):
    obj=Student.objects.all()
    form = Student_form()
    
    if request.method == 'POST':
        form = Student_form(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('Home')  
        
    
    return render(request, 'application/home.html', {'form': form,'obj':obj})

class Update_Form(UpdateView):
    model=Student
    fields='__all__'
    template_name='application/home.html'
    
    def get_success_url(self):
        return reverse('Home')
    
def delete_form(request,pk):
    obj=Student.objects.get(id=pk)
    obj.delete()
    return redirect('Home')
    