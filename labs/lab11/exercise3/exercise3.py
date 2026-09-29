number = int(input())
count =0
biggest_jump =0
prev_numb = 0
while number !=0:
    count+= 1
if prev_num < number:
    jump= number - prev_numb
if jump > biggest_jump:
    biggest_jump = jump
prev_numb = number
number = int(input())

print(count)
print(biggest_jump)
