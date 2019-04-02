# binary-classifier


## Aim:
Devise an algorithm/technique to fool a binary classifier named target-classifier
+ The target-classifier is a binary classifier classifying data to two categories,  i.e. class-1 and class-0.

+ Classifiers' training data,  i.e. a sample of 540 paragraphs. 180 for class-1, and 360 for class-0, provided in the files: class-1.txt and class-0.txt respectively.

+ The target-classifier belong to the SVM family.

+ The target-classifier allows EXACTLY 20 DISTINCT modifications in each test sample.

+ Test sample of 200 paragraphs from class-1 (in the file: test_data.txt). Use these test samples to get feedback from the target classifier (only 15 attempts allowed to each group.).


## step 1: Data processing
Firstly , I use a dictionary to store the content in class0 and class1. words_dict ={key = every content (in class0 and 1)}
Then , change this dict to two list data_x and data_y . data_x contains every words in class0 and class1. data_y contains the times of every words in data_x.

## step 2: Choose SVM kernel
In this step ,I use data from step 1 to set up a training set and then choose a Support Vector Machine kernel.
Because in this project ,I have several eigenvalues , the linear kernel is chosen in the program.

## step 3: Update modified_data
The SVM classifier has eigenvalue weights , so I remove the word with high weights in class1 from modified_data.txt .

