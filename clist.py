class clist:
    class node:
        def __init__(self,item,next):
            self.item=item
            self.next=next
    def __init__(self):
        self.last=None
        self.size=0
    def no_list(self): return self.size

    def insert(self,item):
        newnode=self.node(item,None)
        if self.no_list()==0:
            newnode.next=newnode
            self.last=newnode
        else:
            newnode.next=self.last.next
            self.last.next=newnode
        self.size+=1

    def delete(self):
        #if self.last.item==item:
        if self.size == 1: self.last=None
        else:
            self.last.next=self.last.next.next
        self.size-=1


    def print_list(self):
        temp=self.last
        for i in range(self.no_list()):
            print(temp.item, end=" ")
            temp=temp.next


sample=clist()
sample.insert('apple')
sample.insert('banna')
sample.insert('cat')
sample.print_list()
