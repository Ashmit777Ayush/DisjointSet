# python3
import threading
class disjintSet:
  def __init__(self, number):
    self.set=[int(x) for x in range(1, number+1)]
    self.rank = [0 for x in range(number)]
    
  def find(self, i):
    # run the loop till we find that a element is itself a parent of itself
    while(i+1!=self.set[i]):
      i = self.set[i]-1
      
    return i
  
  def union(self, *args):
    x = args[0][0]-1
    y = args[0][1]-1
    x_id = self.find(x)# find to which set it belongs to
    y_id = self.find(y)# find to which y belongs to
    
    if x_id==y_id:
      return # as both belongs to the same set
    
    else:
      # now we will heck the rank of each and then assign the set to which it belong or parent of it
      if self.rank[x_id] > self.rank[y_id]:# if rank of x is higher then make y to set x that is x_id
        self.set[y_id]=x_id+1 # we need to provide the +1 because we are using indexing from 0 to n-1  but asigning from 1 to n so when searching we are using the -1 to given num then 
        # while froviding it's set_id or parent we have to provide the +1
      else:
        self.set[x_id]=y_id+1 # here also the plus 1
        
        if self.rank[x_id]==self.rank[y_id]:
          self.rank[y]+=1
          
          
def main():
  num = int(input('elements in the disjoint set'))
  dis_set = disjointSet(num)
  
  while(True):
    print('1 --> union')
    print('2 --> find')
    print('3 --> Print the set')
    print('0 --> EXIT')
    
    userInput = int(input('select from the above --> \t'))
    
    if userInput == 1:
      dis_set.union([int(x) for x in input('give two elements to union --> \t').split()])
    elif userInput ==2:
      print(dis_set.find(int(input('give element to be found -->\t'))-1)+1) # while searching we send it as the -1 and while getting it will give the index in -1 we have to add 1 in ans
    elif userInput==3:
      print(*dis_set.set, sep='\t')
    elif userInput==0:
      break
    else:
      print('chose correct options')
      
threading.Thread(target=main).start()
