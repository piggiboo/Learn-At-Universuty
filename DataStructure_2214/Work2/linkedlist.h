#pragma once
#include<iostream>

// 1. แม่แบบกล่องเก็บของ (Node)
template<typename T>
class Node{
  public:
    T data;
    Node * next;
    Node();
    Node(T data);
};


template<typename T>
class LinkedList{
  public:
    Node<T> * head;
    int size;
    LinkedList();
    void add(T data);
    void travel();
    void remove(int index);
    void removeAll();
    void insert(int index,T data);
    T get(int index);
    void set(int index,T data);
};



template<typename T>
Node<T>::Node(){
  data = T();
  next = NULL;
}

template<typename T>
Node<T>::Node(T data){
  this->data = data;
  this->next = NULL;
}

template<typename T>
LinkedList<T>::LinkedList(){
  this->head = new Node<T>();
  size = 0;
}

template<typename T>
void LinkedList<T>::add(T data){
  Node<T> * newNode = new Node<T>(data);
  newNode->next = head->next;
  head->next = newNode;
  size++;
}

template<typename T>
void LinkedList<T>::travel(){
  Node<T> * travel = head;
  for(;travel!=NULL;){
    std::cout<<travel<<","<<travel->data<<","<<travel->next<<std::endl;
    travel = travel->next;
  }
}

template<typename T>
void LinkedList<T>::remove(int index){
  Node<T> * travel = head;
  for(int i = 1;i<=index-1;i++){
    travel = travel->next;
  }
  Node<T> * nodei = travel->next;
  travel->next = nodei->next;
  delete nodei;
  size--;
}

template<typename T>
void LinkedList<T>::removeAll(){
  Node<T> * travel = head;
  Node<T> * temp;
  for(;travel!=NULL;){
    std::cout<<travel<<","<<travel->data<<","<<travel->next<<std::endl;
    temp = travel;
    travel = travel->next;
    delete temp;
  }
}

template<typename T>
T LinkedList<T>::get(int index){
  Node<T> * travel = head;
  
  for(int i = 1; i <= index; i++){
    travel = travel->next;
  }
  
  return travel->data;
}