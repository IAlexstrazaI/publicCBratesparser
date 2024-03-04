from django.shortcuts import render
from .models import City, Country
from django.views import generic
# Create your views here.
from django.utils import timezone
from django.views.generic.detail import DetailView
from articles.models import Article

def index(request):
    cities=City.objects.all().count()
    countries=Country.objects.all().count()
    return render(
        request,
        'index.html',
        context={'cities':cities,'countries':countries},
    )


class CitiesListView(generic.ListView):
    model = City
    context_object_name = 'my_city_list'   # ваше собственное имя переменной контекста в шаблоне
    queryset = City.objects.all()
    template_name = 'city/my_city_list.html'  # Определение имени вашего шаблона и его расположения


class CityDetailView(generic.DetailView):
    model = City






class ArticleDetailView(DetailView):
    model = Article
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context