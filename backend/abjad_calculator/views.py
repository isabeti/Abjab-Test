from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from .forms import AbjadCalculateForm
from .utils import abjad_clalc_FA, abjad_clalc_EN

from .models import PersianWord, EnglishWord
from . import serializers
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class AbjadCalculate(APIView):
    def post(slef, request):
        form = AbjadCalculateForm(request.data)
        if form.is_valid():
            word = form.cleaned_data['word']
            is_persian = form.cleaned_data['is_persian']

            if is_persian == True:
                data = abjad_clalc_FA(word)
            else:
                data = abjad_clalc_EN(word)
            return Response(data)
        return Response(form.errors, status=HTTP_400_BAD_REQUEST)

class PersianWordPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'page_size': self.get_page_size(self.request),
            'results': data
        })
    
class PersianWordSearchView(APIView):
    def get(self, request, word, format=None):
        form = AbjadCalculateForm(data={'word': word})
        if form.is_valid():
            word = form.cleaned_data['word']
            is_persian = form.cleaned_data['is_persian']
            data = abjad_clalc_FA(word)

            abjad_number = data['box_data']['kabir']['abjad_number']
            filter_type = request.query_params.get('filter_type', 'kabir')
            
            if filter_type == 'kabir':
                PersianWord.objects.filter(kabir_abjad=abjad_number)
            elif filter_type == 'saghir':
                PersianWord.objects.filter(saghir_abjad=abjad_number)
            elif filter_type == 'vasit':
                PersianWord.objects.filter(vasit_abjad=abjad_number)
            else:
                return Response('s', status=HTTP_400_BAD_REQUEST)

            queryset = PersianWord.objects.filter(word=word)
            paginator = PersianWordPagination()
            page = paginator.paginate_queryset(queryset, request)

            if page is not None:
                serializer = serializers.PersianWordSerilaizer(page, many=True)
                return paginator.get_paginated_response(serializer.data)

            serializer = serializers.PersianWordSerilaizer(queryset, many=True)
            return Response(serializer.data)
        return Response(form.errors, status=HTTP_400_BAD_REQUEST)