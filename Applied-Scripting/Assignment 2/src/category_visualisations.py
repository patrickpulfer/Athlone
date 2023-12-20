import matplotlib.pyplot as plt


def generatePieChartByCategory(dictionary):
    """Function to generate a Pie Chart with Matplotlib

    Args:
        dictionary (dictionary): Dictionary generated from the csv file
    """
    labels = []
    values = []
    
    for key, value in dictionary.items():
        if key != 'Year of Period':
            labels.append(key)
            values.append(sum(value))

    fig, ax = plt.subplots(figsize=(15,10))
    fig.suptitle('Gigawatt-Hour (GWh) generated by fuel source since 2010')
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.legend(shadow=True, fancybox=True, loc='center left')
    
    plt.show()


def generateBarChartByCategory(dictionary):
    """Function to generate a Bar Chart with Matplotlib

    Args:
        dictionary (dictionary): Dictionary generated from the csv file
    """
    labels = []
    values = []

    for key, value in dictionary.items():
        if key != 'Year of Period':
            labels.append(key)
            values.append(sum(value))

    fig, ax = plt.subplots(figsize=(15,10))
    fig.suptitle('Gigawatt-Hour (GWh) generated by fuel source since 2010')

    hbars = ax.barh(labels, values, label=labels, align='center')
    ax.bar_label(hbars, labels=[f'{v} GWh' for v in values])
    plt.show()


def generateBoxPlotsByCategory(dictionary):
    """Function to generate a Box Plot Chart with Matplotlib

    Args:
        dictionary (dictionary): Dictionary generated from the csv file
    """
    labels = []
    values = []
    
    for key, value in dictionary.items():
        if key != 'Year of Period':
            labels.append(key)
            values.append(value)

    fig, ax = plt.subplots(figsize=(15,10))
    fig.suptitle('Gigawatt-Hour (GWh) generated by fuel source since 2010')
    ax.boxplot(values, showmeans=True, meanline=True)
    ax.set_xticklabels(labels)

    plt.show()