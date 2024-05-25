import matplotlib.pyplot as plt
import numpy as np

# Generate random data
data = [np.random.randn(100) for _ in range(4)]

# Create the box plot
plt.boxplot(data)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Box Plot')
plt.show()
