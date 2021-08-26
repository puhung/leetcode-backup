var lowestCommonAncestor = function (root, p, q) {
  function dfs(node) {
    //deal with 2 situations: First, if node is child of a leaf node, just return node = null; Second, return the current node, which matches p or q;
    if (!node || node == p || node == q) return node;

    let left = dfs(node.left);
    let right = dfs(node.right);

    // Return the node only if the left is p or q and the right is q or p. Else, return left of right
    return left && right ? node : left || right;
  }

  return dfs(root);
};
