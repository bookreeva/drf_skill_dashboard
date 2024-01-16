from rest_framework import serializers

from users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    """ Сериалайзер для создания модели пользователя. """

    class Meta:
        """ Метаданные сериалайзера. """
        model = User
        fields = ('email', 'password', 'login', 'telegram_id',)


class UserProfileSerializer(serializers.ModelSerializer):
    """ Сериалайзер для профиля модели пользователя. """

    class Meta:
        """ Метаданные сериалайзера. """
        model = User
        fields = ('email', 'login', 'telegram_id', 'phone', 'city', 'avatar',)


class UserSerializer(serializers.ModelSerializer):
    """ Сериалайзер для модели пользователя(дефолтный). """

    class Meta:
        """ Метаданные сериалайзера. """
        model = User
        fields = ('email',)
