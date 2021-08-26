//iterative approach
var inorderTraversal = function (root) {
  if (!root) return [];
  let output = [];
  let stack = [];
  let curr = root;

  //continue looping in 2 conditions: 1. even the stack is empty but the curr still has something. 2. at the leaf node where the curr == null, but the stack is not empty
  while (curr != null || stack.length != 0) {
    //push it in the stack then find the left lode
    if (curr != null) {
      stack.push(curr);
      curr = curr.left;
    }
    //move to the bottom
    else {
      curr = stack.pop();
      output.push(curr.val);
      curr = curr.right;
    }
  }
  return output;
};

//recursion
var inorderTraversal = function (root) {
  if (!root) return [];

  return [
    ...inorderTraversal(root.left),
    root.val,
    ...inorderTraversal(root.right),
  ];
};
