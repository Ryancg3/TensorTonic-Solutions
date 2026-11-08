again important to keep the dims. and to remove zeros from the denominator. because if std is zero or close to zero (&lt;eps) then that mean that all datapoints in X are very close to the mean. thus X - mean are close to zero. 



havent check if this is robust in all cases. also what behavoir do we wnat when all datapoints are super close to mean anyhow.