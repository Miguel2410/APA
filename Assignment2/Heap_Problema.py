from math import *
import numpy as np

def getChr(x):
   if (x% 10 == 0):
      x = str(x)[:-1] + 'q'
   else:
      x = str(x)[:-1] + 'p'
   return x


def euclidean_distance(x_i, x_j , y_i, y_j):
   return np.sqrt(np.square((x_i - y_i)) + np.square((x_j - y_j)))

def countCouples(head, k):

   current = head
   f = open("results.txt" , "w")
   contador = 0
   while current is not None:
      
      loci = current.get_loci()
      if(current.get_next() is not None):
         lociNext = current.get_next().get_loci()
      
         if (loci == lociNext) and k >= euclidean_distance(current.get_x() , current.get_y() , current.get_next().get_x() , current.get_next().get_y()):
            contador += 1
         else:
            if(loci != lociNext):
               f.write(getChr(current.get_loci()) + '\t' + str(contador) + '\n')
               contador = 0
      else:
         f.write(getChr(current.get_loci()) + '\t' + str(contador) + '\n')
   
      current = current.get_next()

   f.close()

   
class Node:
   def __init__(self):
      self.next = None
      self.loci = None
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
   
   def set_next(self, next):
      self.next = next
   
   

class LinkedList:
   def __init__(self):
      self.head = None
   
   def addNode(self, node):

      if self.head is None:
         node.set_next(self.head)
         self.head = node
      elif self.head.get_loci() > node.get_loci():
         node.set_next(self.head)
         self.head = node

      else:
         current = self.head
         while current.get_next() is not None and current.get_next().get_loci() < node.get_loci():
            current = current.get_next()

         node.set_next(current.next)
         current.set_next(node)
         
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






   


