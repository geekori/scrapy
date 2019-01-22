import matplotlib.pyplot as plt

# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics
import matplotlib
import matplotlib.pyplot as plt

# The digits dataset
digits = datasets.load_digits()


aa = datasets.load_mlcomp
print(aa)
X,Y = digits['data'],digits['target']
print(X.shape)
digit = X[21]
digit_image = digit.reshape(8,8)
print(Y[21])
plt.imshow(digit_image,cmap=matplotlib.cm.binary,interpolation='nearest')
plt.axis('off')

plt.show()