from django.shortcuts import get_object_or_404
from .models import Cars
from django.views import generic
from django.db.models import F
#from django.core.paginator import Paginator

class CarListView(generic.ListView):
    template_name = 'car_list.html'
    model = Cars
    context_object_name = 'car_key' 
    paginate_by = 2 

    def get_queryset(self):
        search_text = self.request.GET.get('search')
        if search_text:
            return self.model.objects.filter(name_car__icontains=search_text).order_by('-id')
        return self.model.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_value'] = self.request.GET.get('search')
        return context


class CarDetailView(generic.DetailView):
    template_name = 'car_detail.html'
    model = Cars
    context_object_name = 'car_id_key' 

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=car_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        
        viewed_cars = self.request.session.get('viewed_cars', [])
        if car.id not in viewed_cars:
            car.views = F('views') + 1
            car.save()
            car.refresh_from_db()
            
            viewed_cars.append(car.id)
            self.request.session['viewed_cars'] = viewed_cars
            
        return context






# def car_list_view(req):
#     search_text = req.GET.get('search')
    
#     if search_text:
#         car_list = Cars.objects.filter(name__icontains=search_text).order_by('-id')
#     else:
#         car_list = Cars.objects.all().order_by('-id')

#     paginator = Paginator(car_list, 2)
#     page_number = req.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     return render(
#         req,
#         'car_list.html',
#         {
#             "car_key": page_obj,  
#             "search_value": search_text, 
#         }
#     )

# def car_detail_view(req, id):
#     car_id = get_object_or_404(Cars, id=id)

   
#     viewed_cars = req.session.get('viewed_cars', [])
#     if id not in viewed_cars:
#         car_id.views = F('views') + 1
#         car_id.save()
#         car_id.refresh_from_db()
        
#         viewed_cars.append(id)
#         req.session['viewed_cars'] = viewed_cars

#     return render(
#         req,
#         'car_detail.html',
#         {
#             'car_id_key': car_id,
#         }
#     )










# def car_list_view(req):
#     if req.method == 'GET':
 
#         car = Cars.objects.all().order_by('-id')
#     return render(
#             req,
#             'car_list.html',
#             {
#                 "car_key": car,
#             }
#         )

# def car_detail_view(req, id):
#     if req.method == 'GET':
#         car_id = get_object_or_404(Cars, id=id)

#     return render(
#         req,
#         'car_detail.html',
#         {
#             'car_id_key': car_id,
#         }
#     )   

