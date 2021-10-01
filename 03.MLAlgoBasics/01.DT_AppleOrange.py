# -----------------------------------------------------------------
#In this example I'll introduce Machine Learning
# -----------------------------------------------------------------




# Import Scikit Learn: Tree Methods
# -----------------------------------------------------------------
from sklearn import tree

# -----------------------------------------------------------------
# Input Data 
# - Features (Xs)
# - Labels (y)
# -----------------------------------------------------------------
features = [[140,1],[130,1],[150,1],[170,0]] #Texture= Bumpy=0 and Smooth=1
labels = [0,0,1,1] # 0 for apple, 1 for orange

# -----------------------------------------------------------------
# Declare the Classifier
# -----------------------------------------------------------------
clf = tree.DecisionTreeClassifier()

# -----------------------------------------------------------------
# fit = find patterns in data
# Use what we declared to find patterns in data
# -----------------------------------------------------------------
clf = clf.fit(features, labels)

# -----------------------------------------------------------------
# Print the prediction
# -----------------------------------------------------------------
print('The decision tree classifier predicts: ', clf.predict([[150,0]])) # The decision tree classifier predicts:  [1]