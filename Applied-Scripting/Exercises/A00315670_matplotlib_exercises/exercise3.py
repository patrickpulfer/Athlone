import matplotlib.pyplot as plt

"""
mpl_distrowatch.py
"""
distros_dict = {}

with open("distrowatch_2023.csv") as distrowatch_file:
    distrowatch_file.readline()
    for line in distrowatch_file:
        distro, hits_per_day  = line.split(",")
        distros_dict[distro] = int(hits_per_day)
    
"""
end of mpl_distrowatch.py
"""

print(distros_dict)


fig, axs = plt.subplots(1,1, figsize=(15,10))
fig.suptitle('Exercise 3')

axs.barh(list(distros_dict.keys()),distros_dict.values())

for index, value in enumerate(distros_dict.values()):
    axs.text(value,index,str(value))

axs.set_title('Most Popular Linux Distributions, 2021')
axs.set_ylabel('Distributions')
axs.set_xlabel('Hits per Day')


plt.show()
fig.savefig("exercise3.png")