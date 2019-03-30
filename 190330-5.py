# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

root=TreeNode(1)
node1=TreeNode(5)
node2=TreeNode(5)
node3=TreeNode(4)
node4=TreeNode(4)
node5=TreeNode(4)
root.left=node3
root.right=node1
node1.right=node2
node3.left=node4
node3.right=node5

def longestUnivaluePath(root: TreeNode) -> int:
    result=[]
    def calculate(root,num):

        while root and (root.left or root.right):
            #print('test1',root.val,num)
            if root.left and root.right:
                if (root.val != root.left.val) and (root.val != root.right.val):
                    #print('test2',num,root.val,root.left.val,root.right.val)
                    print('append1',num,root.val)
                    result.append(num)
                    #num=0
                    calculate(root.left,0)
                    #print('test3',root.left.val,num)
                    calculate(root.right,0)
                    #print('test4',root.right.val,num)
                    break
                elif (root.val == root.left.val and root.val == root.right.val):
                    #num+=2
                    #print('test5',root.val,root.left.val,root.right.val)
                    calculate(root.left,num+2)
                    calculate(root.right,num+2)
            if root.left:
                if (root.val == root.left.val):
                    #num+=1
                    #print('test6',root.val,root.left.val,num)
                    calculate(root.left,num+1)
                    #num=0
                    calculate(root.right,0)
            if root.right:
                if (root.val == root.right.val):
                    #num+=1
                    #print('test7',root.val,root.right.val,num)
                    calculate(root.right,num+1)
                    #num=0
                    calculate(root.left,0)
            return
        print('append2',num)
        result.append(num)
    calculate(root,0)
    print(result)
    return max(result)
longestUnivaluePath(root)
