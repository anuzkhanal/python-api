from rest_framework.permissions import IsAuthenticated

from todos.models import Todo
from .serializers import TodoSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.


class TodosAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Todo.objects.filter(owner=self.request.user)
        status_query = self.request.query_params.get("status", None)
        if status_query is not None:
            print("queryset", queryset)
            queryset = queryset.filter(status=status_query)
        return queryset


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    looking_field = "id"

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
