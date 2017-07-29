from sklearn import tree
from sklearn import neighbors
from sklearn import svm 

#height,weight,shoesize
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

test_sample = [180,80,40]


#1 Decision Tree Classifier being used here 
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
prediction = clf.predict(test_sample)
print prediction


#2 k nearest neighbor classification 
clf = neighbors.KNeighborsClassifier()
clf = clf.fit(X,Y)
prediction = clf.predict(test_sample)
print prediction


#3 linear SVM
clf = svm.SVC(kernel='linear')
clf = clf.fit(X,Y)
prediction = clf.predict(test_sample)
print prediction