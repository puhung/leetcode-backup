var kthSmallest = function (root, k) {
  let res = [];
  dfs(root);
  return res[k - 1];

  function dfs(node) {
    if (res.length != k) {
      if (node.left) dfs(node.left);
      res.push(node.val);
      if (node.right) dfs(node.right);
    }
  }
};
