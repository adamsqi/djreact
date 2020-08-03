from django.urls import path

from .views import ArticlListView, ArticlDetailView

urlpatterns = [
    path('', ArticlListView.as_view()),
    path('<pk>', ArticlDetailView.as_view()),
]
