class dlist:
    class Node:
        def __init__(self,prev,item,next):
            self.prev=prev
            self.item=item
            self.next=next

    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def size(self): return self.size

    def insert_front(self,item):
        if self.size == 0:
            self.head=self.Node(None,item,None)
            self.tail=self.head
        else:
            self.head=self.Node(None,item,self.head)
        self.size+=1

    def print_list(self):
        p=self.head
        while p:
            print(p.item,end=" ")
            p=p.next
#sample=dlist()
#sample.insert_front('apple')
#sample.insert_front('orange')
#sample.print_list()
