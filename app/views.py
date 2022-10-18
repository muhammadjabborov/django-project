from django.shortcuts import render
from django.views.generic import TemplateView

from app.models import Product, Arrival, Blog


class Template(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.all().order_by('-created_at')
        arrival = Arrival.objects.all().order_by('-created_at')
        blog = Blog.objects.all().order_by('-created_at')
        context['products'] = product
        context['arrivals'] = arrival
        context['blogs'] = blog
        return context
