import os
import basic_analysis, visualisations_analysis, category_analysis, category_visualisations


def main_menu(monthly_Electricity_Data_Ireland_in_GWh, monthly_Renewables_vs_Nonrenewable_in_Gwh, combine_sources_by_year):
    while True:
        os.system('clear')
        print("")
        print("")
        print("Exploratory Data Analysis")
        print("")
        print(r" ____        _             _                _           _      ")
        print(r"|  _ \  __ _| |_ __ _     / \   _ __   __ _| |_   _ ___(_)___  ")
        print(r"| | | |/ _` | __/ _` |   / _ \ | '_ \ / _` | | | | / __| / __| ")
        print(r"| |_| | (_| | || (_| |  / ___ \| | | | (_| | | |_| \__ \ \__ \ ")
        print(r"|____/ \__,_|\__\__,_| /_/   \_\_| |_|\__,_|_|\__, |___/_|___/ ")
        print(r"                                              |___/            ")
        print("")
        print("---------------------------------------------------------------")
        print("Select an Option")
        print("")
        print("1. Analysis of renewable vs. non-renewable energy sources")
        print("2. Visualitation analysis of renewable vs. non-renewable energy sources")
        print("3. Analysis by Category")
        print("3. Visualitation analysis by Category")
        print("Q. Quit")
        print("---------------------------------------------------------------")
        choice = input("Please make a choice: >> ")
        match choice:
            case "q":
                break;
            case "1":
                submenu_Basic_Analysis(monthly_Renewables_vs_Nonrenewable_in_Gwh)
            case "2":
                submenu_Visualisation_Analysis(monthly_Renewables_vs_Nonrenewable_in_Gwh)
            case "3":
                submenu_Analyse_by_Category(combine_sources_by_year)
            case "4":
                submenu_Visualisation_by_Category(combine_sources_by_year)


def submenu_Basic_Analysis(dictionary):  
    while True:
        print("")
        print("")
        print("1. Calculate Number & Total")
        print("2. Calculate the Mean")
        print("3. Calculate the Median")
        print("4. Calculate the Mode")
        print("5. Calculate the Maximum & Minimum")
        print("6. Calculate the Range and Interquartile Range")
        print("7. Calculate the Standard Deviation")
        print("8. Calculate the Pearson and Alternative Mode Skewness")
        print("9. Calculate the Correlation Coefficient between renewable and non-renewable")
        print("B. Back")
        print("---------------------------------------------------------------")  
        choice = input("Please make a choice: >> ")
        match choice:
            case "b":
                break
            case "1":
                result = basic_analysis.getNumberOfValues(dictionary['Renewable'])
                print(f"\n  Number of Renewable items: {result}")
                result = basic_analysis.getNumberOfValues(dictionary['Non-renewable'])
                print(f"  Number of Non-renewable items: {result}")
                result = basic_analysis.getTotal(dictionary['Renewable'])
                print(f"  Total GWh of Renewables: {result}")
                result = basic_analysis.getTotal(dictionary['Non-renewable'])
                print(f"  Total GWh of Non-renewable: {result}")

            case "2":
                result = basic_analysis.getMean(dictionary['Renewable'])
                print(f"\n  Mean of Renewables GWh: {result:.2f}")
                result = basic_analysis.getMean(dictionary['Non-renewable'])
                print(f"  Mean of Non-renewable GWh: {result:.2f}")

            case "3":
                result = basic_analysis.getMedian(dictionary['Renewable'])
                print(f"\n  Median of Renewables GWh: {result}")
                result = basic_analysis.getMedian(dictionary['Non-renewable'])
                print(f"  Median of Non-renewable GWh: {result}")

            case "4":
                result = basic_analysis.getMode(dictionary['Renewable'])
                print(f"\n  Mode of Renewables GWh: {result}")
                result = basic_analysis.getMode(dictionary['Non-renewable'])
                print(f"  Mode of Non-renewable GWh: {result}")

            case "5":
                result = basic_analysis.getMaximum(dictionary['Renewable'])
                print(f"\n  Maximum GWh of Renewables: {result}")
                result = basic_analysis.getMinimum(dictionary['Renewable'])
                print(f"  Maximum GWh of Renewable: {result}")
                result = basic_analysis.getMaximum(dictionary['Non-renewable'])
                print(f"  Maximum GWh of Non-renewable: {result}")
                result = basic_analysis.getMinimum(dictionary['Non-renewable'])
                print(f"  Minimum GWh of Non-renewable: {result}")

            case "6":
                result = basic_analysis.getRange(dictionary['Renewable'])
                print(f"\n  Range GWh of Renewables: {result}")
                result = basic_analysis.getInterQuartileRange(dictionary['Renewable'])
                print(f"  Interquartile Range GWh of Renewables: {result}")
                result = basic_analysis.getRange(dictionary['Non-renewable'])
                print(f"  Range GWh of Non-renewable: {result}")
                result = basic_analysis.getInterQuartileRange(dictionary['Non-renewable'])
                print(f"  Interquartile Range GWh of Non-renewables: {result}")

            case "7":
                result = basic_analysis.getStandardDeviation(dictionary['Renewable'])
                print(f"  Standard Deviation GWh of Renewable: {result:.2f}")
                result = basic_analysis.getStandardDeviation(dictionary['Non-renewable'])
                print(f"  Standard Deviation GWh of Non-renewable: {result:.2f}")

            case "8":
                result = basic_analysis.getPearsonSkewness(dictionary['Renewable'])
                print(f"\n  Pearson Mode Skewness of Renewable: {result:.2f}")
                result = basic_analysis.getPearsonSkewness(dictionary['Non-renewable'])
                print(f"  Pearson Mode Skewness of Non-renewable: {result:.2f}")
                result = basic_analysis.getAlternative_Pearson_Mode_Skewness(dictionary['Renewable'])
                print(f"  Alternative Pearson Mode Skewness of Renewable: {result:.2f}")
                result = basic_analysis.getAlternative_Pearson_Mode_Skewness(dictionary['Non-renewable'])
                print(f"  Alternative Pearson Mode Skewness of Non-renewable: {result:.2f}")

            case "9":
                result = basic_analysis.getCorrelationOfRenewablesVsNonRenewables(dictionary['Renewable'], dictionary['Non-renewable'])
                print(f"\n  Correlation Coefficient between Renewables vs Non-renewables: {result:.2f}")

            case "b":
                break


