import sys
import Heap_Problema as heap
import time


def main():
 
   fichero = sys.argv[1]
   k = sys.argv[2]
   
   list = heap.parsear(fichero)
   
   heap.countCouples(list.head, float(k))
 
if __name__ == "__main__":
   main()