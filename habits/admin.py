from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """Отображение привычек в административной панели."""
    list_display = ('id', 'action', 'creator', 'is_published',)
