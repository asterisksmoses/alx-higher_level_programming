#!/usr/bin/node

const SquareBase = require('./5-square');

class Square extends SquareBase {
	charPrint(c) {
		const char = c === undefined ? 'X' : c;
		for (let x = 0; x < this.height; x++) {
			console.log(char.repeat(this.width));
		}
	}
}

module.exports = Square;
