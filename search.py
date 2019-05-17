class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def display(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
    def search(self,val):
        curr=self.head
        while curr!=None:
            if curr.data==val:
                return True
            curr=curr.next
        return False
        
        
l=LinkedList()
l.head=Node(1)
second=Node(2)
third=Node(3)
l.head.next=second
second.next=third
print("THE LIST CONTAINS")
l.display()
print("the search result for element 2 is",l.search(2))  
