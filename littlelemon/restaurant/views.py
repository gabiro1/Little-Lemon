# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu
from django.shortcuts import render, get_object_or_404


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    items = Menu.objects.all()  
    return render(request, 'menu.html', {'items': items})

def display_menu_items(request,pk):
    if pk:
        menu_item = objects.get(pk=pk)

    else:
        menu_item = ''
    
    return render(request, 'menu_item.html', {'menu_item':menu_item})


def display_menu_item(request, pk):
    # Retrieve the menu item by primary key (pk)
    menu_item = get_object_or_404(Menu, pk=pk)
    return render(request, 'menu_item.html', {'menu_item': menu_item})
