#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    this.width = w > 0 ? w : undefined;
    this.height = h > 0 ? h : undefined;
  }

  print = () => {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  };

  rotate = () => {
    [this.width, this.height] = [this.height, this.width];
  };

  double = () => {
    this.width *= 2;
    this.height *= 2;
  };
}

module.exports = Rectangle;
