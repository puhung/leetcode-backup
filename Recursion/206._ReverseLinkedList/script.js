var reverseList = function (head) {
  //T he end of the new reversed linked list would be null
  let prev = null;
  while (head) {
    let temp = head.next;
    head.next = prev; // head.next point to previous Node, instead of the next Node of the given linked list
    prev = head; // Move the prev Node pointer forward, up to head
    head = temp; // Move the head up to next Node of the given linked list
  }
  return prev;
};
