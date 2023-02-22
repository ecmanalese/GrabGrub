from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Food, Customer, Order
from django.contrib import messages

# Create your views here.
def login(request):
    if(request.method=="POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username, password=password).exists() == True:
            return redirect('view_orders')
        else:
            messages.error(request, 'Invalid username/password')
    return render(request, 'Kiosk/login.html')

def signup(request):
    if(request.method=="POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "" or password == "":
            messages.error(request, 'Invalid credentials')
        else:
            if User.objects.filter(username=username).exists() == True:
                messages.error(request, 'Account already exists.')
            else:
                User.objects.create(username=username, password=password)
                messages.success(request, 'Account successfully created.')
                return redirect('login')
    
    return render(request, 'Kiosk/signup.html')

def view_orders(request):
    order_objects = Order.objects.all()
    return render(request, 'Kiosk/orders.html', {'order':order_objects})

def view_order_details(request, pk):
	o = get_object_or_404(Order, pk=pk)
	return render(request, 'Kiosk/order_details.html', {'o': o})

def update_order(request, pk):
    o = get_object_or_404(Order, pk=pk)
    if(request.method=="POST"):
        qty = request.POST.get('qty')
        payment_mode = request.POST.get('payment_mode')

        Order.objects.filter(pk=pk).update(qty=qty, payment_mode=payment_mode)
        messages.success(request, "Details were updated.")

        #Reflects the update immediately
        o = get_object_or_404(Order, pk=pk)
        
        return redirect('view_order_details', pk=pk)
    else:
        return render(request, 'Kiosk/update_order.html', {'o':o})

def delete_order(request, pk):
    Order.objects.filter(pk=pk).delete()
    messages.success(request, "Order deleted successfully.")
    return redirect('view_orders')

def view_food(request):
    food_objects = Food.objects.all()
    return render(request, 'Kiosk/foodlist.html', {'food':food_objects})

def view_food_details(request, pk):
	f = get_object_or_404(Food, pk=pk)
	return render(request, 'Kiosk/food_details.html', {'f': f})

def update_food(request, pk):
    f = get_object_or_404(Food, pk=pk)
    if(request.method=="POST"):
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        created_at = request.POST.get('created_at')

        nf = Food.objects.get(pk=pk)

        if Food.objects.filter(name=name).exists() == True:
            if name == nf.name:
                Food.objects.filter(pk=pk).update(name=name, desc=desc, price=price, created_at=created_at)
                messages.success(request, "Details were updated.")
            else:
                messages.error(request, 'Food already exists.')
            

        #Reflects the update immediately
        f = get_object_or_404(Food, pk=pk)
        return redirect('view_food_details', pk=pk)
    else:
        return render(request, 'Kiosk/update_food.html', {'f':f})

def delete_food(request, pk):
    Food.objects.filter(pk=pk).delete()
    messages.success(request, "Food deleted successfully.")
    return redirect('view_food')

def add_food(request):
    if(request.method=="POST"):
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        created_at = request.POST.get('created_at')

        if Food.objects.filter(name=name).exists() == True:
             messages.error(request, 'Food already exists.')
        else:
            messages.success(request, "Food successfully added.")
            Food.objects.create(name=name, desc=desc, price=price, created_at=created_at)
            return redirect('view_food')
    return render(request, 'Kiosk/add_food.html')

def view_customer(request):
    customer_object = Customer.objects.all()
    return render(request, 'Kiosk/customers.html', {'customer':customer_object})

def view_customer_details(request, pk):
	c = get_object_or_404(Customer, pk=pk)
	return render(request, 'Kiosk/customer_details.html', {'c': c})

def update_customer(request, pk):
    c = get_object_or_404(Customer, pk=pk)
    if(request.method=="POST"):
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')

        cn = Customer.objects.get(pk=pk)

        if Customer.objects.filter(name=name).exists() == True:
            if name == cn.name:
                Customer.objects.filter(pk=pk).update(name=name, address=address, city=city)
                messages.success(request, "Details were updated.")
            else:
                messages.error(request, 'Customer already exists.')

        #Reflects the update immediately
        c = get_object_or_404(Customer, pk=pk)
        
        return redirect('view_customer_details', pk=pk)
    else:
        return render(request, 'Kiosk/update_customer.html', {'c':c})

def delete_customer(request, pk):
    Customer.objects.filter(pk=pk).delete()
    messages.success(request, "Customer deleted successfully.")
    return redirect('view_customer')


