from django.urls import path
from .views import HomePagesView,AboutPagesView

urlpatterns = [
    path('about/',AboutPagesView.as_view(),name='about'),
    path('',HomePagesView.as_view(),name='home')
]
