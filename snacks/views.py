from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import SnackList

# Create your views here.
class SnackListView(ListView):
    template_name = "snack_list.html"
    model = SnackList
    

class SnackDetailView(TemplateView):
    template_name = "snack_detail.html"