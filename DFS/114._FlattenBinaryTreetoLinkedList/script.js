var flatten = function (root) {
  let curr = root;
  while (curr) {
    //if there is left child, flatten the element
    if (curr.left) {
      //find the most right leaf of current left node
      let last = curr.left;
      while (last.right) {
        last = last.right;
      }

      //connect previous right node to the right of the most right leaf we found
      last.right = curr.right;
      //move the left child to the curr's right.
      curr.right = curr.left;

      curr.left = null;
    }
    //iterate through the right element until the end.
    curr = curr.right;
  }
};
