import numpy as np

users = 4
days = 2

fitness_data_dic = {f"user {i+1}":[] for i in range(users)}
print(fitness_data_dic)

# number of peaople 4, days 7

for d in range(1,days+1):
    print(f"Eneter the steps for day {d}")
    for p in range(1,users+1):
        value = int(input())
        fitness_data_dic[f"user {p}"].append(value)

print(fitness_data_dic)

fitness_data_list_np = np.array(list(fitness_data_dic.values()))  

# fitness_data_list_np = np.array([[100,2000,4000,6000],[4000,5000,6000,2000], [400,8000,10000,2000], [400,5000,6000,1000]])

avg_per_person = np.mean(fitness_data_list_np, axis=1)
print("Average steps per person:", avg_per_person)

avg_per_day = np.mean(fitness_data_list_np, axis=0)
print("Average steps per day:", avg_per_day)

most_active_person = np.argmax(avg_per_person) + 1
print("Most active person on average: User", most_active_person)

days_person3_above_8000 = np.sum(fitness_data_list_np[2] > 8000)
print("The Day Person 3 > 8000 steps:", days_person3_above_8000)

weekly_total = np.sum(fitness_data_list_np, axis=1)
print("Weekly total steps per person:", weekly_total)

total_per_day = np.sum(fitness_data_list_np, axis=0)
max_day = np.argmax(total_per_day) + 1
print("Day with maximum group steps: Day", max_day)

cleaned_data = np.where(fitness_data_list_np < 5000, 5000, fitness_data_list_np)
print("Data after replacing values < 5000:")
print(cleaned_data)

median_steps = np.median(fitness_data_list_np)
print("Overall median steps:", median_steps)

# avg_per_person = np.mean(fitness_data_list_np, axis=1)

# print("average steps per person...")
# for i, avg in enumerate(avg_per_person, start=1):
#     print(f"User {i}: {avg:.2f}")


# avg_per_day = np.mean(fitness_data_list_np, axis=0)

# print("Average Steps per Day...")
# for d, avg in enumerate(avg_per_day, start=1):
#     print(f"Day {d}: {avg:.2f}")

# most_active_person = np.argmax(avg_per_person) + 1
# print(f"Person who walked the most on average: User {most_active_person}")


# person3_days = np.sum(fitness_data_list_np[2] > 8000)
# print(f"Days Person 3 walked > 8000 steps: {person3_days}")

# weekly_total = np.sum(fitness_data_list_np, axis=1)

# print("Weekly Total Steps per Person:")
# for i, total in enumerate(weekly_total, start=1):
#     print(f"User {i}: {total}")

# total_per_day = np.sum(fitness_data_list_np, axis=0)
# max_day = np.argmax(total_per_day) + 1
# print(f"Day with Maximum Group Steps: Day {max_day}")


# cleaned_data = np.where(fitness_data_list_np < 5000, 5000, fitness_data_list_np)
# print("After Replacing < 5000 with 5000:")
# print(cleaned_data)

# median_steps = np.median(fitness_data_list_np)
# print(f"Overall Median of All Step Values: {median_steps}")
