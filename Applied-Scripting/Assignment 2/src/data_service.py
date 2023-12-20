import sys

def csv_to_dictionary(filename):
    """Function to import data from a CSV file and process it for consumption readiness

    Args:
        filename (string): Name of the File

    Returns:
        _type_: Dictionary with the data from the CSV file
    """

    headers = []
    year_of_Period = []
    month_of_Period = []
    coal = []
    combust_Renew = []
    hydro = []
    natural_Gas = []
    oil = []
    other = []
    peatAnDBM = []
    solar_Farms = []
    wastes = []
    wind = []

    try:
        with open(filename, 'r') as file:
            headers = file.readline()
            for line in file.readlines():
                line = line.rstrip("\n").split(",")
                year_of_Period.append(int(line[0]))
                month_of_Period.append(line[1])
                coal.append(int(line[3]))
                combust_Renew.append(int(line[4]))
                hydro.append(int(line[5]))
                natural_Gas.append(int(line[6]))
                oil.append(int(line[7]))
                other.append(int(line[8]))
                peatAnDBM.append(int(line[9]))
                solar_Farms.append(int(line[10]))
                wastes.append(int(line[11]))
                wind.append(int(line[12]))

                monthly_Electricity_Data_Ireland_in_GWh_Dictionary = {
                    "Year of Period" : year_of_Period,
                    "Month of Period" : month_of_Period,
                    "Coal" : coal,
                    "Combust Renew" : combust_Renew,
                    "Hydro" : hydro,
                    "Natural Gas" : natural_Gas,
                    "Oil" : oil,
                    "Other" : other,
                    "Peat and DBM" : peatAnDBM,
                    "Solar Farms" : solar_Farms,
                    "Wastes" :wastes,
                    "Wind" : wind,
                }
        return monthly_Electricity_Data_Ireland_in_GWh_Dictionary;

    except FileNotFoundError:
        print("Data Source file not found: " + data_source_file_name)
        sys.exit()



def combine_renewable_vs_nonrenewable_sources(dictionary):
    """Function to combine renewable and non-renewable energy sources

    Args:
        dictionary (dictionary): Dictionary from the csv_to_dictionary function

    Returns:
        dictionary: Renewables vs Non-reneables data
    """
    
    renewable = []
    nonrenewable = []
    i = 0
    
    list_size = len(dictionary['Year of Period'])

    for i in range(list_size):
        renewable.append( dictionary['Hydro'][i]
                         +dictionary['Solar Farms'][i]
                         +dictionary['Wind'][i])
        nonrenewable.append( dictionary['Coal'][i] 
                            +dictionary['Combust Renew'][i] 
                            +dictionary['Natural Gas'][i]
                            +dictionary['Oil'][i] 
                            +dictionary['Other'][i] 
                            +dictionary['Peat and DBM'][i]
                            +dictionary['Wastes'][i]
                            )

    monthly_Renewables_vs_Nonrenewable = {
        "Year of Period" : dictionary['Year of Period'],
        "Month of Period" : dictionary['Year of Period'],
        "Renewable" : renewable,
        "Non-renewable" : nonrenewable,
    }

    return monthly_Renewables_vs_Nonrenewable


def combine_sources_by_year(dictionary):
    """Functions to combine monthly energy sources into yearly

    Args:
        dictionary (dictionary): Dictionary from the csv_to_dictionary function

    Returns:
        dictionary: Yearly energy sources dictionary
    """
    list_of_years = dictionary['Year of Period']
    year_of_Period = []
    coal = []
    combust_Renew = []
    hydro = []
    natural_Gas = []
    oil = []
    other = []
    peatAnDBM = []
    solar_Farms = []
    wastes = []
    wind = []

    i = 0
    list_size = len(dictionary['Year of Period'])

    for i in range(list_size):
        if year_of_Period.count( dictionary['Year of Period'][i] ) == 0:
            year_of_Period.append( dictionary['Year of Period'][i] )
            coal.append( dictionary['Coal'][i] )
            combust_Renew.append( dictionary['Combust Renew'][i] )
            hydro.append( dictionary['Hydro'][i] )
            natural_Gas.append( dictionary['Natural Gas'][i] )
            oil.append( dictionary['Oil'][i] )
            other.append( dictionary['Other'][i] )
            peatAnDBM.append( dictionary['Peat and DBM'][i] )
            solar_Farms.append( dictionary['Solar Farms'][i] )
            wastes.append( dictionary['Wastes'][i] )
            wind.append( dictionary['Wind'][i] )
        else:
            index = year_of_Period.index( dictionary['Year of Period'][i] ) #2

            coal[index] = coal[index] + dictionary['Coal'][i]
            combust_Renew[index] = combust_Renew[index] + dictionary['Combust Renew'][i]
            hydro[index] = hydro[index] + dictionary['Hydro'][i]
            natural_Gas[index] = natural_Gas[index] + dictionary['Natural Gas'][i]
            oil[index] = oil[index] + dictionary['Oil'][i]
            other[index] = other[index] + dictionary['Other'][i]
            peatAnDBM[index] = peatAnDBM[index] + dictionary['Peat and DBM'][i]
            solar_Farms[index] = solar_Farms[index] + dictionary['Solar Farms'][i]
            wastes[index] = wastes[index] + dictionary['Wastes'][i]
            wind[index] = wind[index] + dictionary['Wind'][i]

    combine_sources_by_year = {
        "Year of Period" : year_of_Period,
        "Coal" : coal,
        "Combust Renew" : combust_Renew,
        "Hydro" : hydro,
        "Natural Gas" : natural_Gas,
        "Oil" : oil,
        "Other" : other,
        "Peat and DBM" : peatAnDBM,
        "Solar Farms" : solar_Farms,
        "Wastes" :wastes,
        "Wind" : wind,
    }

    return combine_sources_by_year
