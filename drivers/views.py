from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import DriverModel
from .forms import DriverForm


class DriverCreateView(generic.CreateView):
    template_name = 'create_driver.html'
    form_class = DriverForm
    success_url = reverse_lazy('drivers:driver_list') 


class DriverListView(generic.ListView):
    template_name = 'driver_list.html'
    model = DriverModel
    context_object_name = 'driver' 

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class DriverUpdateView(generic.UpdateView):
    template_name = 'update_driver.html'
    form_class = DriverForm
    model = DriverModel
    success_url = reverse_lazy('drivers:driver_list')

    def get_object(self, **kwargs):
        driver_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=driver_id)


class DriverDeleteView(generic.DeleteView):
    model = DriverModel
    success_url = reverse_lazy('drivers:driver_list')

    def get_object(self, **kwargs):
        driver_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=driver_id)

# def create_driver_view(request):
#     if request.method == "POST":
#         form = DriverForm(request.POST , request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/driver_list/')
#     else:
#         form = DriverForm()
    
#     return render(
#         request,
#         'create_driver.html',
#         {'form': form}
#     )

# def driver_list_view(request):
#     if request.method == 'GET':
#         driver = DriverModel.objects.all().order_by('-id')
#     return render(request , 'driver_list.html' , {'driver':driver})


# def update_driver_view(request,id):
#     driver_id = get_object_or_404(DriverModel, id=id)
#     if request.method == 'POST':
#         form = DriverForm(request.POST,request.FILES , instance=driver_id)
#         if form.is_valid():
#             form.save()
#             return redirect('/driver_list/')

#     else:
#         form = DriverForm(instance=driver_id)

#     return render(
#         request,
#         'update_driver.html',
#         {
#             'form':form ,
#             'driver_id':driver_id
#         }
#     )

# def delete_driver_view(request, id):
#     driver_id = get_object_or_404(DriverModel, id=id)
#     driver_id.delete()
#     return redirect('/driver_list/')