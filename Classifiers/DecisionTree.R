cat("\014")  #Clear Console
setwd("C:\\Users\\manu\\Desktop\\ML")  #Setting working dir

conditions <- read.table("Knowledge Modeling Train.txt",header = T)  
conditions_test <- read.table("Knowledge Modeling Test.txt",header = T)

library(rpart)
library(rpart.plot)

rpart_tree_model <- rpart(UNS ~ ., data=conditions, method = "class")
rpart.plot(rpart_tree_model)
summary(rpart_tree_model)

predict_model <- predict(rpart_tree_model,conditions_test,type = "class")

conditions_UNS = conditions[,ncol(conditions)]  #Taking label from train data
conditions_test_UNS = conditions_test[,ncol(conditions_test)]  #Taking label from test data 

mean (predict_model == conditions_test_UNS) #Testing Accuracy
table(conditions_UNS[1:145], predict_model) #Confusion Matrix

predict_model
summary(predict_model)
summary(dec_tree)
dec_tree 
head(conditions)