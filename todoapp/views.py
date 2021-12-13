from django.shortcuts import get_object_or_404, redirect, render

from todo.views import redirect_home

from .forms import todoForm
from .models import Todo
from django.contrib import messages
from django.views.generic.edit import CreateView


# Create your views here.
class todoListViewClass(CreateView):
    
    def post(self,request):
        form = todoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Todo is created.')
            return redirect('home')
        
    def get(self,request,*kwargs):
        todo_list = Todo.objects.all().order_by('date')
        form = todoForm()
    
        page = {
            'forms': form,
            'list': todo_list,
            'title': 'Todo List',
        }
        
        return render(request,'todoapp/todo.html',context = page)
    

# def todoListView(request):
#     todo_list = Todo.objects.order_by('date')
    
#     if request.method == 'POST':
#         form = todoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
        
#     form = todoForm()
    
#     page = {
#         'forms': form,
#         'list': todo_list,
#         'title': 'Todo List',
#     }
    
#     return render(request,'todoapp/todo.html',context = page)


def remove(request,item_id):
    try:
        item = get_object_or_404(Todo, id= item_id)
        item.delete()
        messages.success(request, 'Todo removed successfully.')
    # Todo.objects.get(id=item_id).delete()
    except:
        messages.error(request, 'Fail to remove Todo.')
    return redirect('home')