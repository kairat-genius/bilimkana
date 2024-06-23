from parler_rest.serializers import TranslatableModelSerializer
from .models import FAQ

class FAQSerializer(TranslatableModelSerializer):
    class Meta:
        model = FAQ
        fields = ('id', 'question', 'answer')