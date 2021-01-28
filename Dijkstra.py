#DO NOT CHANGE ANY EXISTING CODE IN THIS FILE
class min_heap_pq():            #Class to executes function of priority queues
                        
    def __init__(self):             #Initialise class variable
        self.heap_size=0            #varibale to store size of heap
        self.heap=[]                #variable to save the queue as an array
        
    def Parent(self,i):                 #Function to mark index of the parent in heap
        return int((i-1)/2)
    
    def Left(self,i):               # Function to mark index of left child
        return int(2*i+1)
    
    def Right(self,i):              # Function to mark index of right child
        return int(2*i+2)
    
    def min_heapify(self,i):        #min heapify function to make the min heap tree passed with index of element
        l=self.Left(i)              # left child for any index i is initialised
        r=self.Right(i)             # right child for any index i is initialised
        
        if l<self.heap_size and self.compare(self.heap[l][1],self.heap[i][1]):       #compare the left heap and called a compare function for value compare
            smallest=l                                                               # if condition true then smallest is set to left
        else: 
            smallest=i                           # if condition true then smallest is left as i which is parent
        
        if r<self.heap_size and self.compare(self.heap[r][1],self.heap[smallest][1]):
            smallest=r                        # if condition true then smaller is right so smallest set to r
        if smallest!=i:                      # if to check if i index is of the parent
            temp=self.heap[i]          #   swapping the smallest of child with parent
            self.heap[i]=self.heap[smallest]   
            self.heap[smallest]=temp
            self.min_heapify(smallest)       #recursive call for min_heapify to traverse whole tree         
        
            
    def compare(self,array_element,key):        #a compare function takes two elements to compare
        if(array_element<key):      # if compare true return true 
            return True
        else:           #if true returns false
            return False
    def min_heap_insert(self,key):              #min heap function to insert Key_value element in heap
        self.heap.append(key)                       #New key_value is appended at last position
        self.heap_size=len(self.heap)               #heap size is calculated
        self.decrease_key(self.heap_size-1)             #Called decrease key function


    def decrease_key(self,index):               #Function that lets key_value swim up tree based on its key  value     
       
        while (index > 0) and (self.heap[self.Parent(index)][1] > self.heap[index][1]) :    #checks if key value (by weight) parent is smaller or larger
            temp=self.heap[self.Parent(index)]                      #if parent is bigger than exchanged with it in heap
            self.heap[self.Parent(index)]=self.heap[index]
            self.heap[index]=temp
            index=self.Parent(index)                        #Index of parent and Key_vlaue element swapped for further swim in heap tree
        
    def decrease_key_relax(self,key_value):                 #decrease_key function when 2 key value for same vertex but different weights
         for i in range(len(self.heap)):                    #for loop O(Vlogn) to find vertex match
             if (self.heap[i][0]==key_value[0]):
                 self.heap[i][0]=key_value[0]
         self.decrease_key(len(self.heap)-1)                    #called decrease key to let the new key_value pair to sm in heap's min position

    def extract_min(self):                      #function returns the Smallest element from heap and removes it from heap 
        
        min=self.heap[0]                    #the smallest element is at the heap's fist position(index=0)
        index=self.heap_size-1
        
        if(index==0):           #if condition to check was it the only element in heap
            self.heap.clear()
        else:
            self.heap[0]=self.heap[index]           #made the last element of heap as first
            del self.heap[index]
        self.heap_size=index
        self.min_heapify(0)             #min_heapify function called on the new first element(the old last element moved to first)
        
        return min              #smallest element returned
    
    def minimum(self):              #shows which element is the in heap (not used in code, just for observation)
        return self.heap[0]         #smallest element at the ehap's first position (index=0)
            
    def isEmpty(self):              #checks whether the heap is empty or not
        
        return self.heap_size > 0               #return false when heap does not contain any element otherwise true

