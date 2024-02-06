from rest_framework.serializers import ModelSerializer
from kitchen_api_app.models import RecipeContainer


class RecipeSeralizer(ModelSerializer):

    class Meta:
        model = RecipeContainer
        fields=['title','creator','description','number']