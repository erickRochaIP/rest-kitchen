from rest_framework import viewsets, generics
from .models import Receita
from .serializers import ReceitaSerializer


# Create your views here.
class ReceitaViewSet(viewsets.ModelViewSet):

    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

    def get_queryset(self):
        queryset = Receita.objects.all()
        chef = self.request.query_params.get('id_chef')
        if chef is not None:
            queryset = queryset.filter(id_chef=chef)
        return queryset
