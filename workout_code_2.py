import random

workout_type = "endurance"
rounds = 6
total_exercises = 6

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

chosen_exercises = random.sample(exercises, total_exercises)

if workout_type == "endurance":
    a_or_an = "an"
    active = 40
    rest = 20
elif workout_type == "hiit":
    a_or_an = "a"
    active = 20
    rest = 10


def get_total_workout_time(active_seconds, rest_seconds, total_exercises, total_rounds):
    seconds_per_round = (active_seconds + rest_seconds) * total_exercises
    seconds_total = seconds_per_round * int(total_rounds)
    minutes_per_workout = seconds_total / 60
    return minutes_per_workout


workout_time = get_total_workout_time(active, rest, total_exercises, rounds)

print(f"""This will be {a_or_an} {workout_type} workout, with {active} seconds of activity \
followed by {rest} seconds of rest for each exercise, repeating for {rounds} rounds. 
This will take {workout_time} minutes.
Your randomly chosen exercises are as follows:""")

for i, exercise in enumerate(chosen_exercises, 1):
    print(f"{i}. {exercise}")

print("Don't forget to warm up and cool down!")
