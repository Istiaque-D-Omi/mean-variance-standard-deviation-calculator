import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')
  else:
    a = np.array(list)
    b = a.reshape(3, 3)
    
    mean1=np.mean(b, axis=0).tolist()
    mean2=np.mean(b, axis=1).tolist()
    mean3=np.mean(b)

    
    var1=np.var(b, axis=0).tolist()
    var2=np.var(b, axis=1).tolist()
    var3=np.var(b)

    
    std1=np.std(b, axis=0).tolist()
    std2=np.std(b, axis=1).tolist()
    std3=np.std(b)

    
    max1=np.amax(b, axis=0).tolist()
    max2=np.amax(b, axis=1).tolist()
    max3=np.amax(b)

    
    min1=np.amin(b, axis=0).tolist()
    min2=np.amin(b, axis=1).tolist()
    min3=np.amin(b)

    
    sum1=np.sum(b, axis=0).tolist()
    sum2=np.sum(b, axis=1).tolist()
    sum3=np.sum(b)

  
  
    calculation={'mean':[mean1,mean2,mean3],
    'variance':[var1,var2,var3],
    'standard deviation':[std1,std2,std3],
    'max':[max1,max2,max3],
    'min':[min1,min2,min3],
    'sum':[sum1,sum2,sum3]
    }
  


  return calculation
