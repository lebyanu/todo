from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import todo_form
from . models import todomodel
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView,DeleteView

# Create your views here.
class todo_listview(ListView):
    model = todomodel
    template_name = 'home.html'
    context_object_name = 'task'
class todo_detailview(DeleteView):
    model = todomodel
    template_name = 'details.html'
    context_object_name = 'task'
class todo_upadateview(UpdateView):
    model = todomodel
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbdhome',kwargs={'pk':self.object.id})
class todo_delete(DeleteView):
    model = todomodel
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')








def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = int(request.POST.get('priority'))
        date = request.POST.get('date')
        tsk = todomodel(name=name, priority=priority, date=date)
        tsk.save()

    tasks = todomodel.objects.all()
    return render(request, 'home.html', {'task': tasks})



def delete(request, id):
    tsk = todomodel.objects.get(id=id)
    if request.method == 'POST':
        tsk.delete()
        return redirect('/')
    return render(request, 'delete.html')








def update(request, id):
    tsk = todomodel.objects.get(id=id)
    frm = todo_form(request.POST or None, instance=tsk)
    if frm.is_valid():
        frm.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': frm, 'task': tsk})





