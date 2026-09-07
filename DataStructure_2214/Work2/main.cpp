#include<iostream>
#include<string>
#include"linkedlist.h"

int main(){

   LinkedList<std::string> ll1; 

   ll1.add("A10");
   ll1.add("A20");
   ll1.add("A30");
   ll1.add("A40");
   ll1.add("A50");

   std::cout << "Size = " << ll1.size << std::endl;
   
 
   ll1.travel();
   
  
   std::cout << "\n--- Testing get() Function ---" << std::endl;
   

   std::cout << "Data at index 1 is: " << ll1.get(1) << std::endl;
   std::cout << "Data at index 3 is: " << ll1.get(3) << std::endl; 
   std::cout << "Data at index 5 is: " << ll1.get(5) << std::endl; 
   

   ll1.removeAll();
   

   return 0; 
}