from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.tasks import send_daily_habit_messages, send_weekly_habit_messages
from habits.paginators import HabitPaginator
from habits.permissions import IsCreator
from habits.serializers import (HabitSerializer, HabitDetailSerializer,
                                HabitCreateSerializer)


class HabitCreateAPIView(generics.CreateAPIView):
    """ Представление для создания урока. """
    serializer_class = HabitCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """ Присваивает текущего пользователя как создателя. """
        new_lesson = serializer.save()
        new_lesson.creator = self.request.user
        new_lesson.save()

        send_daily_habit_messages.delay()
        send_weekly_habit_messages.delay()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """ Представление для вывода конкретной привычки. """
    serializer_class = HabitDetailSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsCreator]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Представление для редактирования привычки. """
    serializer_class = HabitDetailSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsCreator]

    def perform_update(self, serializer):
        """ Создает отправку обновлений пользователям. """
        update_habit = serializer.save()
        update_habit.save()

        send_daily_habit_messages.delay()
        send_weekly_habit_messages.delay()


class HabitListAPIView(generics.ListAPIView):
    """ Представление для вывода списка привычек. """
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_published=True)
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]


class HabitUserListAPIView(generics.ListAPIView):
    """ Представление для вывода списка привычек. """
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """ Получает список привычек текущего пользователя. """
        user = self.request.user
        return Habit.objects.filter(creator=user)


class HabitDestroyApiView(generics.DestroyAPIView):
    """ Представление для удаления привычки. """
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsCreator]
