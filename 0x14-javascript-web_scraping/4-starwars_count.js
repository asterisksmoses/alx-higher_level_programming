#!/usr/bin/node

const request = require('request');
const process = require('process');

const api_Url = process.argv[2]

if (!api_Url) {
	console.error('Error: No API URL Available');
	process.exit(1);
}

const wedgeAntilles_Id = 18;

request.get(api_Url, (error, response, body) => {
	if (error) {
		console.error('Error in making request:', error);
		return;
	}
	if (response.statusCode == 200) {
		const data = JSON.parse(body);
		const movies = data.results;
		let count = 0;


		for (const movie of movies) {
			if (movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntilles_Id}/`)) {
				count++;
			}
		}

		console.log(count);
	} else {
		console.error(`Error: Received status code ${response.statusCode}`);
	}
});
