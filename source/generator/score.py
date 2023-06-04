import random

def get_score(num_results):
    mean = 6.5
    std_dev = 1.5
    scores = [round(random.normalvariate(mean, std_dev), 2) for _ in range(num_results)]

    if num_results >= 1:
        for i in range(1, num_results):
            adjustment = random.uniform(-2, 2)
            scores[i] = round(scores[i-1] + adjustment, 2)
            scores[i] = max(0, min(10, scores[i]))  # Ensures scores are within 0-10 range
    else:
        scores = [max(0, min(10, score)) for score in scores]  # Ensure single score is within 0-10 range

    return scores


