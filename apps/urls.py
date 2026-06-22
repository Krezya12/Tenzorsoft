from django.urls import path

from apps.views import *

urlpatterns = [
    path('', home, name='home'),
    path('', HomeListView.as_view(), name='home'),

]