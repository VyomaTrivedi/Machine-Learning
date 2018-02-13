#cat("\014")  #Clear Console

#setwd("C:/Users/manu/Desktop/ML/Assignment3")

args = commandArgs(trailingOnly=TRUE)
if (length(args)!=2) {
  stop("2 arguments must be supplied (training file, testing file)", call.=FALSE)
}

conditions = read.table(args[1],header = T)
conditions_label = conditions[,ncol(conditions)]  #Taking label from train data
conditions_test = read.table(args[2],header = T)

num_cols <- ncol(conditions)
num_rows <- nrow(conditions)

#c0 <- 0
#total 0 classes
#for (i in 1:num_rows) 
#  {
#  if (conditions[i,names(conditions)[num_cols]]==0) {
#  inc(c0) <- 1
#    
#  }
#}
#c0
#c1 <-0
##total 1 classes
#for (i in 1:num_rows) {
#  if (conditions[i,names(conditions)[num_cols]]==1) {
#    inc(c1)<-1
#  }
#}
#c1

label_level <- length(table(conditions_label))
s<-table(conditions_label)
num_of_attr <- num_cols-1
vector0=c()

for (k in 1:label_level)  {
  cat("P(",names(conditions)[num_cols],"=",unique(conditions_label)[k],") =", s[k]/num_rows," ")
      for (j in 1:num_of_attr)  {
        for (i in 1:nrow(unique(conditions[j])))  {
          q1<-(conditions[conditions_label == unique(conditions_label)[k], ])
          q4=sort(sapply(conditions[j], function(x) unique(x)))
          q2<-nrow(q1[q1[j] == q4[i],])
          q3<-q2/s[k]
          vector0=append(vector0,q3)
          cat("P(",names(conditions)[j],"=",q4[i],"|",unique(conditions_label)[k],") =", q3,"    ")
        }
      }
  cat("\n\n")
}

conditions_features <- conditions[,-num_cols]
conditions_test_features <- conditions_test[,-num_cols]

conditions_label <- conditions[,num_cols]
conditions_test_label <- conditions_test[,num_cols]

library(e1071)

NB_model <- naiveBayes(as.factor(conditions_label) ~.,data=conditions_features)

NB_pred_traindata <- predict(NB_model, conditions)
nmean <- mean(NB_pred_traindata == conditions_label) #Training accuracy
accuracy <-nmean * 100
cat("Training accuracy :",accuracy)
cat("\n")
NB_pred_testdata <- predict(NB_model, conditions_test)
nmean <- mean(NB_pred_testdata == conditions_test_label)  #Testing accuracy
taccuracy <-nmean * 100
cat("Testing accuracy :",taccuracy)