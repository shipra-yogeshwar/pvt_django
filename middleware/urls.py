from django.urls import path

from . import views


urlpatterns = [
    path('middleware/', views.MiddlewareAPIView.as_view()),
]