import pandas as pd
import matplotlib.pyplot as plt

numbers = pd.DataFrame([10000, 2345, 620, 485, 135, 80, 55, 25, 5, 0])
numbers.plot()

plt.xlabel("iterations")
plt.ylabel("remainders")
plt.show()
