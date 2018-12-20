wd="/home/raphael/Downloads/"
library(rlist)
setwd(wd)
Jnana<-read.csv("list_files_Jnana.csv",na.string=c("","NA"),header=FALSE, stringsAsFactors=FALSE)
Ananda<-read.csv("list_files_Ananda.csv",na.string=c("","NA"),header=FALSE, stringsAsFactors=FALSE)
Copie<-Ananda
Original<-Jnana
print ("length of original")
print (dim(Original))
print ("length of copy")
print (dim(Copie))
result<-data.frame()
result_missing<-data.frame()
i<-0

for (filename in Original$V1){#fot each filename in original
        is_copied<-NULL
        i<-i+1
        #print(Original$V1)
        is_copied<-Copie[grep(filename,Copie$V1,fixed=TRUE) , ]
       # print ("filename")
        #print (filename)
        #print ("length of found files")
        #print (dim(is_copied)[1])
       
        if  (dim(is_copied)[1]>0){
                #print ("copied")
                #print (filename)
                filename_new<- paste0(Original$V2[i],"/",filename)
                result<-list.append(result, filename_new)
                }
        else{
                #print("missing")
               # print (filename)
                filename_new<- paste0(Original$V2[i],"/",filename)
                result_missing<-list.append(result_missing, filename_new)
        }
}
result2<-unlist(result)
result_missing<-unlist(result_missing)
write.csv(file="list_copied.csv",result2)
write.csv(file="list_missing.csv",result_missing)
#removed pratique du don et limite