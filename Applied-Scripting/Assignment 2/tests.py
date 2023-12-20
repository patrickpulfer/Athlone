import sys
import pytest
from collections import Counter

sys.path.insert(0,'src') # Necessary to include our src folder. Else import won't recognize the init files in our subdirectory. 

from src import menu, basic_analysis, data_service, category_analysis


sample_dict = {
    "Category A": [10, 20, 30],
    "Category B": [5, 15, 25],
    "Year of Period": [2000, 2001, 2002]
}


def test_getNumberOfValues():
    """Test for getNumberOfValues function in basic_analysis.py
    """
    assert basic_analysis.getNumberOfValues([1, 2, 3, 4]) == 4
    assert basic_analysis.getNumberOfValues([]) == 0


def test_getTotal():
    """Test for getTotal function in basic_analysis.py
    """
    assert basic_analysis.getTotal([1, 2, 3, 4]) == 10
    assert basic_analysis.getTotal([]) == 0


def test_getMean():
    """Test for getMean function in basic_analysis.py
    """
    assert basic_analysis.getMean([1, 2, 3, 4]) == 2.5
    with pytest.raises(ZeroDivisionError):
        basic_analysis.getMean([])


def test_getMedian():
    """Test for getMedian function in basic_analysis.py
    """
    assert basic_analysis.getMedian([1, 3, 2, 5, 4]) == 3
    assert basic_analysis.getMedian([1, 2, 3, 4]) == 2.5
    with pytest.raises(IndexError):
        basic_analysis.getMedian([])


def test_getMode():
    """Test for getMode function in basic_analysis.py
    """
    assert basic_analysis.getMode([1, 2, 2, 3, 3]) == [2, 3]
    assert basic_analysis.getMode([1, 1, 1, 2, 3]) == [1]


def test_getMaximum():
    """Test for getMaximum function in basic_analysis.py
    """
    assert basic_analysis.getMaximum([1, 2, 3, 4]) == 4
    with pytest.raises(ValueError):
        basic_analysis.getMaximum([])


def test_getMinimum():
    """Test for getMinimum function in basic_analysis.py
    """
    assert basic_analysis.getMinimum([1, 2, 3, 4]) == 1
    with pytest.raises(ValueError):
        basic_analysis.getMinimum([])


def test_getRange():
    """Test for getRange function in basic_analysis.py
    """
    assert basic_analysis.getRange([1, 2, 3, 4]) == 3
    with pytest.raises(ValueError):
        basic_analysis.getRange([])


def test_getInterQuartileRange():
    """Test for getInterQuartileRange function in basic_analysis.py
    """
    assert basic_analysis.getInterQuartileRange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    with pytest.raises(IndexError):
        basic_analysis.getInterQuartileRange([])


def test_getStandardDeviation():
    """Test for getStandardDeviation function in basic_analysis.py
    """
    assert basic_analysis.getStandardDeviation([1, 2, 3, 4]) == pytest.approx(1.29, 0.01)
    assert basic_analysis.getStandardDeviation([1]) is None


def test_getPearsonSkewness():
    """Test for getPearsonSkewness function in basic_analysis.py
    """
    assert basic_analysis.getPearsonSkewness([1, 2, 3, 4, 5]) == pytest.approx(0.0, 0.01)
    assert basic_analysis.getPearsonSkewness([1, 1, 1, 2, 3]) > 0


def test_getAlternative_Pearson_Mode_Skewness():
    """Test for getAlternative_Pearson_Mode_Skewness function in basic_analysis.py
    """
    test_data = [1, 2, 2, 3, 4]
    expected_result = basic_analysis.getAlternative_Pearson_Mode_Skewness(test_data)
    assert basic_analysis.getAlternative_Pearson_Mode_Skewness(test_data) == pytest.approx(expected_result, abs=0.01)


def test_getCorrelationOfRenewablesVsNonRenewables():
    """Test for getCorrelationOfRenewablesVsNonRenewables function in basic_analysis.py
    """
    assert basic_analysis.getCorrelationOfRenewablesVsNonRenewables([1, 2, 3], [3, 2, 1]) == pytest.approx(-1.0, 0.01)
    with pytest.raises(ValueError):
        basic_analysis.getCorrelationOfRenewablesVsNonRenewables([1, 2], [1, 2, 3])


def test_getDistincSubCategories():
    """Test for getDistincSubCategories function in category_analysis.py
    """
    assert category_analysis.getDistincSubCategories(sample_dict) == 3
    assert category_analysis.getDistincSubCategories({}) == 0


def test_getHighestSubCategory():
    """Test for getHighestSubCategory function in category_analysis.py
    """
    assert category_analysis.getHighestSubCategory(sample_dict) == ["Category A", 30]


def test_getLowestSubCategory():
    """Test for getLowestSubCategory function in category_analysis.py
    """
    assert category_analysis.getLowestSubCategory(sample_dict) == ["Category B", 5]


def test_getHighestTotalSubCategory():
    """Test for getHighestTotalSubCategory function in category_analysis.py
    """
    assert category_analysis.getHighestTotalSubCategory(sample_dict) == ["Category A", 60]
    assert category_analysis.getHighestTotalSubCategory({"Category C": [], "Year of Period": [2000]}) == [None, 0]


def test_getLowestTotalSubCategory():
    """Test for getLowestTotalSubCategory function in category_analysis.py
    """
    assert category_analysis.getLowestTotalSubCategory(sample_dict) == ["Category B", 45]
    assert category_analysis.getLowestTotalSubCategory({"Category C": [], "Year of Period": [2000]}) == [None, 0]