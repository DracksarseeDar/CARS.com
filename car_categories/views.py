from django.shortcuts import render, get_object_or_404
from car_categories.models import Cars

def car_list_view(req):
    if req.method == 'GET':
 
        car = Cars.objects.all().order_by('-id')
    return render(
            req,
            'car_list.html',
            {
                "car_key": car,
            }
        )

def car_detail_view(req, id):
    if req.method == 'GET':
        car_id = get_object_or_404(Cars, id=id)

    return render(
        req,
        'car_detail.html',
        {
            'car_id_key': car_id,
        }
    )   

