from django.urls import path
from .views import AbjadCalculateFA

app_name = 'abjad_calculator'
urlpatterns = [
    path('calculator/', AbjadCalculateFA.as_view(), name='calculator')
]