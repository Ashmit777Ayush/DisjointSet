# python3
import threading
class disjointSet:
  def __init__(self, n):
    # creating the disjoint set from 1 to n
    self.set = [int(x) for x in range(1, n+1)]
    
  # function to give which set it belongs to
  def find(self, i):
    return self.set[i]
  
  def union(self, *args):
    x_id = self.find(args[0][0]-1)# find the set to which it belongs to 
    y_id = self.find(args[0][1]-1)# for y also find the set to which it belongs
    
    if x_id==y_id:# this means that both belongs to the same set
      return 
    else:# if not belonging to the same set
      id_new = min(x_id, y_id)# taking minimum of both the id'
      
      for x in range(len(self.set)):# go through the each set elements
        if self.set[x] in (x_id, y_id):# if any belongs to these two id's then update heir set id
          self.set[x]=id_new
          
         
def main():
  number = int(input('number of elements in the disjoint set --> \t'))
  
  dis_set = disjointSet(number)
  
  while(True):
    print('1 --> union')
    print('2 --> find')
    print('3 --> Print the set')
    print('0 --> EXIT')
    
    userInput = int(input('select from the above --> \t'))
    
    if userInput == 1:
      dis_set.union([int(x) for x in input('give two elements to union --> \t').split()])
    elif userInput ==2:
      print(dis_set.find(int(input('give element to be found -->\t'))-1))
    elif userInput==3:
      print(*dis_set.set, sep='\t')
    elif userInput==4:
      break
    else:
      print('chose correct options')
      
threading.Thread(target=main).start()
