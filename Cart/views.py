from django.shortcuts import render, get_object_or_404
from .cart import Cart
from Booking.models import Item
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt




def historicalindex(request):
    return render(request, 'historicalIndex.html')



def cart_summary(request):
    cart = Cart(request)
    cart_items = cart.get_items 
    cart_quantity = cart.__len__()  
    
    if not cart_items:
        cart_quantity = 0
    
    return render(request, 'Cartpage.html', {
        "cart_items": cart_items,
        "cart_quantity": cart_quantity,  
    })


def cart_add(request):
    if request.method == 'POST' and request.POST.get('action') == 'post':
        cart = Cart(request)
        
        item_id = int(request.POST.get('item_id'))
        item = get_object_or_404(Item, id=item_id)

        cart.add(item=item)

        # Update cart quantity after adding item
        cart_quantity = cart.__len__()

        # Prepare JSON response with updated cart quantity
        response_data = {'qty': cart_quantity}
        return JsonResponse(response_data)
    
    return JsonResponse({'error': 'Invalid request or action'})

def cart_delete(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		item_id = int(request.POST.get('item_id'))
		# Call delete Function in Cart
		cart.delete(item=item_id)

		response = JsonResponse({'item':item_id})
		messages.success(request, ("Item Deleted From Shopping Cart..."))
		return response
from django.utils import timezone



from Booking.models import Booking
@csrf_exempt
def book_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = get_object_or_404(Item, id=item_id)

        if not item.is_booked:
            # Check if the item is already booked by someone else
            if item.booked_by and item.booked_by != request.user:
                return JsonResponse({'success': False, 'error': 'Item already booked by another user.'})

            # Create a Booking instance
            booking = Booking(
                user=request.user,
                email=request.user.email,
            )
            booking.save()

            # Update the item's booking status
            item.is_booked = True
            item.booked_by = request.user
            item.booked_at = timezone.now()
            item.save()

            # Remove the item from the cart
            cart = Cart(request)
            cart.delete(item)

            return JsonResponse({'success': True, 'item_id': item_id})
        else:
            return JsonResponse({'success': False, 'error': 'Item already booked.'})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})



@csrf_exempt
def unbook_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = get_object_or_404(Item, id=item_id)
        
        if item.booked_by == request.user:
            booking = Booking.objects.filter(user=request.user, email=request.user.email).first()

            if booking:
                booking.delete()

            item.is_booked = False
            item.booked_by = None
            item.booked_at = None
            item.save()

            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'You are not authorized to unbook this item'})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
