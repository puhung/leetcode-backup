//bfs
var connect = function (root) {
  if (!root) return root;
  let queue = [root];
  while (queue.length) {
    let n = queue.length;
    for (let i = 0; i < n; i++) {
      let current = queue.shift();
      if (i !== n - 1) {
        current.next = queue[0];
      }
      if (current.left) {
        queue.push(current.left);
      }
      if (current.right) {
        queue.push(current.right);
      }
    }
  }
  return root;
  // Time Complexity: O(N), we visit all nodes exactly once
  // Space Complexity: O(N), the bottom level can contain at most N/2 nodes and therefore queue can contain N/2 nodes at most
};
//dfs
var connect = function (root) {
  setNext(root);
  return root;
};

//a function to set the child nodes' next pointers instead of the current node's. Set child nodes arrangement before resursion
function setNext(root) {
  if (!root || !root.left) return root;

  //declare the child name
  let left = root.left;
  let right = root.right;

  // Set child nodes' pointer
  left.next = right;
  if (root.next) right.next = root.next.left; // if the current element has a sibling node next to it, set the child node next pointer to sibling node left child

  setNext(left);
  setNext(right);
  // Time Complexity: O(N), we visit every node exactly once
  // Space Complexity: O(1), we simply relink given nodes
}
