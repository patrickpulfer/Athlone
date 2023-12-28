from collections import Counter


def getNumberOfValues(list):
    """Calculates the number of values in the list

    Args:
        list (list): The list of the data

    Returns:
        int: Number of Values
    """
    numberOfValues = len(list)

    return numberOfValues


def getTotal(list):
    """Calculates the sum of all data in the list

    Args:
        list (list): The list of the data

    Returns:
        int: Total of values
    """
    total = sum(list)

    return total


def getMean(list):
    """Calculates the mean of the data provided in the list

    Args:
        list (list): The list of the data

    Returns:
        float: Mean of the values
    """
    length = len(list)
    mean = sum(list) / length

    return mean


def getMedian(list):
    """Calculates the medium value of the list by sorting the list and finding the middle value

    Args:
        list (list): The list of the data

    Returns:
        int: Median value of the list
    """
    length = len(list)
    sorted_list = sorted(list)

    if length % 2 == 1:
        median = sorted_list[length // 2]
    else:
        middle1 = sorted_list[(length // 2) - 1]
        middle2 = sorted_list[length // 2]
        median = (middle1 + middle2) / 2.0

    return median


def getMode(list):
    """ Calculates the mode of a list by using a dictionary to count the frequency of each element in the list and then finding the element(s) with the highest frequency.

    Args:
        list (list): The list of the data

    Returns:
        list: The mode of the data (can be single of multiple values in the list)
    """
    mode_counter = {}

    for item in list:
        if item in mode_counter:
            mode_counter[item] += 1
        else:
            mode_counter[item] = 1

    max_count = max(mode_counter.values())
    mode = [key for key, value in mode_counter.items() if value == max_count]

    return mode


def getMaximum(list):
    """Calculates the maximum value present in the list

    Args:
        list (list): The list of the data

    Returns:
        int: Maximum value of list
    """
    maximum = max(list)

    return maximum



def getMinimum(list):
    """Calculates the minimum value present in the list

    Args:
        list (list): The list of the data

    Returns:
        int: Minimum value of list
    """
    minimum = min(list)

    return minimum


def getRange(list):
    """Calculates the range of a list subtracting the minimum from the maximum value.

    Args:
        list (list): The list of the data

    Returns:
        int: Range of the list
    """
    minimum = min(list)
    maximum = max(list)
    range_of_list = maximum - minimum

    return range_of_list


def getInterQuartileRange(list):
    """Calculates the Interquartile Range (IQR) of a list, by performing the following steps:
    1. Sorting the list in ascending order
    2. Calculating the first and third quartile
    3. Subtracting the first from third quartile

    Args:
        list (list): The list of the data

    Returns:
        float: The Interquartile Range (IQR of the list
    """
    length = len(list)
    sorted_list = sorted(list)

    if length % 2 == 0:
        lower_half = sorted_list[:length // 2]
        upper_half = sorted_list[length // 2:]
        Q1 = (lower_half[len(lower_half) // 2 - 1] + lower_half[len(lower_half) // 2]) / 2
        Q3 = (upper_half[len(upper_half) // 2 - 1] + upper_half[len(upper_half) // 2]) / 2
    else:
        lower_half = sorted_list[:length // 2]
        upper_half = sorted_list[length // 2 + 1:]
        Q1 = lower_half[len(lower_half) // 2]
        Q3 = upper_half[len(upper_half) // 2]
    interQuartileRange = Q3 - Q1

    return interQuartileRange


def getStandardDeviation(list):
    """Calculates the Standard Deviation of a list by performing the following steps:
    1. Calculating the mean value
    2. Calculating the squared difference between each element and the mean
    3. Calculating the variance as the average of the squared differences
    4. Finally, calculating the standard deviation as the square root of the variance

    Args:
        list (list): The list of the data

    Returns:
        float: The Standard Deviation of a list
    """
    if len(list) < 2:
        return None
    
    mean = sum(list) / len(list)
    squared_differences = [(x - mean) ** 2 for x in list]
    variance = sum(squared_differences) / (len(list) - 1)
    standard_deviation = variance ** 0.5

    return standard_deviation


def getPearsonSkewness(list):
    """Calculates the Pearson Mode Skewness.

    See https://en.wikipedia.org/wiki/Skewness#Pearson's_first_skewness_coefficient_(mode_skewness)

    Args:
        list (list): The list of the data

    Returns:
        float: The Skewness of the list
    """
    if len(list) < 2:
        return None
    
    mean = sum(list) / len(list)
    median = sorted(list)[len(list) // 2]
    std_deviation = (sum((x - mean) ** 2 for x in list) / (len(list) - 1)) ** 0.5
    pearson_skewness = 3 * (mean - median) / std_deviation

    return pearson_skewness


def getAlternative_Pearson_Mode_Skewness(list):
    """Calculates the Pearson Alternative Mode (or second skewness).

    See https://en.wikipedia.org/wiki/Skewness#Pearson's_second_skewness_coefficient_(median_skewness)

    Args:
        list (list): The list of the data

    Returns:
        float: The Skewness of the list
    """
    if len(list) < 2:
        return None
    
    mean = sum(list) / len(list)
    mode = max(Counter(list), key=Counter(list).get)
    std_deviation = (sum((x - mean) ** 2 for x in list) / (len(list) - 1)) ** 0.5
    
    alt_pearson_skewness = (mean - mode) / std_deviation

    return alt_pearson_skewness


def getCorrelationOfRenewablesVsNonRenewables(list1, list2):
    """Calculates the Correlation Coefficient between renewable and non-renewable list sources, 
    by first calculating the means of both lists, 
    then using the Pearson correlation formulate to compute the correlation.

    Args:
        list1 (list): List data from Renewable Sources
        list2 (list): List data from Non-renewable Sources

    Raises:
        ValueError: Check to ensure both lists have the same length

    Returns:
        float: Correlation Coefficient between renewable and non-renewable
    """
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length")

    length = len(list1)
    mean1 = sum(list1) / length
    mean2 = sum(list2) / length
    numerator = sum((list1[i] - mean1) * (list2[i] - mean2) for i in range(length))
    denominator1 = sum((list1[i] - mean1) ** 2 for i in range(length))
    denominator2 = sum((list2[i] - mean2) ** 2 for i in range(length))
    correlation = numerator / ((denominator1 * denominator2) ** 0.5)

    return correlation