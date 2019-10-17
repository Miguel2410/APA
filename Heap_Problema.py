from math import *
import numpy as np

def getChr(x):
   if (x% 10 == 0):
      x = str(x)[:-1] + 'q'
   else:
      x = str(x)[:-1] + 'p'
   return x
def isNear(coord_1, coord_2, k):
   
   if(euclidean_distance(coord_1,coord_2) <= k):
      return True
   
   return False


def euclidean_distance(x_i, x_j , y_i, y_j):
   
   return np.sqrt(np.square((x_i - y_i)) + np.square((x_j - y_j)))

def countCouples(head, k):

   current = head
   f = open("results.txt" , "w")
   contador = 0
   while current is not None:
      

      loci = current.loci
      if(current.next is not None):
         lociNext = current.next.loci
      
         if (loci == lociNext) and k >= euclidean_distance(current.x , current.y , current.next.x , current.next.y):
            contador += 1
         else:
            if(loci != lociNext):
               f.write(getChr(current.loci) + '\t' + str(contador) + '\n')
               contador = 0
      else:
         f.write(getChr(current.loci) + '\t' + str(contador) + '\n')
   
         # current = current.next
         # loci = lociNext
         # if (current.next is not None):
         #    lociNext = getChr(current.next.loci)
      current = current.next

   f.close()

   
class Node:
   def __init__(self):
      self.next = None
      self.loci = None
      self.chr = None
      self.x = None
      self.y = None
      self.read = None
 
   def get_x(self):
      return self.x

   def get_y(self):
      return self.y
   
   def get_loci(self):
      return self.loci
   
   def get_read(self):
      return self.read
   
   def set_x(self,x):
      self.x = x
      
   def set_y(self, y):
      self.y = y
      
   def set_loci(self, loci):
      self.loci = loci
   
   def set_read(self, read):
      self.read = read
   
   

class LinkedList:
   def __init__(self):
      self.head = None
   
   def addNode(self, node):

      if self.head is None:
         node.next = self.head
         self.head = node
      elif self.head.loci > node.loci:
         node.next = self.head
         self.head = node

      else:
         current = self.head
         while current.next is not None and current.next.loci < node.loci:
               
            current = current.next

         node.next = current.next
         current.next = node
   def __str__(self):
      data=[]
      current = self.head
      while current is not None:
         print(current.val)
         current = current.next
         
def parsear(fichero):
   f = open(fichero , "r")
   linked = LinkedList()
   for line in f:
      read, loci, coords = line.split('\t')
      x,y =coords[1:coords.index(')')].split(',')


      node = Node()
      if 'p' in loci:
         node.set_loci(int(loci[:loci.index('p')] + '1'))
      else:
         node.set_loci(int(loci[:loci.index('q')] + '0'))

      node.set_x(float(x))
      
      node.set_y(float(y))
      node.set_read(read)
      
      linked.addNode(node)
     
   return linked


def parsear2(fichero):
   f = open(fichero , "r")
   linked = LinkedList()
   for line in f:
      read , loci , coords = line.split('\t')
      
      x , y = coords[1:coords.index(')')].split(',')
      
      node = Node()
      node.set_loci(loci)
      node.set_x(float(x))
      
      node.set_y(float(y))
      node.set_read(read)
      
      linked.head = node
      linked.head.next = linked.head
   
   return linked
def insertionSort(h):
   if h == None:
      return None
   # Make the first node the start of the sorted list.
   sortedList = h
   h = h.next
   sortedList.next = None
   while h != None:
      curr = h
      h = h.next
      if not mayorQue(curr.loci, sortedList.loci):
         # Advance the nodes
         curr.next = sortedList
         sortedList = curr
      else:
         # Search list for correct position of current.
         search = sortedList
         while search.next != None and mayorQue(curr.loci,search.next.loci):
            search = search.next
         # current goes after search.
         curr.next = search.next
         search.next = curr
   return sortedList


   


