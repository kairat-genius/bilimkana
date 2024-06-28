from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import FAQ, Category, Program, Teacher
from .serializers import FAQSerializer, CategorySerializer, ProgramSerializer, TeacherSerializer, ApplicationsSerializer

class FAQListAPIView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'ru')
        queryset = self.get_queryset()
        serializer = FAQSerializer(queryset, many=True, context={'lang': lang})
        return Response(serializer.data)

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'ru')
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True, context={'lang': lang})
        return Response(serializer.data)

class ProgramListAPIView(generics.ListAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'ru')
        queryset = self.get_queryset()
        serializer = ProgramSerializer(queryset, many=True, context={'lang': lang})
        return Response(serializer.data)

class TeacherListAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'ru')
        queryset = self.get_queryset()
        serializer = TeacherSerializer(queryset, many=True, context={'lang': lang})
        return Response(serializer.data)


@api_view(['POST'])
def create_application(request):
    serializer = ApplicationsSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)