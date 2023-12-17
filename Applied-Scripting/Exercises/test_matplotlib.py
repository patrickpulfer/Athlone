import matplotlib.pyplot as plt
import numpy as np


data = {
    "First": 1,
    "Second": 2,
}

values = [1,2,3,4,5]



fig, ax = plt.subplots(1,3)

fig.savefig("test.pdf")


plt.show()