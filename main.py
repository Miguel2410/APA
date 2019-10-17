import sys
import Heap_Problema as heap
import time


def main():
 
   
   # TODO: Comprobar numero de argumentos correcto
   fichero = sys.argv[1]
   k = sys.argv[2]
   
   list = heap.parsear(fichero)
   
   heap.countCouples(list.head, float(k))
 
   
   
   # AQUI LO HARE USANDO EL METODO DE INSERTION SORT
   #list = heap.parsear2(fichero)
   #list = heap.insertionSort(list.head)
   #heap.countCouples(list, float(k))

if __name__ == "__main__":
   main()