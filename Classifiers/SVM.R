cat("\014")  #Clear Console
setwd("C:\\Users\\manu\\Desktop\\ML")  #Setting working dir

#Getting data into dataframes
conditions <- read.table("Knowledge Modeling Train.txt",header = T)  
conditions_test <- read.table("Knowledge Modeling Test.txt",header = T)

#Shuffle rows
conditions[sample(nrow(conditions)),]  
conditions_test[sample(nrow(conditions_test)),]  

training_features<-conditions[,-6] 
training_lables<-conditions[,6]  

test_features<-conditions_test[,-6]
test_lables<-conditions_test[,6]

library(kernlab)

rbf <- rbfdot(sigma=0.01)
SVM <- ksvm(UNS~.,data=conditions,type="C-bsvc",kernel=rbf,C=10,prob.model=TRUE)

poly <- polydot(degree = 1, scale = 2, offset = 1)
SVM <- ksvm(UNS~.,data=conditions,type="C-bsvc",kernel=poly,C=10,prob.model=TRUE)

tan_kernel <- tanhdot(scale = 1, offset = 1)
SVM <- ksvm(UNS~.,data=conditions,type="C-bsvc",kernel=tan_kernel,C=10,prob.model=TRUE)

vanilla_kernel <- vanilladot()
SVM <- ksvm(UNS~.,data=conditions,type="C-bsvc",kernel=vanilla_kernel,C=10,prob.model=TRUE)

bessel <- besseldot(sigma = 1, order = 1, degree = 1)
SVM <- ksvm(UNS~.,data=conditions,type="C-bsvc",kernel=bessel,C=10,prob.model=TRUE)

fitted(SVM)

svm_predict<-predict(SVM, training_features, type="probabilities")
y<-colnames(svm_predict)[apply(svm_predict,1,which.max)]
mean(y == training_lables)

svm_predict_test<-predict(SVM, test_features, type="probabilities")
y_test<-colnames(svm_predict)[apply(svm_predict_test,1,which.max)]
mean(y_test == test_lables)

training_lables
svm_predict_test
svm_predict
dim(predict(SVM, training_features, type="probabilities"))
y
y_test