#1st step: Import dependencies 

from sklearn import tree # import scikit tree from scikit learn



# [height, weight, shoe_size] dataset size is only 11 people

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

# Y is the lable , each lable is a gender and it's associated with the body matrix X(previous list)

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

# now we have our dataset ,now we want to store our variable to store our decision tree

clf = tree.DecisionTreeClassifier() #decision tree classifier

# now that we have tree variable, we can train our dataset.
# we will call the fit() method on the classifier variable which takes two arguments 

#will store our x andy variables as the arguments

clf = clf.fit(X, Y) #the fit() trains the decision tree on our  dataset 

#let's test it by classifying the gender of someone given a new list of body matrix

#variable to store the result,

#we will call the predict method of our decision tree to predict the gender given our three value in a list

prediction = clf.predict([[190, 70, 43]])

#then we can print the prediction 

print(prediction)