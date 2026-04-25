from django.contrib import admin
from .models import Workout, Exercise, ExerciseSet, Routine, RoutineExercise

admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(ExerciseSet)
admin.site.register(Routine)
admin.site.register(RoutineExercise)
