import matplotlib.pyplot as plt

"""
mpl_earthquakes.py
"""
magnitudes = []
with open("earthquakes_Oct_2023.csv") as data_file:
    data_file.readline()
    
    for line in data_file:
        time_string, latitude, longitude, depth, magnitude = line.split(",")        
        magnitudes.append(float(magnitude))
"""
end of mpl_earthquakes.py
"""


fig, axs = plt.subplots(1,3, figsize=(15,10))
fig.suptitle('Visualizations of Earthquake Magnitudes')

print(magnitudes)

# Histogram
bins = range(int(max(magnitudes)+2))
axs[0].hist(magnitudes, bins=bins, ec="black")
axs[0].set_title('Histogram')
axs[0].set_ylabel('Magnitudes')

# Box Plot
axs[1].set_title('Box Plot')
axs[1].boxplot(magnitudes, showmeans=True, meanline=True)
axs[1].set_ylabel('Magnitudes')

# Violin Plot
axs[2].set_title('Violin Plot')
axs[2].violinplot(magnitudes, showmeans=True)
axs[2].set_ylabel('Magnitudes')

plt.show()
fig.savefig("exercise1.png")