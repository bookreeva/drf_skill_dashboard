from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import IsOwner, IsSuperUser
from users.serializers import (UserCreateSerializer, UserProfileSerializer,
                               UserSerializer)


class UserViewSet(ModelViewSet):
    """ Сет представлений для модели пользователя. """
    queryset = User.objects.all()
    # Сериалайзеры для представлений.
    default_serializer = UserSerializer
    serializers = {
        'create': UserCreateSerializer,
        'retrieve': UserProfileSerializer,
        'update': UserProfileSerializer,
    }

    def get_object(self):
        """ Получает текущего пользователя. """
        return self.request.user

    def perform_create(self, serializer):
        """ Сохраняет пароль в зашифрованном виде через set_password(). """
        user = serializer.save()
        user.set_password(user.password)
        user.save()

    def get_serializer_class(self):
        """ Возвращает сериализатор в зависимости от выбора запроса. """
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        """ Возвращает права в зависимости от статуса пользователя. """
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'list':
            permission_classes = [IsSuperUser]
        else:
            permission_classes = [IsAuthenticated, IsOwner]

        return [permission() for permission in permission_classes]
