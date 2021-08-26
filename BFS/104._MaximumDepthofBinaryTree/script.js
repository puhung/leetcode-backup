var maxDepth = function (root) {
  if (root === null || root === undefined) return 0;
  //find the max depth of the children node ,then + 1
  else return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
};
