#delete at a given position
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
            temp=temps.next
    def deleteatanypos(self,pos):
        temp=self.head
        if temp==None:
            return
        if pos==0:
            self.head=temp.next
            temp=None
            return
        for i in range(pos-1):
            temp=temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next=temp.next.next
        temp.next=None
        temp.next=next
        

l=LinkedList()
l.head=Node(1)
second=Node(2)
third=Node(3)
l.head.next=second
second.next=third
print("The list contains")
l.display()
print("after deleting an element with given position")
l.deleteatanypos(2)
l.display()
    
