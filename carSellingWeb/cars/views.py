from django.shortcuts import render
from .models import cars
from .forms import CarForm
from django.shortcuts import get_object_or_404,redirect
# Create your views here.
def index(request):
    return render(request,'index.html')

# def car_list(request):
#     cars_list= cars.objects.all().order_by('-created_at')
#     return render(request,'cars_list.html',{'cars':cars_list})

def car_list(request):
    cars_list = cars.objects.all().order_by('-created_at')
    print(f"Number of cars: {len(cars_list)}")  # Check if cars_list is empty
    for car in cars_list:
        print(f"Car ID: {car.id}, Car Name: {car.car_name}, Image URL: {car.photo.url}")

    return render(request, 'cars_list.html', {'cars': cars_list})

def car_create(request):
    if request.method == "POST":
        form=CarForm(request.POST , request.FILES)
        if form.is_valid():
            car=form.save(commit=False)
            car.user=request.user
            car.save()
            return redirect('car_list')
    else:
        form=CarForm()
    return render(request,'car_form.html',{'form':form})

def car_edit(request,car_id):
    car=get_object_or_404(cars,pk=car_id,user=request.user)
    if request.method == 'POST':
        form= CarForm(request.POST, request.FILES,instance=car)
        if form.is_valid():
            car=form.save(commit=False)
            car.user =request.user
            car.save()
            return redirect('car_list')
    else:
        form= CarForm(instance=car)
    return render(request,'car_form.html',{'form':form})

def car_delete(request,car_id):
    car= get_object_or_404(cars,pk=car_id,user= request.user)
    if request.method == "POST":
        car.delete()
        return redirect('car_list')
    return render(request,'car_confirm_delete.html',{'car':car})