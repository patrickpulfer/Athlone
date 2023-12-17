import matplotlib.pyplot as plt

"""
mpl_webservers.py
"""
data = {}
with open("webservers_202310.csv") as data_file:   
    _ = data_file.readline()
    for line in data_file:
        developer, share = line.split(",")
        data[developer] = float(share)

remaining = 100 - sum(data.values())
data["Others"] = remaining

"""
end of mpl_webservers.py
"""

fig, axs = plt.subplots(1,1, figsize=(15,10))
fig.suptitle('Exercise 2')

axs.pie(data.values(),labels=data.keys(),autopct="%.f%%")
axs.set_title('Web Server Market Share, October 2023')

plt.show()
fig.savefig("exercise2.png")