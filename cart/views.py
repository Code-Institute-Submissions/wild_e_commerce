from django.shortcuts import render, get_object_or_404, redirect, reverse
from models import CartItem
from django.contrib.auth.decorators import login_required
from products.models import Product
from payments.forms import MakePaymentForm
from django.template.context_processors import csrf
from django.contrib import messages
from django.conf import settings
import stripe
from categories.models import Category

from django.contrib.auth.models import User
from .serializers import UserSerializer

from rest_framework import viewsets
from .serializers import CartItemSerializer

stripe.api_key = settings.STRIPE_SECRET


@login_required(login_url="/accounts/login")
def user_cart(request):
    cartItems = CartItem.objects.filter(user=request.user)#load the cart items from the database
    total = 0
    for item in cartItems:
        total += item.product.price# increming the total by the price

    if request.method == 'POST':
        form = MakePaymentForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request, "You have successfully paid")
                CartItem.objects.filter(user=request.user).delete()
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        if len(cartItems) == 0: # if no. of item in the cart is 0. return empty cart httml
            return render(request, 'empty_cart.html')

        form = MakePaymentForm() # if we have something in the cart, we create the makepaymentform
    categories = Category.objects.filter(parent=None)
    args = {'form': form,
            'items': cartItems,
            'total': total,
            'publishable': settings.STRIPE_PUBLISHABLE,
            'categories': categories
            }
    args.update(csrf(request))# adding csrf token to the form

    return render(request, 'cart.html', args)


@login_required(login_url="/accounts/login")
def add_to_cart(request, id):
    product = get_object_or_404(Product, pk=id)
    cartItem = CartItem(
        user=request.user,
        product=product,
        quantity=1
    )
    cartItem.save()
    return redirect(reverse('cart'))


def remove_from_cart(request, id):
    CartItem.objects.get(id=id).delete()
    return redirect(reverse('cart'))


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
