# put your python code here
sample_input = int(input())
if (sample_input % 4 == 0 and sample_input % 100 != 0) or sample_input % 400 == 0:
    print("Leap")
else:
    print("Ordinary")
