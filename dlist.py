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

    
