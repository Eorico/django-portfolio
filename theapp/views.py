from django.shortcuts import render
from .models import Colors
from django.db.models import Q
from django.views.generic import TemplateView

class Searchpage(TemplateView):
    template_name = "Search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q")
        if query:
            context["results"] = Colors.objects.filter(
                Q(UI_ID__icontains=query) |
                Q(NAME__icontains=query) |
                Q(RGB__icontains=query) |
                Q(SYMBOL__icontains=query) |
                Q(USAGE_FOR_BRANDING__icontains=query) |
                Q(CATEGORY__icontains=query) |
                Q(MEANING__icontains=query)
            )
        else:
            context["results"] = None  
        return context

def mamba(request):
    return render(request, 'mamba.html')  

def IgTrend(request):
    return render(request, 'MISMS.html')

def ORMTable(request):
    return render(request, 'Table.html')
