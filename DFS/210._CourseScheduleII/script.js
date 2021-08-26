var findOrder = function (numCourses, prerequisites) {
  let graph = new Map();
  let visiting = new Set();
  let visited = new Set();
  let result = [];

  for (let [v, e] of prerequisites) {
    if (graph.has(v)) {
      let i = graph.get(v);
      i.push(e);
      graph.set(v, i);
    } else {
      graph.set(v, [e]);
    }
  }

  /*
  for(const [v,e] of graph){
        if(DFS(v)){
            return false; //if cyclic it will not finish so it is false
        }
    }
  */
  //This code below is better than the upper code, since this code can deal with non-prerequisites [].
  //However, the problem with this code is that we would do repeat dfs for same element. Ex: Input: numCourses = 1, prerequisites = []. Thus, `!visited.has(i)` is needed!!
  for (let i = 0; i < numCourses; i++) {
    if (!visited.has(i) && dfs(i)) {
      return [];
    }
  }

  return result;

  function dfs(v) {
    visiting.add(v);
    let edges = graph.get(v);
    if (edges) {
      for (let e of edges) {
        if (visited.has(e)) continue;

        if (visiting.has(e)) return true;

        if (dfs(e)) return true;
      }
    }

    visiting.delete(v);
    visited.add(v);
    result.push(v);
    return false;
  }
};
