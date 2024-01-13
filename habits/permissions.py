from rest_framework.permissions import BasePermission


class IsCreator(BasePermission):
    """ Права доступа для владельца. """
    message = 'Вы не являетесь создателем объекта.'

    def has_object_permission(self, request, view, obj):
        """ Настраивает способ проверки разрешений. """
        return request.user == obj.creator
