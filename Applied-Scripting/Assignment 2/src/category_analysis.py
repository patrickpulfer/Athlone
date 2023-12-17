

def getDistincSubCategories(dictionary):
    """Calculates the lenght of the lists inside the dictionary

    Args:
        dictionary (dictionary): Dictionary generated from the csv file

    Returns:
        int: Number of Sub-categories in dictionary
    """
    numberDistincSubCategories = len(dictionary.keys())

    return numberDistincSubCategories


def getHighestSubCategory(dictionary):
    """ Calculates the highest number within the sub-categories, by comparing values until the highest is recorded.
        The function will check if the values are numerical and not a year.

    Args:
        dictionary (dictionary): Dictionary generated from the csv file

    Returns:
        list: List of sub-category name and its value
    """
    HighestSubCategoryValue = 0
    HighestSubCategoryKey = None

    for key, value in dictionary.items():
        if type(value[0]) == int or type(value[0]) == float:
            if key != 'Year of Period':
                max_value_in_list = max(value)
                if max_value_in_list > HighestSubCategoryValue:
                    HighestSubCategoryValue = max_value_in_list
                    HighestSubCategoryKey = key
    result = [HighestSubCategoryKey, HighestSubCategoryValue]

    return result


def getLowestSubCategory(dictionary):
    """ Calculates the lowest number within the sub-categories, by first getting the highest number
        from getHighestSubCategory function and comparing lower values until the lowest is recorded.
    Args:
        dictionary (dictionary): Dictionary generated from the csv file

    Returns:
        list: List of sub-category name and its value
    """
    LowestSubCategoryValue = getHighestSubCategory(dictionary)[1]
    LowestSubCategoryKey = None

    for key, value in dictionary.items():
        if type(value[0]) == int or type(value[0]) == float:
            if key != 'Year of Period':
                min_value_in_list = min(value)
                if min_value_in_list < LowestSubCategoryValue:
                    LowestSubCategoryValue = min_value_in_list
                    LowestSubCategoryKey = key
    result = [LowestSubCategoryKey, LowestSubCategoryValue]

    return result


def getHighestTotalSubCategory(dictionary):
    """ Calculatest the highest total number within the sub-categories. 
        The function will also create a new dictionary if you want to return it.

    Args:
        dictionary (dictionary): Dictionary generated from the csv file

    Returns:
        list: List of highest total sub-category name and its value
    """
    total_subcategories = {}
    highestTotalKey = None
    highestTotalValue = 0

    for key, value in dictionary.items():
        total_subcategories.update({ key : sum(value) })

    print(total_subcategories)

    for key, value in total_subcategories.items():
        if key != 'Year of Period':
            max_total_value_in_list = value
            if max_total_value_in_list > highestTotalValue:
                highestTotalValue = max_total_value_in_list
                highestTotalKey = key
    result = [highestTotalKey, highestTotalValue]

    return result


def getLowestTotalSubCategory(dictionary):
    total_subcategories = {}
    lowestTotalKey = None
    lowestTotalValue = getHighestTotalSubCategory(dictionary)[1]

    for key, value in dictionary.items():
        total_subcategories.update({ key : sum(value) })

    print(total_subcategories)

    for key, value in total_subcategories.items():
        if key != 'Year of Period':
            min_total_value_in_list = value
            if min_total_value_in_list < lowestTotalValue:
                lowestTotalValue = min_total_value_in_list
                lowestTotalKey = key
    result = [lowestTotalKey, lowestTotalValue]

    return result


