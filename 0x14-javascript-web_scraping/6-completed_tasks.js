#!/usr/bin/node

const request = require('request');
const process = require('process');

const api_Url = process.argv[2];

if (!api_Url) {
	console.error('Error: No API URL available');
	process.exit(1);
}

request.get(api_Url, (error, response, body) => {
	if (error) {
		console.error('Error in making the request:', error);
		return;
	}

	if (response.statusCode == 200) {
		const data = JSON.parse(body);
		const completed_Tasks = {};

		data.forEach(task => {
			if (task.completed) {
				if(completed_Tasks[task.userId]) {
					completed_Tasks[task.userId]++;
				} else {
					completed_Tasks[task.userId] = 1;
				}
			}
		});

		console.log(completed_Tasks);
	} else {
		console.error(`Error: Received status code ${response.statusCode}`);
	}
});
