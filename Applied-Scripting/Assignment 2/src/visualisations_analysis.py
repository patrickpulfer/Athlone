import matplotlib.pyplot as plt


def square_root_rule_bins(data):
    """ Calculates the square root of the list of numbers to determine
        the optimal bin size for the histogram

    Args:
        data (list): List of data, ex. list of GWh 

    Returns:
        int: returns optimal bin numbers
    """
    n = len(data)
    num_bins = int(n ** 0.5)

    return num_bins


def getHistogramPlots(renewable_list, nonRenewable_list):
    """ Creates three separate histogram graphs to show histograms about renewable
        vs non-renewable sources by using the Mathplotlib moodule.

    Args:
        renewable_list (list): List of monthly renewable GWh usage
        nonRenewable_list (list): List of monthly non-renewable GWh usage
    """
    square_root_bins = square_root_rule_bins(nonRenewable_list)

    fig = plt.figure(figsize=(15,10))
    fig.suptitle('Histograms for Renewable vs. Non-renewable energy sources in Ireland')

    gs = fig.add_gridspec(2,2)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[1, :])

    ax1.hist(renewable_list, bins=square_root_bins, color='green', alpha=0.5, ec="black")
    ax1.set_title('Renewable Energy Sources')
    ax1.set_ylabel('Months')
    ax1.set_xlabel('Gigawatt-Hour (GWh)')

    ax2.hist(nonRenewable_list, bins=square_root_bins, color='red', alpha=0.5, ec="black")
    ax2.set_title('Non-renewable Energy Sources')
    ax2.set_ylabel('Months')
    ax2.set_xlabel('Gigawatt-Hour (GWh)')

    ax3.hist(renewable_list, bins=square_root_bins, color='green', alpha=0.5, ec="black")
    ax3.set_title('Non-renewable Energy Sources')
    ax3.set_ylabel('Months')
    ax3.set_xlabel('Gigawatt-Hour (GWh)')

    ax3.hist(nonRenewable_list, bins=square_root_bins, color='red', alpha=0.5, ec="black")
    ax3.set_title('Renewable vs Non-renewable Energy Sources')
    ax3.set_ylabel('Months')
    ax3.set_xlabel('Gigawatt-Hour (GWh)')

    plt.show()


def getBoxPlots(renewable_list, nonRenewable_list):
    """Creates two separate box plots graphs about renewable
        vs non-renewable sources by using the Mathplotlib moodule.

    Args:
        renewable_list (list): List of monthly renewable GWh usage
        nonRenewable_list (list): List of monthly non-renewable GWh usage
    """
    fig, axs = plt.subplots(1,2, figsize=(15,10))
    fig.suptitle('Box plots for Renewable vs. Non-renewable energy sources')

    axs[0].set_title('Renewable Energy Sources')
    axs[0].boxplot(renewable_list, showmeans=True, meanline=True)
    axs[0].set_ylabel('Gigawatt-Hour (GWh)')

    axs[1].set_title('Non-renewable Energy Sources')
    axs[1].boxplot(nonRenewable_list, showmeans=True, meanline=True)
    axs[1].set_ylabel('Gigawatt-Hour (GWh)')

    plt.show()


def getScatterPlots(renewable_list, nonRenewable_list):
    """Creates a single scatter box graph from the renewable and non-renewable data sources
        by using the Mathplotlib moodule.

    Args:
        renewable_list (list): List of monthly renewable GWh usage
        nonRenewable_list (list): List of monthly non-renewable GWh usage
    """
    fig, axs = plt.subplots(1,1, figsize=(15,10))
    fig.suptitle('Scatter plots for all renewable energy sources')

    plt.scatter(renewable_list, nonRenewable_list)
    plt.show()