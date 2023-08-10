from django.shortcuts import render, redirect
from django.http import Http404
from .forms import NewDishForm, OrderForm, UpdateStatusForm


# Create your views here.
menu = [
    {'id': 1, 'name': 'Margherita Pizza', 'price': 10.99, 'availability': True},
    {'id': 2, 'name': 'Pasta Carbonara', 'price': 12.99, 'availability': True},
    {'id': 2, 'name': 'Idli Dosa', 'price': 34.99, 'availability': False},
    
]
orders=[]

def menu_view(request):
    context = {'menu': menu}

    if request.method == 'POST':
        form = NewDishForm(request.POST)
        if form.is_valid():
            new_dish = {
                'id': len(menu) + 1,
                'name': form.cleaned_data['name'],
                'price': form.cleaned_data['price'],
                'availability': form.cleaned_data['availability'],
            }
            menu.append(new_dish)
    else:
        form = NewDishForm()

    context['form'] = form
    return render(request, 'menu.html', context)


def remove_dish(request, dish_id):
    for dish in menu:
        if dish['id'] == dish_id:
            menu.remove(dish)
            break
    return redirect('menu')

def update_availability(request, dish_id):
    for dish in menu:
        if dish['id'] == dish_id:
            dish['availability'] = not dish['availability']
            break
    return redirect('menu')



def order_view(request):
    context = {}
    menu_choices = [(dish['id'], dish['name']) for dish in menu]
    if request.method == 'POST':
        
        form = OrderForm(menu_choices, request.POST)
        
        if form.is_valid():
            customer_name = form.cleaned_data['customer_name']
            selected_dish_ids = form.cleaned_data['selected_dishes']
            selected_dishes = [dish for dish in menu if str(dish['id']) in selected_dish_ids]
            
            
            unavailable_dishes = [dish for dish in selected_dishes if not dish['availability']]
            if unavailable_dishes:
                context['unavailable_dishes'] = unavailable_dishes
            else:
            
                new_order = {
                    'order_id': len(orders) + 1,
                    'customer_name': customer_name,
                    'dishes': selected_dishes,
                    'status': 'received',  
                }
                orders.append(new_order)
                context['order_placed'] = True

    else:
        form = OrderForm(menu_choices)

    context = {'form': form}
    print("order-context",context)
    return render(request, 'order.html', context)



def update_status_view(request, order_id):
    context = {}
    order = None
    
    for o in orders:
        if o['order_id'] == order_id:
            order = o
            break

    if order is None:
        raise Http404("Order not found")

    if request.method == 'POST':
        form = UpdateStatusForm(request.POST)
        if form.is_valid():
            new_status = form.cleaned_data['new_status']
            order['status'] = new_status
            context['status_updated'] = True
    else:
        form = UpdateStatusForm()

    context['form'] = form
    context['order'] = order
    return render(request, 'update_status.html', context)


def review_orders_view(request):
    context = {'orders': orders}
    print("order-view",context)
    return render(request, 'review_orders.html', context)




