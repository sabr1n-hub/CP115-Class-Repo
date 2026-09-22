num_rounds = int(input())
final_score =0
rounds_processed = 0
for score in range(num_rounds):
    score =float(input())
    if score > 100:
        score += score*0.20
    final_score += score
    rounds_processed += 1

print(f"{final_score:.1f}")
print(rounds_processed)
