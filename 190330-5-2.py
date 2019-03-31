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
    global ans
    ans=0
    def calculate(root):
        global ans
        if not root: return 0
        leftnum=calculate(root.left)
        rightnum=calculate(root.right)
        leftarr=rightarr=0
        if root.left and root.left.val==root.val:
            leftarr+=1
        if root.right and root.right.val==root.val:
            rightarr+=1
        ans=max(ans,leftarr+rightarr)
        return max(leftarr,rightarr)
    calculate(root)
    print(ans)
    return ans
longestUnivaluePath(root)
