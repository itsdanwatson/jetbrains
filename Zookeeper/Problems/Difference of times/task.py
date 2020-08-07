# put your python code here

moment_a_hours = int(input())
moment_a_minutes = int(input())
moment_a_seconds = int(input())

moment_b_hours = int(input())
moment_b_minutes = int(input())
moment_b_seconds = int(input())

# Convert to seconds
convert_a_hours = int((moment_a_hours * 60) * 60)
convert_a_minutes = int(moment_a_minutes * 60)

convert_b_hours = int((moment_b_hours * 60) * 60)
convert_b_minutes = int(moment_b_minutes * 60)

moment_a = int(convert_a_hours) + int(convert_a_minutes) + int(moment_a_seconds)

moment_b = int(convert_b_hours) + int(convert_b_minutes) + int(moment_b_seconds)

time_difference = (int(moment_b) - int(moment_a))

print(time_difference)
