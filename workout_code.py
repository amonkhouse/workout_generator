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

print(chosen_exercises)
