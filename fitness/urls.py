from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    WorkoutViewSet, ExerciseViewSet, ExerciseSetViewSet,
    RoutineViewSet, RoutineExerciseViewSet
)

router = DefaultRouter()
router.register(r'workouts', WorkoutViewSet, basename='workout')
router.register(r'exercises', ExerciseViewSet, basename='exercise')
router.register(r'sets', ExerciseSetViewSet, basename='exerciseset')
router.register(r'routines', RoutineViewSet, basename='routine')
router.register(r'routine-exercises', RoutineExerciseViewSet, basename='routineexercise')

urlpatterns = [
    path('', include(router.urls)),
]
