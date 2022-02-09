from rest_framework import status, response, permissions

from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate


from todos.models import Todo
from .serializers import TodoSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class TodosAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    filter_backend = [DjangoFilterBackend]

    filterset_fields = ["status"]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    looking_field = "id"

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
