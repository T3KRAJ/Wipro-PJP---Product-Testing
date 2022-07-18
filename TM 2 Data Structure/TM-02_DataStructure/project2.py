# Tek Raj Joshi
# Superset ID: 1368453

sample_scores = [2,3,6,6,5]
max_score = max(sample_scores)
while max_score in sample_scores:
    sample_scores.remove(max_score)

print(max(sample_scores))