from rest_framework.routers import DefaultRouter
from .views import taskModelViewSet

app_name = "api-v1"

router = DefaultRouter()

router.register("task", taskModelViewSet, basename="task")

urlpatterns = router.urls
