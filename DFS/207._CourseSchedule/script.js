var canFinish = function (numCourses, prerequisites) {
  let graph = new Map();
  let visiting = new Set(); // is being explored
  let visited = new Set(); // is already explored
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
  for (let i = 0; i < numCourses; i++) {
    if (dfs(i)) {
      return false; // if dfs is true, there is a cycle. It's not possible to finish all the courses. Return false.
    }
  }

  return true;

  //if the edges meet the element under visiting state, this means that there is a cycle, which means that it's not possible to finish all the courses.
  function dfs(v) {
    visiting.add(v);
    let edges = graph.get(v);
    if (edges) {
      for (let e of edges) {
        if (visited.has(e)) continue; //skip if it is explored already

        //2 conditions that proves there is a cycle.
        if (visiting.has(e)) return true; //found e is being explored
        if (dfs(e)) return true; // DFS deeper if this e is cyclic
      }
    }

    visiting.delete(v); // remove from visiting set when all decedant v are visited
    visited.add(v);
    result.push(v);
    return false;
  }
};
