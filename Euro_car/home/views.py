from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView
from brand.models import Brand
from car.models import Car
from user.models import History
from django.shortcuts import get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from .forms import CommentForm
# Create your views here.


class HomeView(ListView):
    template_name = 'index.html'
    model = Car
    context_object_name = 'car'

    def get_queryset(self):
        brand_slug = self.kwargs.get('brand_slug')
        if brand_slug:
            brand = Brand.objects.get(slug=brand_slug)
            return Car.objects.filter(brand=brand)
        return Car.objects.all()

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['brand'] = Brand.objects.all()
        return context

# Details View
class DetailsView(DetailView):
    template_name = 'details.html'
    model = Car
    # def get_object(self):
    #     pk = self.kwargs.get(self.pk_url_kwarg)
    #     return Car.objects.get(pk = pk)
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=request.POST)
        car = self.get_object()

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    
# Buy Now
def buy_now(request, id):
    car = Car.objects.get(pk=id)
    if car.quantity > 0:
            history = History(name=car.name, brand=car.brand.name, quantity=1, user=request.user)
            history.save()
            car.quantity -= 1
            car.save()
    return redirect('profile')


