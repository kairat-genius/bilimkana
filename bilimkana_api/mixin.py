
"""Mixin views"""
from rest_framework import generics
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter

@extend_schema(
    parameters=[
        OpenApiParameter(name='lang', type=str, location=OpenApiParameter.QUERY,
                         description='Language code (e.g. "ru", "en", "ky") default = ru'),
    ],
)
class LanguageContextListMixin(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'ru')
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True, context={'lang': lang})
        return Response(serializer.data)

@extend_schema(
    parameters=[
        OpenApiParameter(name='lang', type=str, location=OpenApiParameter.QUERY,
                         description='Language code (e.g. "ru", "en", "ky") default = ru'),
    ],
)
class LanguageContextDetailMixin(generics.RetrieveAPIView):
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            'lang': self.request.query_params.get('lang', 'ru')
        })
        return context


"""Mixin serializers"""
from rest_framework import serializers

class TranslationSerializerMixin(serializers.ModelSerializer):
    """Миксин для сериализаторов, поддерживающих переводы полей."""

    def get_localized_field(self, obj, field_name, lang):
        """
        Получает локализованное поле в зависимости от языка.
        """
        default_field_name = f'{field_name}_ru'
        lang_field_name = f'{field_name}_{lang}'
        return getattr(obj, lang_field_name, getattr(obj, default_field_name))


class TitleDescriptionMixin:
    def get_title(self, obj):
        lang = self.context.get('lang', 'ru')
        return self.get_localized_field(obj, 'title', lang)

    def get_description(self, obj):
        lang = self.context.get('lang', 'ru')
        return self.get_localized_field(obj, 'description', lang)

