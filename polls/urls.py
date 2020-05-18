from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)

app_name = 'polls'
urlpatterns = [
    path("login/", views.login),
    path("", views.home),
    path("choices/", views.ChoiceList.as_view()),
    path("choices/test/<int:pk>/", views.ChoiceDetail.as_view()),
    path('questions/', views.QuestionListCreateAPIView.as_view()),
    path('api/', include(router.urls)),
    path('api/api-auth', include('rest_framework.urls', namespace='rest-framework'))
]
