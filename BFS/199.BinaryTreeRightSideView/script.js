//BFS
var rightSideView = function (root) {
  if (!root) return [];
  let queue = [root];
  let result = [];

  //the while loop is for looping each level in the tree
  while (queue.length) {
    let Qlength = queue.length;

    for (let i = 0; i < Qlength; i++) {
      let current = queue.shift();
      if (i === Qlength - 1) result.push(current.val);
      if (current.left) queue.push(current.left);
      if (current.right) queue.push(current.right);
    }
  }
  return result;
};
//DFS
var rightSideView = function (root) {
  if (!root) return [];
  let result = [];
  preorderDFS(root, 0);
  return result;

  function preorderDFS(node, h) {
    if (!node) return;
    result[h] = node.val;
    preorderDFS(node.left, h + 1);
    preorderDFS(node.right, h + 1);
  }
};
