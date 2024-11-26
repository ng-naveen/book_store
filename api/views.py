from api.serializers import BookSerializer, UserSerializer
from api.models import Books
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import authentication, permissions



class BooksView(ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookSerializer
    queryset = Books.objects.all()

    @action(methods=['GET'], detail=False)
    def get_genres(self, request, *args, **kwargs):
        genres_list = Books.objects.values_list('genre', flat=True).distinct()
        return Response(data=genres_list)

    def get_queryset(self):
        query_set = self.queryset
        
        if 'genre' in self.request.query_params:
            query_set = query_set.filter(genre=self.request.query_params.get('genre'))
        if 'price_gt' in self.request.query_params:
            query_set = query_set.filter(price__gt=int(self.request.query_params.get('price_gt')))
        return query_set

        
class UserView(ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()


