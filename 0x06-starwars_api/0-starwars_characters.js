#!/usr/bin/node
// Prints all characters of a Star Wars movie

const request = require('request');
const movieId = process.argv[2];

const requestPromise = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
};

if (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  (async () => {
    try {
      const body = await requestPromise(url);
      const characters = JSON.parse(body).characters;
      for (const character of characters) {
        const body = await requestPromise(character);
        const name = JSON.parse(body).name;
        console.log(name);
      }
    } catch (error) {
      console.error(error);
    }
  })();
}
