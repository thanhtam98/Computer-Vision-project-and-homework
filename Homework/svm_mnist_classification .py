import matplotlib.pyplot as plt
import numpy as np
import time
import datetime as dt
import matplotlib.pyplot as plt
import cv2
import glob

from sklearn import datasets, svm, metrics
from sklearn.datasets import fetch_mldata
from mnist_helpers import *
(images, targets) = datasets.load_digits(n_class=10, return_X_y=True)
show_some_digits(images,targets)

X_data = images/255.0
Y = targets

from sklearn.model_selection import train_test_split
X_train, _, y_train, _ = train_test_split(X_data, Y, test_size=0.2, random_state=42)


################ Classifier with good params ###########
# Create a classifier: a support vector classifier

param_C = 10
param_gamma = 0.05
classifier = svm.SVC(kernel = 'linear',C=param_C,gamma=param_gamma)

#We learn the digits on train part
start_time = dt.datetime.now()
print('Start learning at {}'.format(str(start_time)))
classifier.fit(X_train, y_train)
end_time = dt.datetime.now() 
print('Stop learning {}'.format(str(end_time)))
elapsed_time= end_time - start_time
print('Elapsed learning {}'.format(str(elapsed_time)))

test_image = cv2.imread('image/0-80.png')
test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
test_image = cv2.resize(test_image, (8,8))
test_image = test_image.reshape(-1,64)
X_test = test_image
y_test = [2]

for name in glob.glob('image/*.png'):
      test_image = cv2.imread(name)
      test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
      test_image = cv2.resize(test_image, (8,8))
      test_image = test_image.reshape(-1,64)
      X_test = np.append(X_test, test_image, axis=0)
      y_test = np.append(y_test, int(name[6]))
      
expected = y_test
predicted = classifier.predict(X_test)

show_some_digits(X_test,predicted,title_text="Predicted {}")

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
      
cm = metrics.confusion_matrix(expected, predicted)
print("Confusion matrix:\n%s" % cm)

plot_confusion_matrix(cm)

print("Accuracy={}".format(metrics.accuracy_score(expected, predicted)))


