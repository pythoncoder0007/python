#task-6
# Sort in Ascending Order
l1 = [2,5,3,4,6,7,9,4,5,8,1,33]
  
tem = 0;    
 
print("Elements of original list: ")   
for i in range(0, len(l1)): 
   print(l1[i], end=" ");  
   
# Sort in Ascending Order    
for i in range(0, len(l1)):  
  
  for j in range(i+1, len(l1)): 

      
    if(l1[i] > l1[j]): 

            #print("tem=l1[i]",l1[i])
            tem = l1[i]; 
            #print("tem-",tem) 
            l1[i] = l1[j]; 
            #print("l1[i]-",l1[i])
            l1[j] = tem; 
            #print("l1[j]----",l1[j])

      
                  
print();   
print("Elements of list sorted in ascending order: ");    
for i in range(0, len(l1)):    
    print(l1[i], end=" ");   
  