class Dijkstra():               #Dijsktra algorithm can be found here

    def __init__(self):         #initialised the Class variables 
        self.d={}               #stores the distance from source for each vertex as dictionary's key Value pair (vertex-distance)
        self.usp={}             #initialised varibale to store the Unique shortest path for each vertex as dictionary(key Value pair- (vertex-1 or 0))
        self.parent={}          #stores the predecessor for each vertex as key value pair(Vertex-predecessor)
        self.key=min_heap_pq()      #Object of priority queue class(min_heap_pq) created to store the key value pair
        
    def initialise_SS(self,n,s):                #function to initialise the distance and Unique shortest path variables 
        for i in range(1,n+1):                      #looped over each verte G(1 to N)
            self.d[i]=float('inf')                  #Distance set to infinity for each vertex at start
            self.parent[i]=None                         #parents for each vertex set to None(nil) at start
        self.d[s]=0                         #distance from source to source set to 0
        self.usp[s]=1                   
        
    
    def contain(self,v):                    #contain function to check if a heap contains a keyvalue pair
        for i in range(len(self.key.heap)):             #loop to iterate in heap O((V+E)logn)
            if v==self.key.heap[i][0]:                      
                return True                     #return true If element present in priority queue of key value pair
            
    def Relax(self,u,v,w):                  #function to relax the distances
        if  self.d[v] > (self.d[u]+w):              #if new distance smaller than existing add smaller distance
            self.d[v]= self.d[u]+w                      #new smaller distance for the corresponding vertex updated
            self.parent[v]=u                #predecessor of new smaller distance for the corresponding vertex updated
            if (self.contain(v)):                   #check if the priority queue of key_value pair contains the new Key_value pair 
                key_value=[v,self.d[v]]                 #Key_value pair generated(Vertex-weight)
                self.key.decrease_key_relax(key_value)  #if contains than updated smaller distance in priority queue for the vertex
            else:               
                key_value=[v,self.d[v]]             #if the vertex not in queue added in priority queue
                self.key.min_heap_insert(key_value)
            self.usp[v]=self.usp[u]             #usp updated to that of predecessor as unique path
        elif self.d[v]==self.d[u]+w:                #else condition to check if vertex can be traversed by equal weight by new vertex
            self.usp[v]=0                               #not a unique path anymore set to 0
            
            
    def Dijkstra_alg(self, n, e, mat, s):                       #Function for Dijsktra main algorithm implemented
         #Write your code here to calculate shortest paths and usp values from source to all vertices
		 #This method will have four inputs (Please see testcase file)
		 #This method should return a two dimensional array as output (Please see testcase file)
         self.initialise_SS(n,s)                #initialised variables (d,usp,parent) to initial conditiond
         
         discovered=[]                      #variable to add the discovered or already visited nodes(vertex)
         key_value=[s,self.d[s]]            #vertex(0 index)-weight(1 index) pair as key_value generated of source
         self.key.min_heap_insert(key_value)        #source inserted in priority queue named key
         
         while self.key.isEmpty():                  #iterated if queue not empty
             u=self.key.extract_min()               #extracted the smallest element (key-value) in heap based on its weight
             discovered.append(u[0])                #appened in discovered list
             
             for i in range(e):                             #loop iterated over vertex taking a total of O((|V|+|E|)logN)
                 if mat[i][0]==u[0] and (mat[i][1] not in discovered):          #checks for in one direction as Undirected graph
                     self.Relax(mat[i][0],mat[i][1],mat[i][2])                  #relax called if found node to node path to relax distance
                 if mat[i][1]==u[0] and (mat[i][0] not in discovered):          #check from other way as undirected graph
                     self.Relax(mat[i][1],mat[i][0],mat[i][2])                  #relax called if found node to node path to relax distance
                     
         result=[]                      #result appended distance to each vertex and usp
         for i in  range(1,n+1):                #loop to add the result for each vertex 
             result.append([self.d[i],self.usp[i]])     #result appended in the list
         return result                      #Final result returend
 
############------------END PROGRAM----------#################