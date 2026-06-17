



def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def is_outlier(value, mean, threshold=2.0):
    distance = abs(value - mean) / mean  # relative distance from mean
    return distance > threshold / 10     # normalize to a useful scale

# Use the default threshold
print(is_outlier(150, mean=87.6))        # True — 150 is far from mean

# Override with a stricter threshold
print(is_outlier(95, mean=87.6, threshold=5))  # False — close enough

# Applied to a dataset
scores = [85, 92, 78, 95, 150, 88]  # 150 is suspicious
mean = calculate_average(scores)
outliers = [s for s in scores if is_outlier(s, mean, threshold=5)]
print(outliers)  # [150]