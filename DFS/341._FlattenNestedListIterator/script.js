class NestedIterator {
  constructor(nestedList) {
    this.data = [];
    this.flatten(nestedList);
  }

  flatten(list) {
    for (let element of list) {
      if (element.isInteger()) {
        this.data.push(element.getInteger());
      } else this.flatten(element.getList());
    }
  }
  hasNext() {
    return this.data.length;
  }

  next() {
    return this.data.shift();
  }
}
