import sys
sys.path.insert(0,'src') # Necessary to include our src folder. Else import won't recognize the init files. 

from src import menu, basic_analysis, data_service

""" Application to calculate and display various queries on Ireland's energy generation sources data contained in Monthly_Electricity_Data_Ireland.csv. 
    Once started, the application will display a menu which can be navigated.
"""


if __name__ == '__main__':
    """The Start of the Program
    """
    monthly_Electricity_Data_Ireland_in_GWh = {}
    monthly_Renewables_vs_Nonrenewable_in_Gwh = {}

    data_source_file_name = 'Monthly_Electricity_Data_Ireland.csv'


    monthly_Electricity_Data_Ireland_in_GWh = data_service.csv_to_dictionary(data_source_file_name)
    monthly_Renewable_vs_Nonrenewable_in_Gwh = data_service.combine_renewable_vs_nonrenewable_sources(monthly_Electricity_Data_Ireland_in_GWh)
    combine_sources_by_year = data_service.combine_sources_by_year(monthly_Electricity_Data_Ireland_in_GWh)

    menu.main_menu(monthly_Electricity_Data_Ireland_in_GWh, monthly_Renewable_vs_Nonrenewable_in_Gwh, combine_sources_by_year)

