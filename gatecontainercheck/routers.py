from rest_framework import routers

from machine.api.viewsets import MachineViewSet

router = routers.DefaultRouter()
router.register(r'machine', MachineViewSet)
