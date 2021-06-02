# python3
import threading
class disjointSet:
  def __init__(self, number):
    self.set = [x for x in range(1, number+1)]# assigning from 1 to n
    self.rank = [0 for x in range(number)]
    
  def find(self, i):
    # in path compresssion actually at each time we are seaching the parent or id we asr assigning the parent id to it's children actually and then returning the set id or parent
    if i+1 != self.set[i]: # as we are indexing 0 to n-1 and elements were from 1 to n at these index respectively so we have to match with the i+1 at index i
      self.set[i]=self.find(self.set[i]-1)# always find at index that would be at self.set[i]-1
    return self.set[i]
  
  
  def union(self, *args):
    x = args[0][0]-1 # because  of the indexing
    y = args[0][1]-1 # beacuse of the indexing
    
    x_id = self.find(x)-1 # as we are getting directly the parent or id but have to look in the index that will be id-1
    y_id = self.find(y)-1 # same in this case also
    
    if self.rank[x_id]>self.rank[y_id]:# now assign as like rank heuristics
      self.set[y_id]=x_id+1
    else:
      self.set[x_id]=y_id+1
      
      if self.rank[x_id]==self.rank[y_id]:
        self.rank[y_id]+=1
        
        
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
      print(dis_set.find(int(input('element whose set_id_to be found-->\t'))-1))
    elif userInput==3:
      print(*dis_set.set, sep='\t')
      print(*dis_set.rank, sep='\t')
    elif userInput==0:
      break
    else:
      print('chose correct options')
      
threading.Thread(target=main).start()
