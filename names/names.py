import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

#  Bunary tree
class BinarySearchTree:
      def __init__(self, value):
       self.value = value
       self.left = None
       self.right = None

  # Insert the given value into the tree / adds the input value to the binary tree
  # adhering to the rules of the ordering of the elements in dinary search tree.
  # Needs to travers to find spot to insert

  # step 2 - insert into tree name 1 
# step 3 - use inter.  name2  then use consains to seach list 
# set 4- if true - append to dup. []
# duplicates = set(names_1) & set(names_2)
# duplicates = set(names_1).intersection(names_2)

def insert(self, value):
        # Current node is self
        #Check if self.value is bigger or smaller then new value - left or right
        if value < self.value:
              # We go left or right then check if nodeexists
              if not self.left:
                    # if node does not exiist then create a node there
                    self.left = BinarySearchTree(value)
                    # if node does not exist use recursion: call insert on that node
              else:
                    self.left.insert(value)
        else:
                  if not self.right:
                        self.right = BinarySearchTree(value)
                  else:
                        self.right.insert(value)
 

  

def contains(self, target):
    # Check if the current value is the target
    if self.value == target:
          return True
          # Otherwiaw, left or right bases on bigger or smaller, and then call contains agine
    else:
      if target < self.value:
                if not self.left:
                    return False
                else:
                    return self.left.contains(target)
      else:
                      # go right
                if not self.right:
                    return False
                else:
                    self.right.contains(target)

  # Return the maximum value found in the tree
def get_max(self):
    # max node is fartherst to the right
    if not self.right:
          return self.value
    return self.right.get_max()




  # Call the function `cb` on the value of each node
  # You may use a recursive or iterative approach
def for_each(self, cb):
    cb(self.value)
    if self.left:
        self.left.for_each(cb)
    if self.right:
        self.right.for_each(cb)
              
        
    


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")