from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from brand.models import Brand
from car.models import Car
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
    def get_object(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Car.objects.get(pk = pk)