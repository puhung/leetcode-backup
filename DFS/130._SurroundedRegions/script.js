var solve = function (board) {
  if (!board) return;
  //check the outer column
  for (let i = 0; i < board.length; i++) {
    dfs(i, 0); //to check the leftest column
    dfs(i, board[0].length - 1); // to check the rightest column
  }
  //check the outer row
  for (let j = 0; j < board[0].length; j++) {
    dfs(0, j); //check the uppest row
    dfs(board.length - 1, j); // check the bottomest row
  }
  //set 'O' to 'X', then set '*' to 'X'
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      if (board[i][j] == "O") board[i][j] = "X";
      else if (board[i][j] == "P") board[i][j] = "O";
    }
  }
  return board;

  function dfs(i, j) {
    if (
      i >= 0 &&
      i < board.length &&
      j >= 0 &&
      j < board[0].length &&
      board[i][j] == "O"
    ) {
      board[i][j] = "P";
      dfs(i - 1, j);
      dfs(i + 1, j);
      dfs(i, j - 1);
      dfs(i, j + 1);
    }
    return;
  }
};
