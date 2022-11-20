a_hours = int(input())
b_hours = int(input())
h_hours = int(input())

if h_hours > b_hours:
    print("Excess")
elif h_hours < a_hours:
    print("Deficiency")
else:
    print("Normal")
