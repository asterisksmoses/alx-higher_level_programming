#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const process = require('process');

const url = process.argv[2];
const file_Path = process.argv[3];

if (!url || !file_Path) {
	console.error('Error: Both URL and file path are not available');
	process.exit(1);
}

request.get(url, (error, response, body) => {
	if (error) {
		console.error('Error in making the request:', error);
		return;
	}

	if (response.statusCode === 200) {
		fs.writeFile(file_Path, body, 'utf8', (err) => {
			if (err) {
				console.error('Error while writing to file:', err);
				return;
			}
			console.log(`Content successfully saved to ${file_Path}`);
		});
	} else {
		console.error(`Error: Received status code ${response.statusCode}`);
	}
});
