import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('bin.txt')  #
plt.imshow(data, cmap='gray')
plt.axis(False)
plt.savefig('flag.png')
plt.show()
plt.close()
