var diameterOfBinaryTree = function (root) {
  let maxLength = 0;
  maxDepth(root);
  return maxLength;

  function maxDepth(node) {
    if (!node) return 0; //reaches the leaf node

    //do the recursion for left, right node
    let left = maxDepth(node.left);
    let right = maxDepth(node.right);

    maxLength = Math.max(maxLength, left + right); // compare maxLength with the longest path that passes through the current node from left to right.

    return 1 + Math.max(left, right); // This value will be used to return to the parent of current node, so choose the longest path between left and right, then return it.
  }
};
