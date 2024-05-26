from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from .forms import AbjadCalculateForm
from .utils import abjad_clalc_FA, abjad_clalc_EN

# Create your views here.
class AbjadCalculateFA(APIView):
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
    