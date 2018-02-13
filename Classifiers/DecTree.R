cat("\014")  #Clear Console
setwd("C:\\Users\\manu\\Desktop\\ML")  #Setting working dir

conditions <- read.table("Knowledge Modeling Train.txt",header = T)  
conditions_test <- read.table("Knowledge Modeling Test.txt",header = T)

conditions[sample(nrow(conditions)),] 
conditions_test[sample(nrow(conditions_test)),] 

library(tree)      

tree_model=tree(as.factor(UNS)~.,conditions)

plot(tree_model)  
text(tree_model,pretty=0)  

tree_pred_traindata = predict(tree_model,conditions,type ="class")
conditions_UNS = conditions[,ncol(conditions)]
mean (tree_pred_traindata == conditions_UNS) #Training Accuracy before pruning

tree_pred_traindata
conditions_UNS

tree_pred_testdata = predict(tree_model,conditions_test,type ="class")
conditions_test_UNS = conditions_test[,ncol(conditions_test)]
mean (tree_pred_testdata == conditions_test_UNS) #Testing Accuracy before pruning

tree_pred_testdata
conditions_test_UNS

set.seed(3)
cv_tree = cv.tree(tree_model,FUN = prune.misclass)  #Cross validation to check where to stop pruning
plot(cv_tree$size,cv_tree$dev,type="b")  #plot to see where dev is minimum

pruned_model = prune.misclass(tree_model,best = 10) #best = no.of leaf nodes to prune

plot(pruned_model)
text(pruned_model,pretty=0)  #To display text on the plot

tree_pred_traindata_prune = predict(pruned_model,conditions,type ="class")
mean (tree_pred_traindata_prune == conditions_UNS)  #Training accuracy post pruning

tree_pred_testdata_prune = predict(pruned_model,conditions_test,type ="class")
mean (tree_pred_testdata_prune == conditions_test_UNS)  #Testing accuracy post pruning