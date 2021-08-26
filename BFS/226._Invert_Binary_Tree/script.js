//recursion
var invertTree = function (root) {
  if (root === null) return root;

  [root.left, root.right] = [invertTree(root.right), invertTree(root.left)];
  return root;
};

//DFS
var invertTree = function (root) {
  let stack = [root];

  while (stack.length) {
    let n = stack.pop();
    if (n !== null) {
      [n.left, n.right] = [n.right, n.left];
      stack.push(n.left, n.right);
    }
  }
  return root;
};

//BFS
var invertTree = function (root) {
  let queue = [root];

  while (queue.length) {
    let n = queue.shift();
    if (n !== null) {
      [n.left, n.right] = [n.right, n.left];
      queue.push(n.left, n.right);
    }
  }
  return root;
};
