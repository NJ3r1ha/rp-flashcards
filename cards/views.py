from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .models import Card


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")
    template_name = "card_list.html"


class CardCreateView(CreateView):
    model = Card
    template_name = "card_form.html"
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("cards:card_create")


class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("cards:card_list")
