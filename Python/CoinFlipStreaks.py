import random
def StreakCheck(list):
    streak = 0
    streak_number = 0
    previous_value=list[0]
    for index, item in enumerate(list):
        # print(item)
        current_value=item
        if(current_value==previous_value):
            streak+=1
        else:
            streak=1
            previous_value=current_value
        if(streak==6):
            streak_number+=1
        # print('Current streak is '+ str(streak))
    # print('Final streak number is ' + str(streak_number))
    return streak_number

# test = [1,0,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,0,0,0,1]
# StreakCheck(test)

def GenerateList():
    SIZE = 100
    list=[]
    for i in range(SIZE):
        list.append(random.randint(0,1))
    return list

# test_list = GenerateList()
# for i in range(len(test_list)):
#     print(test_list[i])
# print(len(test_list))

experiment_number=10000
final_streak_number = 0
for i in range(10000):
    final_streak_number = 0
    sample = GenerateList()
    current_streak_number = StreakCheck(sample)
    final_streak_number = final_streak_number + current_streak_number
    print('Chance of streak: %s%%' % (final_streak_number/100))
