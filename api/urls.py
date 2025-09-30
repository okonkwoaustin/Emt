from rest_framework.routers import SimpleRouter

from .views import EmployeeViewSet, EmployeeTaskViewSet

router = SimpleRouter()

router.register("employees", EmployeeViewSet, basename="employee"),
router.register("tasks", EmployeeTaskViewSet, basename="task"),

urlpatterns = router.urls