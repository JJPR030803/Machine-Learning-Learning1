import numpy as np



noise = (np.random.random([15])*4)-2
feature = np.arange(6,21)
label = (feature*3)+4
label = label+noise
print(label)