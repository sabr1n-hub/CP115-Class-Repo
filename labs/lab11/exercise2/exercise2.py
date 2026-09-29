score = int(input())
total_a =0
total_b =0
turn=1
while score !=-1:
      if turn % 2 !=0:
            total_a += score   
      else:
           total_b += score
      turn += 1
      score = int(input())
      if total_a > total_b:
            winner = "A"
      elif total_b > total_a:
            winner ="B"
      else:
            winner ="Tie"

print(total_a)
print(total_b)
print(winner)
