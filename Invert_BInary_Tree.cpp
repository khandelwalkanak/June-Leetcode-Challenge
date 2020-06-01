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
    void dfs(TreeNode* root)    // helper function for swapping the values.
    {
        if(root == NULL)        // terminating condition or whatever people call it!.
        {
            return;
        }
        swap(root->left, root->right);//swapping of the immediate left and right of the tree.
        
        dfs(root->left);            // passing root->left as new root recursively
        
        dfs(root->right);           // same as upper, but only with root->right.
    }
    TreeNode* invertTree(TreeNode* root) 
    {
        
        dfs(root);                  // calling helper function.
        
        return root;
    }
};