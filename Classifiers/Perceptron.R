cat("\014")  #Clear Console
setwd("C:\\Users\\manu\\Desktop\\ML")  #Setting working dir

conditions <- read.table("Knowledge Modeling Train.txt",header = T)  
conditions_test <- read.table("Knowledge Modeling Test.txt",header = T)

conditions_test_label <- conditions_test[,6]

library(neuralnet)
nn_model = neuralnet(UNS ~ STG+SCG+STR+LPR+PEG,data=conditions,hidden=0,err.fct="sse",threshold = 0.00001,rep = 100)
plot(nn_model,rep="best")

library(caret)

# Method 1
my.grid <- expand.grid(.decay = c(0.5, 0.1), .size = c(10,10))
nn_model <- train(UNS ~ STG+SCG+STR+LPR+PEG, data = conditions,method = "nnet", maxit = 1000, tuneGrid = my.grid, trace = F, linout = 1)
perceptron_predict <- predict(nn_model, newdata = conditions_test)
perceptron_rmse <- sqrt(mean((perceptron_predict - conditions_test_label)^2))
perceptron_rmse

# Method 2
set.seed(7)
control <- trainControl(method="repeatedcv", number=10, repeats=3)
model <- train(UNS ~ STG+SCG+STR+LPR+PEG, data=conditions, method="nnet", trControl=control, tuneLength=5)
print(model)