def submenu_Visualisation_Analysis(dictionary):  
    while True:
        print("")
        print("")
        print("1. Generate Histograms for Renewable and Non-renewable sources")
        print("2. Generate Box plots for Renewable and Non-renewable sources")
        print("3. Generate Scatter plots for Renewable and Non-renewable sources")
        print("B. Back")
        print("---------------------------------------------------------------")  
        choice = input("Please make a choice: >> ")
        match choice:
            case "b":
                break
            case "1":
                result = visualisations_analysis.getHistogramPlots(dictionary['Renewable'], dictionary['Non-renewable'])
            case "2":
                result = visualisations_analysis.getBoxPlots(dictionary['Renewable'], dictionary['Non-renewable'])
            case "3":
                result = visualisations_analysis.getScatterPlots(dictionary['Renewable'], dictionary['Non-renewable'])


def submenu_Analyse_by_Category(dictionary):
    while True:
        print("")
        print("")
        print("1. Calculate the number of distinc subcategories")
        print("2. Calculate the highest value in the dataset ")
        print("3. Calculate the lowest value in the dataset")
        print("4. Calculate the highest total value in the dataset")
        print("5. Calculate the lowest total value in the dataset")
        print("B. Back")
        print("---------------------------------------------------------------")  
        choice = input("Please make a choice: >> ")
        match choice:
            case "b":
                break
            case "1":
                result = category_analysis.getDistincSubCategories(dictionary)
                print(f"\n  Number of sub-categories in dataset: {result}")
            case "2":
                result_list = category_analysis.getHighestSubCategory(dictionary)
                print(f"\n  Highest value is {result_list[1]} within the sub-category '{result_list[0]}'")
            case "3":
                result_list = category_analysis.getLowestSubCategory(dictionary)
                print(f"\n  Lowest value is {result_list[1]} within the sub-category '{result_list[0]}'")
            case "4":
                result_list = category_analysis.getHighestTotalSubCategory(dictionary)
                print(f"\n  Highest total value is {result_list[1]} within the sub-category '{result_list[0]}'")
            case "5":
                result_list = category_analysis.getLowestTotalSubCategory(dictionary)
                print(f"\n  Lowest total value is {result_list[1]} within the sub-category '{result_list[0]}'")


def submenu_Visualisation_by_Category(dictionary):
    while True:
        print("")
        print("")
        print("1. Generate Pie chart by categories")
        print("2. Generate Bar chart by categories")
        print("3. Generate Box plot by categories")
        print("B. Back")
        print("---------------------------------------------------------------")  
        choice = input("Please make a choice: >> ")
        match choice:
            case "b":
                break
            case "1":
                category_visualisations.generatePieChartByCategory(dictionary)
            case "2":
                category_visualisations.generateBarChartByCategory(dictionary)
            case "3":
                category_visualisations.generateBoxPlotsByCategory(dictionary)