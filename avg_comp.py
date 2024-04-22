your_score = 92
class_points = [75, 60, 55, 80, 85, 90, 95, 65, 70, 50, your_score]

def avg_comp(class_points):
    avg = sum(class_points) / len(class_points)
    if avg > your_score:
        print(f"The class average is {avg} which is higher than your score of {your_score}.")
    else:
        print(f"The class average is {avg} which is lower than your score of {your_score}.")

avg_comp(class_points)

