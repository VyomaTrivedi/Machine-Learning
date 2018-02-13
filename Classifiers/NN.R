cat("\014")  #Clear Console
setwd("C:\\Users\\manu\\Desktop\\ML")  #Setting working dir

conditions <- read.table("Knowledge Modeling Train.txt",header = T)  
conditions_test <- read.table("Knowledge Modeling Test.txt",header = T)

conditions_test_label <- conditions_test[,6]

library(neuralnet)
nn_model = neuralnet(UNS ~ STG+SCG+STR+LPR+PEG,data=conditions,hidden=c(2),err.fct="sse",threshold = 0.001,rep = 5) #Error = 5.84
nn_model = neuralnet(UNS ~ STG+SCG+STR+LPR+PEG,data=conditions,hidden=c(4),err.fct="sse",threshold = 0.01,rep = 25) #Error = 2.5
nn_model = neuralnet(UNS ~ STG+SCG+STR+LPR+PEG,data=conditions,hidden=c(8),err.fct="sse",threshold = 0.001,rep = 25) #Error = 
plot(nn_model,rep="best") 
