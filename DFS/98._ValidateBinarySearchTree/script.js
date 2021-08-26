var isValidBST = function (root, min = -Infinity, max = Infinity) {
  if (!root) return true;
  if (root.val <= min || root.val >= max) return false; //check if current node follows the BST rule

  //check if left and right follow the BST rule
  return (
    isValidBST(root.left, min, root.val) &&
    isValidBST(root.right, root.val, max)
  );
};
