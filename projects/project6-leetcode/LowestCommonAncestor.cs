namespace LeetCode.LowestCommonAncestor;

public class TreeNode
{
    public int val { get; set; }
    public TreeNode? left { get; set; }
    public TreeNode? right { get; set; }
    public TreeNode(int val = 0, TreeNode? left = null, TreeNode? right = null)
    {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
public class LowestCommonAncestorSolution
{
    public TreeNode? LowestCommonAncestor(TreeNode? root, TreeNode p, TreeNode q)
    {
        if (root == null)
        {
            return null;
        }
        if (root == p || root == q)
        {
            return root;
        }

        TreeNode? left = LowestCommonAncestor(root.left, p, q);
        TreeNode? right = LowestCommonAncestor(root.right, p, q);

        if (left != null && right != null)
        {
            return root;
        }

        return left ?? right;
    }
}
