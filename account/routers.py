from rest_framework.routers import DefaultRouter
from .viewsets import AccountViewset

router = DefaultRouter()
router.register('account', AccountViewset)
