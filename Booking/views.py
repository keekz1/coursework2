from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import ToDoList, UnsavedItem, Item,UnsavedItem, Item, Image, Profile
from .forms import AddItemForm
from PIL import Image as PILImage
from io import BytesIO
import os
from django.shortcuts import render, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import  UpdateUserForm, UpdateProfileForm
from django.contrib import messages


from django.conf import settings

@login_required(login_url='login')
def home(request):
    items = Item.objects.all()
    profile = Profile.objects.all()
    return render(request, 'homepage.html', { 'profile': profile, 'items': items})

@login_required
def index(request, id):
    try:
        ls = ToDoList.objects.get(id=id)
    except ToDoList.DoesNotExist:
        return HttpResponse("ToDoList does not exist.")
    return render(request, "Booking/list.html", {"ls": ls})






@login_required
def list_view(request, id):
    try:
        ls = ToDoList.objects.get(id=id)
    except ToDoList.DoesNotExist:
        return HttpResponse("ToDoList does not exist.")

    # Get all unsaved items
    unsaved_items = UnsavedItem.objects.all()

    if request.method == 'POST':
        form = AddItemForm(request.POST, request.FILES) 
        if 'add_item' in request.POST:
            if form.is_valid():
                unsaved_item = form.save(commit=False)
                unsaved_item.save()
                return redirect('list_view', id=id)  
        elif 'save' in request.POST:
            for unsaved_item in unsaved_items:
                # Create a new saved item for each unsaved item
                saved_item = Item.objects.create(
                    list=ls,
                    name=unsaved_item.name,
                    type=unsaved_item.type,
                    audit=unsaved_item.audit,
                    location=unsaved_item.location,
                    image=unsaved_item.image
                )
                # Save the newly created item
                saved_item.save()
            # Clear all unsaved items after saving
            unsaved_items.delete()
            return redirect('list_view', id=id)
        elif 'delete_item' in request.POST:
            item_id = request.POST.get('delete_item')
            # Delete the selected item
            ls.items.filter(id=item_id).delete()
            return redirect('list_view', id=id)
    else:
        # If the request method is not POST, initialize the form
        form = AddItemForm()

    saved_items = ls.items.all()

    return render(request, "list.html", {"ls": ls, "unsaved_items": unsaved_items, "saved_items": saved_items, "form": form})

def delete_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('itemId')
        try:
            item = Item.objects.get(id=item_id)
            item.delete()
            return JsonResponse({'success': True})
        except Item.DoesNotExist:
            try:
                unsaved_item = UnsavedItem.objects.get(id=item_id)
                unsaved_item.delete()
                return JsonResponse({'success': True})
            except UnsavedItem.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Item not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


    

def item_info(request, item_id):
    # Retrieve the item object using its ID
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'itemInfo.html', {'item': item})


def update_user(request):
    return render(request, 'profilepage.html',{})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')
    
@login_required
def student_bookings(request):
    booked_items = Item.objects.filter(booked_by=request.user)
    return render(request, 'booking.html', {'booked_items': booked_items})