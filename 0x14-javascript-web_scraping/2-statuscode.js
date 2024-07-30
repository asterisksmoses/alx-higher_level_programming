#!/usr/bin/node

const request = require('request');
const process = require('process');

const url = process.argv[2];

if (!url) {
	console.error('Error: No URL available');
	process.exit(1);
}

request.get(url, (error, response, body) => {
	if (error) {
		console.error('Error in making a request:', error);
		return;
	}

	console.log(`code: ${response.statusCode}`);
});
