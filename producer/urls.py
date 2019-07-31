from rest_framework import routers
from .views import BankprodViewSet

router = routers.SimpleRouter()
router.register(r'bank', BankprodViewSet)
urlpatterns = router.urls




