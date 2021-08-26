var zigzagLevelOrder = function (root) {
  if (!root) return [];
  let result = [];
  let queue = [root];
  let height = 0;

  while (queue.length) {
    let currLevel = [];
    let n = queue.length;

    for (let i = 0; i < n; i++) {
      let current = queue.shift();
      if (current === null) continue;
      if (height % 2 == 0) {
        currLevel.push(current.val);
      } else currLevel.unshift(current.val);

      if (current.left) queue.push(current.left);
      if (current.right) queue.push(current.right);
    }

    result.push(currLevel);
    height++;
  }

  return result;
};
