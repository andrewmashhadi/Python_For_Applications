#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: Andrew Mashhadi
"""


class Node:
    
    def __init__(self, data):        
        self.data = data
        self.next = None

    def __str__(self):        
        return repr(self.data)   
        


class LinkedList:
    
    def __init__(self, pythonList = None):          
        self.first = None
        self.last = None
        self.len = 0              
        if type(pythonList) is list:
            for entry in pythonList:      
                self.append(entry)       

    def append(self, data):          
        self.len += 1
        newNode = Node(data)        
        if self.first == None:
            self.first = newNode
            self.last = newNode
            return        
        
        self.last.next = newNode
        self.last = newNode
        
    def prepend(self, data):         
        self.len += 1
        newNode = Node(data)       
        if self.first == None:
            self.first = newNode
            self.last = newNode
            return      
        
        newNode.next = self.first
        self.first = newNode
        
    def __len__(self):       
        return self.len
    
    def __eq__(self, other):       
        if other.len != self.len:
            return False       
        self_node = self.first
        other_node = other.first 
        while self_node is not None: 
            if self_node.data != other_node.data:
                return False
            self_node = self_node.next
            other_node = other_node.next
            
        return True
    
    def __str__(self):       
        curr_node = self.first
        list_str = "["        
        while curr_node is not None:
            list_str += (str(curr_node) + " -> ")
            curr_node = curr_node.next           
        list_str += "]"
        
        return list_str       
        
    def __repr__(self):       
        curr_node = self.first
        list_str = "LinkedList(["        
        while curr_node is not None:
            if curr_node is not self.first:
                list_str += ", "
            list_str += str(curr_node)
            curr_node = curr_node.next           
        list_str += "])"
        
        return list_str

    def insert(self, data, idx):      
        curr_node = self.first
        if idx == 0:
            self.prepend(data)
            return 
        elif idx == self.len:
            self.append(data)
            return
            
        curr_node = self.first
        for i in range(1, idx):        
            curr_node = curr_node.next  
            
        prev_node = curr_node
        after_node = curr_node.next  
        
        newNode = Node(data)
        prev_node.next = newNode
        newNode.next = after_node
        self.len += 1
