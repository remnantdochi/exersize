/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int cnt = 0;
    int calc(TreeNode* root)
    {
        int left = 0, right = 0;
        if (root == NULL) return cnt;
        if (root->left == NULL && root->right == NULL) return cnt;
        if (root->left != NULL) left = calc(root->left);
        if (root->right != NULL) right = calc(root->right);
        return left>right ? left + 1 : right + 1; 
    }
    int maxDepth(TreeNode* root) {
        int left = 0, right = 0;
        if (root == NULL) return 0;
        if (root->left != NULL)
        {
            cnt=1;
            left = calc(root->left);          
        }
        if (root->right != NULL)
        {
            cnt=1;
            right = calc(root->right);          
        }
        return left>right ? left+1:right+1;
    }
};