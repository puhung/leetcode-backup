var numIslands = function (grid) {
  if (!grid) return;
  let row = grid.length;
  let col = grid[0].length;
  let count = 0;

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (grid[i][j] == "1") {
        dfs(i, j);
        count++;
      }
    }
  }
  return count;

  //circle the entire island from grid[i][j]
  function dfs(i, j) {
    if (i >= 0 && i < row && j >= 0 && j < col && grid[i][j] == "1") {
      grid[i][j] = "I";
      dfs(i - 1, j);
      dfs(i + 1, j);
      dfs(i, j - 1);
      dfs(i, j + 1);
    }
  }
};
