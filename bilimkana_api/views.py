from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import FAQ, Category, Program, Teacher, Applications, News, Events
from .serializers import FAQSerializer, CategorySerializer, ProgramSerializer, TeacherSerializer, NewsSerializer, EventsSerializer, ApplicationsSerializer

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


class NewsListAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = NewsSerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'ru')
        queryset = self.get_queryset()
        serializer = NewsSerializer(queryset, many=True, context={'lang': lang})
        return Response(serializer.data)


class EventsListAPIView(generics.ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'ru')
        queryset = self.get_queryset()
        serializer = EventsSerializer(queryset, many=True, context={'lang': lang})
        return Response(serializer.data)


class ApplicationListAPIView(generics.ListAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ApplicationsSerializer(queryset, many=True, context={'lang': 'ru'})
        return Response(serializer.data)


class ApplicationCreateAPIView(generics.CreateAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)