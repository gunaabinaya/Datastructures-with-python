class queue:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return self.items==[]
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        return self.items.pop(0)
    def display(self):
        print( self.items)
s=queue()
a=1
while(a==1):
    print("1.enqueue\n2.dequeue\n3.display\nEnter your choice")
    n=int(input())
    if(n==1):
        x=input("Enter the item to be queue")
        s.enqueue(x)
        s.display()
    elif(n==2):
        if s.isempty():
            print("The queue is empty")
        else:
            print("delwted value",s.dequeue())
        s.display()
    elif n==3:
        if s.isempty():
            print("The queue is empty")
        else:
            print("the queue contains",s.display())
    else:
        print("Invalid option")
