#deletes the entire list
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
            print(temp.data)
            temp=temp.next
    def deletelist(self):
        curr=self.head
        while curr:
            p=curr.next
            del curr.data
            curr=p
            
l=LinkedList()
l.head=Node(1)
second=Node(2)
third=Node(3)
l.head.next=second
second.next=third
print("The list before deletion")
l.display()
l.deletelist()
    
