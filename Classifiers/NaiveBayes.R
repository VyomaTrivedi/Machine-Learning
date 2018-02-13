cat("\014")  #Clear Console
setwd("C:\\Users\\manu\\Desktop\\ML")  #Setting working dir

conditions <- read.table("Knowledge Modeling Train.txt",header = T)  
conditions_test <- read.table("Knowledge Modeling Test.txt",header = T)

conditions_features <- conditions[,-6]
conditions_test_features <- conditions_test[,-6]

conditions_label <- conditions[,6]
conditions_test_label <- conditions_test[,6]

library(e1071)

NB_model <- naiveBayes(as.factor(conditions_label) ~.,data=conditions_features)

NB_pred_traindata <- predict(NB_model, conditions)
NB_pred_testdata <- predict(NB_model, conditions_test)

mean(NB_pred_traindata == conditions_label) #Training accuracy
mean(NB_pred_testdata == conditions_test_label)  #Testing accuracy

table(predict(NB_model, conditions))