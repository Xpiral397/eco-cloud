from django.urls import path
from .views import say_helo


urlpatterns = [
    path('', say_helo)
]
