from rest_framework import generics
from django.utils.translation import activate
from .serializers import FAQSerializer
from .models import FAQ

class FAQList(generics.ListAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        language = self.request.GET.get('lang', 'ru')
        activate(language)

        return FAQ.objects.language(language)


