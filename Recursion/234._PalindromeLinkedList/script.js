var isPalindrome = function (head) {
  //finding middle process
  let slow = head,
    fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  //reversing process
  //reverse the entire back half array
  let prev = slow;
  slow = slow.next;
  prev.next = null; // Separate the array into fisrt and back half array. This step also stop checking process in the middle
  while (slow) {
    let temp = slow.next;
    slow.next = prev;
    prev = slow;
    slow = temp;
  }

  //checking process
  //Check whether the two half arrays are the same.
  fast = head;
  slow = prev;
  //when the slow reaches to the middle, there is no more next node.
  while (slow) {
    if (fast.val != slow.val) return false;
    else {
      fast = fast.next;
      slow = slow.next;
    }
  }
  return true;
};
