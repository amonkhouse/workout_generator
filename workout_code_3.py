import random


def get_total_workout_time(active_seconds, rest_seconds, exercises_per_category, total_rounds):
    seconds_per_round = (active_seconds + rest_seconds) * exercises_per_category * 3
    seconds_total = seconds_per_round * int(total_rounds)
    minutes_per_workout = seconds_total / 60
    return int(minutes_per_workout)


workout_type = input("Select a workout type: endurance, or hiit?\t")
assert workout_type in ['endurance', 'hiit']

if workout_type == "endurance":
    a_or_an = "an"
    active = 40
    rest = 20
elif workout_type == "hiit":
    a_or_an = "a"
    active = 20
    rest = 10

total_exercises_per_category = int(input("How many exercises for each body part (legs, upper, and core) "
                                         "would you like to do?\t"))

rounds = int(input("How many rounds would you like to do?\t"))

total_workout_time = get_total_workout_time(active, rest, total_exercises_per_category, rounds)

body_part_focus = {"legs": ["squats", "lunges", "burpees", "squat jumps", "donkey kicks"],
                   "abs": ["plank", "side plank", "flutter kicks", "russian twists", "leg drops"],
                   "arms": ["push-ups", "overhead press", "bicep curls", "tricep dips", "inchworm"]}

exercises = []
for body_part in body_part_focus.keys():
    exercises_to_add = random.sample(body_part_focus[body_part], total_exercises_per_category)
    for exercise in exercises_to_add:
        exercises.append(exercise)

print(f"""This will be {a_or_an} {workout_type} workout, with {active} seconds of activity \
followed by {rest} seconds of rest for each exercise, repeating for {rounds} rounds. 
This will take around {total_workout_time} minutes.
Your randomly chosen exercises are as follows:""")

for i, exercise in enumerate(exercises, 1):
    print(f"{i}. {exercise}")

print("Don't forget to warm up and cool down!")
