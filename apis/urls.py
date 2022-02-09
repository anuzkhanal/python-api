from django.urls import path

from authentication.views import ResgisterAPIView, LoginAPIView, ChangePasswordAPIView
from todos.views import TodosAPIView, TodoDetailAPIView

urlpatterns = [
    path("signup", ResgisterAPIView.as_view(), name="register"),
    path("signin", LoginAPIView.as_view(), name="login"),
    path("changePassword", ChangePasswordAPIView.as_view(), name="changepassword"),
    path("todos", TodosAPIView.as_view(), name="todos"),
    path("todos/<int:pk>", TodoDetailAPIView.as_view(), name="todo"),
]
