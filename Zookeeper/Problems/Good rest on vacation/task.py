# put your python code here
holiday_duration = int(input())
food_cost = int(input())
flight_cost = int(input())
hotel_cost = int(input())

hotel_total = (hotel_cost * (holiday_duration - 1))
food_total = (food_cost * holiday_duration)

total_cost = ((flight_cost * 2) + hotel_total + food_total)

print(total_cost)

