from rest_framework import permissions
from knox.auth import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from .serializers import ErrorcodeSerializer
from .models import Errorcode


class MiddlewareAPIView(ModelViewSet):
    permission_classes_by_action = {
        'POST': [permissions.IsAuthenticated],
        'GET': [permissions.IsAdminUser],
        'PUT': [permissions.IsAuthenticated],
        'PATCH': [permissions.IsAuthenticated],
        'default': [permissions.IsAdminUser]
    }

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [
                permission()
                for permission in self.permission_classes_by_action[self.request.method]
            ]
        except KeyError:
            # action is not set return default permission_classes
            return [
                permission()
                for permission in self.permission_classes_by_action["default"]
            ]

    serializer_class = ErrorcodeSerializer
    queryset = Errorcode.objects.all()
    authentication_classes = (TokenAuthentication, )
