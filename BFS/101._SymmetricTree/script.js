var isSymmetric = function (root) {
  if (root == null) return true;

  return symmetryChecker(root.left, root.right);
};

function symmetryChecker(left, right) {
  if (left == null && right == null) return true; // If both sub trees are empty

  if (left == null || right == null) return false; // If only one of the sub trees are empty
  if (left.val !== right.val) return false; // If the values dont match up

  // Check both subtrees but travelled in a mirrored/symmetric fashion
  return (
    symmetryChecker(left.left, right.right) &&
    symmetryChecker(left.right, right.left)
  );
}
