from Booking.models import Item

class Cart():
    def __init__(self, request):
        self.session = request.session

        # Initialize cart if not already present in session
        if 'cart' not in self.session:
            self.session['cart'] = {}

        self.cart = self.session['cart']

    def add(self, item):
        item_id = str(item.id)

        if item_id in self.cart:
            pass
        else:
            self.cart[item_id] = {'audit': str(item.audit)}

        self.session.modified = True

    def get_items(self):
        item_ids = self.cart.keys()
        items = Item.objects.filter(id__in=item_ids)
        return items

    def delete(self, item):
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.session.modified = True

    def __len__(self):
        return len(self.cart)
