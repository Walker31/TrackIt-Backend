from django.db import models
from django.contrib.auth.models import User
from encrypted_fields import fields

class Workout(models.Model):
    WORKOUT_TYPES = [
        ('push', 'Push'),
        ('pull', 'Pull'),
        ('legs', 'Legs'),
    ]

    type = models.CharField(max_length=20, choices=WORKOUT_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    timestamp = models.DateTimeField()
    notes = fields.EncryptedTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_type_display()} - {self.timestamp.date()}"

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, related_name='exercises', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    muscle_group = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ExerciseSet(models.Model):
    exercise = models.ForeignKey(Exercise, related_name='sets', on_delete=models.CASCADE)
    set_number = models.IntegerField()
    weight = fields.EncryptedCharField(max_length=100)
    reps = models.IntegerField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.exercise.name} - Set {self.set_number}"

class Routine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='routines')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=Workout.WORKOUT_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class RoutineExercise(models.Model):
    routine = models.ForeignKey(Routine, related_name='routine_exercises', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    muscle_group = models.CharField(max_length=100)
    sets_count = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.routine.name})"
