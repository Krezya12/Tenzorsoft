from django.urls import path

from apps.views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),

]