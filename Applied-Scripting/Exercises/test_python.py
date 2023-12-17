from math import sqrt

def calc_mean(numbers):
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def calc_mode(numbers):
    if not numbers:
        return 0
    mode_count = max(numbers.count(number) for number in numbers)
    return min(number for number in numbers if numbers.count(number) == mode_count)

def calc_std_dev(numbers):
    if not numbers:
        return 0.0
    mean = calc_mean(numbers)
    squared_deviations = [(x - mean) ** 2 for x in numbers]
    variance = sum(squared_deviations) / (len(numbers) - 1)
    std_dev = sqrt(variance)
    return std_dev

def calc_mode_skewness(numbers):
    if not numbers:
        return 0.0
    mean = calc_mean(numbers)
    mode = calc_mode(numbers)
    std_dev = calc_std_dev(numbers)
    return (mean - mode) / std_dev



mean_result = calc_mean([7, 9, 5, 3])
print(f"{mean_result:.1f}")

"""

mean_result = calc_mean(list(range(1, 11)))
print(f"{mean_result:.1f}")


mode_result = calc_mode([6, 3, 9, 6, 6, 5, 9, 3])
print(f"{mode_result}")

mode_result = calc_mode([6, 3, 9, 6, 6, 5, 9, 3, 9])
print(f"{mode_result}")

std_dev_result = calc_std_dev([1, 2, 3, 4, 4, 5])
print(f"{std_dev_result:.2f}")

mode_skewness_result = calc_mode_skewness([1, 2, 3, 4, 4, 5])
print(f"{mode_skewness_result:.3f}")

mode_skewness_result = calc_mode_skewness([1, 2, 2, 3, 4, 5])
print(f"{mode_skewness_result:.3f}")

mode_skewness_result = calc_mode_skewness([1, 2, 2, 3, 3, 3, 4, 4, 5])
print(f"{mode_skewness_result:.3f}") 
"""