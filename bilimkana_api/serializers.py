from parler_rest.serializers import TranslatableModelSerializer
from .models import FAQ, News, Events

class FAQSerializer(TranslatableModelSerializer):
    class Meta:
        model = FAQ
        fields = ('id', 'question', 'answer')


class NewsSerializer(TranslatableModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class EventsSerializer(TranslatableModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
