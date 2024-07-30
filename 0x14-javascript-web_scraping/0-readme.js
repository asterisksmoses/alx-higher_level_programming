#!/usr/bin/node

const fs = require('fs');
const process = require('process');

const file_Path = process.argv[2];

if (!file_Path) {
	console.error('Error: No file path available');
	process.exit(1);
}

fs.readFile(file_Path, 'utf8', (err, data) => {
	if (err) {
		console.error('Error in reading file:', err);
		return;
	}
	console.log(data);
});
