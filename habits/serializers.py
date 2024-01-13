from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели привычки. """

    class Meta:
        """ Метаданные для сериализатора. """
        model = Habit
        fields = ('action',)


class HabitCreateSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания модели привычки. """

    class Meta:
        """ Метаданные для сериализатора. """
        model = Habit
        exclude = ('creator',)


class HabitDetailSerializer(serializers.ModelSerializer):
    """ Сериализатор для конкретной модели привычки. """

    class Meta:
        """ Метаданные сериализатора. """
        model = Habit
        fields = '__all__'
