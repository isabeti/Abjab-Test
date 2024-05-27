from django.urls import path
from .views import AbjadCalculate, PersianWordSearchView

app_name = 'abjad_calculator'
urlpatterns = [
    path('calculator/', AbjadCalculate.as_view(), name='calculator'),
    path('search/<str:word>/', PersianWordSearchView.as_view(), name='persian_word_search'),
]