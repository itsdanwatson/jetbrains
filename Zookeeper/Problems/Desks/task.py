# put your python code here

group_one = int(input())
group_two = int(input())
group_three = int(input())

number_of_desks = (((group_one % 2) + (group_one // 2))
                   + ((group_two % 2) + (group_two // 2))
                   + ((group_three % 2) + (group_three // 2)))

print(number_of_desks)
