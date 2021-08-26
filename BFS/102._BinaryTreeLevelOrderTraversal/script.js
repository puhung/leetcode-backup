//BFS
var levelOrder = function (root) {
  if (!root) return [];

  let queue = [root];
  let result = [];

  while (queue.length !== 0) {
    //since we need a seperate array for each level, we set a array for the current level
    let currlevel = [];
    //since we will edit the queue in the for loop, thus we need to store the queue length prior dequeuing
    let Qlength = queue.length;

    //create a for loop to loop the current-level elements in queue
    for (let i = 0; i < Qlength; i++) {
      currElement = queue.shift();
      if (currElement.left) {
        queue.push(currElement.left);
      }
      if (currElement.right) {
        queue.push(currElement.right);
      }
      //push the current element in the current-level array
      currlevel.push(currElement.val);
    }
    //push the current level array in the result
    result.push(currlevel);
  }
  return result;
};
