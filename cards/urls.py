from django.urls import path

from .views import CardListView, CardCreateView, CardUpdateView

app_name = "cards"

urlpatterns = [
    path("", CardListView.as_view(), name="card_list"),
    path("new", CardCreateView.as_view(), name="card_create"),
    path("edit/<int:pk>", CardUpdateView.as_view(), name="card_update"),
]
