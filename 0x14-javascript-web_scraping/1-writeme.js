#!/usr/bin/node

const fs = require('fs');
const process = require('process');

const file_Path = process.argv[2]
const string_To_Write = process.argv[3]

if (!file_Path || !string_To_Write) {
	console.error('Error: Both file path and string to write are not available');
	process.exit(1);
}

fs.writeFile(file_Path, string_To_Write, 'utf8', (err) => {
	if (err) {
		console.error('Error occured while writing to file:', err);
		return;
	}
	console.log(`Successfully wrote to $file_Path`);
});
