//loop solution
// if n is the power of 3, after looping, the n will become 1;
var isPowerOfThree = function (n) {
  //keep looping until n = 0 or n % 3 != 0
  while (n > 1) {
    if (n % 3 == 0) n /= 3;
    else break; //if n is not the power of 3, break
  }

  //check if n becomes 1;
  return n === 1;
};

//Integer Limitations
//the larger power of three can be devided by small power of three. Thus we find the largest power of three 3^19 = 1162261467, then use n to devide it, check if there is any remainder

var isPowerOfThree = function (n) {
  return n > 0 && 1162261467 % n == 0;
};
