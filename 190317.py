class TreeNode:
    def __init__(self,val,left=None,right=None):
         self.val = val
         self.left = None
         self.right = None
def rightSideView(root: TreeNode):
    heights=[root.val]
    height=[root]
    while height:
        temp=[]
        for node in height:
            print('test',node.val)
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right)
            #height.pop(0)
        if temp: heights.append(temp[-1].val)
        height=temp
    print(heights)
sample1=TreeNode(1)
sample2=TreeNode(2)
sample3=TreeNode(3)
sample4=TreeNode(4)
sample5=TreeNode(5)
sample1.left=sample2
sample1.right=sample3
sample2.right=sample5
sample3.right=sample4
rightSideView(sample1)
