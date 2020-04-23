import random

exercises = ["squats",
             "lunges",
             "push-ups",
             "flutter kicks",
             "inchworm",
             "high knees",
             "burpees",
             "donkey kicks",
             "plank",
             "squat jumps"]

chosen_exercises = random.sample(exercises, 5)

for i, exercise in enumerate(chosen_exercises, 1):
    print(f"{i}. {exercise}")
