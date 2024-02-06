from django.shortcuts import render
from kitchen_api_app.serializers import RecipeSeralizer
from kitchen_api_app.models import RecipeContainer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination





class Paginator(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class RecipeView(ModelViewSet):
    serializer_class = RecipeSeralizer
    pagination_class = Paginator
    def get_queryset(self,*args,**kwargs):
        return RecipeContainer.objects.all()