var pathSum = function (root, targetSum) {
  //the count must be outside the recursion function orelse the count will always be refreshed
  let count = 0;
  main(root, targetSum);
  return count;

  //this function allow us to find the path from this element and repeat counting the number of paths that start from the left and right node
  function main(root, target) {
    if (!root) return 0;
    pathFinder(root, target);
    main(root.left, target);
    main(root.right, target);
    return;
  }

  function pathFinder(curr, sum) {
    if (!curr) return;
    sum -= curr.val;
    if (sum === 0) {
      count++;
    }
    pathFinder(curr.left, sum);
    pathFinder(curr.right, sum);
  }
};
