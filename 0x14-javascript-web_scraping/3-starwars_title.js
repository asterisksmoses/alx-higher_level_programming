#!/usr/bin/node

const request = require('request');
const process = require('process');

const movieId = process.argv[2];

if (!movieId) {
	console.error('Error: No movie ID available');
	process.exit(1);
}

const api_Url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(api_Url, (error, response, body) => {
	if (error) {
		console.error('Error in making the request:', error);
		return;
	}

	if (response.statusCode === 200) {
		const movie_Data = JSON.parse(body);
		console.log(movie_Data.title);
	} else {
		console.error(`Error: Reeceived status code ${response.statusCode}`);
	}
});
