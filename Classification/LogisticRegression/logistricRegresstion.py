import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sqlalchemy import false

data1 = np.arange(10).reshape(-1, 1)
data2 = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1, ])
print(data1, data2)

# model
LogisticModel = LogisticRegression(
    solver='liblinear', C=10.0, random_state=0).fit(data1, data2)
print(LogisticModel.classes_)
print(LogisticModel.intercept_)
print(LogisticModel.predict_log_proba(data1))
logisticData = LogisticModel.predict(data1)
cm = confusion_matrix(data2, logisticData)
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(cm)
ax.grid(false)
ax.xaxis.set(ticks=(0, 1), ticklabels=('p1', 'p2'))
ax.yaxis.set(ticks=(0, 1), ticklabels=('a1', 'a2'))
ax.set_ylim(1.5, -0.5)
for i in range(2):
    for j in range(2):
        ax.text(j, i, cm[i, j], ha='center', va='center', color='red')
plt.show()
print(classification_report(data2, logisticData))
