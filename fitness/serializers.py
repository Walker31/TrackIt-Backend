from rest_framework import serializers
from .models import Workout, Exercise, ExerciseSet, Routine, RoutineExercise

class ExerciseSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseSet
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    sets = ExerciseSetSerializer(many=True, required=False)
    
    class Meta:
        model = Exercise
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, required=False)
    
    class Meta:
        model = Workout
        fields = '__all__'
        read_only_fields = ('user',)

    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises', [])
        workout = Workout.objects.create(**validated_data)
        for exercise_data in exercises_data:
            sets_data = exercise_data.pop('sets', [])
            exercise = Exercise.objects.create(workout=workout, **exercise_data)
            for set_data in sets_data:
                ExerciseSet.objects.create(exercise=exercise, **set_data)
        return workout

class RoutineExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineExercise
        fields = '__all__'

class RoutineSerializer(serializers.ModelSerializer):
    routine_exercises = RoutineExerciseSerializer(many=True, read_only=True)
    
    class Meta:
        model = Routine
        fields = '__all__'
        read_only_fields = ('user',)
