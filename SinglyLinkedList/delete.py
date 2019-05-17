#delete by keyvalue
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
    def delete(self,key):
        temp=self.head
        if temp is not None:
            if(temp.data==key):
                self.next=temp.next
                temp=None
        while(temp is not None):
            if(temp.data==key):
                break
            prev=temp
            temp=temp.next
        if(temp==None):
            return
        prev.next=temp.next
        temp=None
    
        
l=LinkedList()
l.head=Node(1)
second=Node(2)
third=Node(3)
l.head.next=second
second.next=third
print("the list conatins")
l.display()
print("after deleting the element 3")
l.delete(3)
l.display()
    
