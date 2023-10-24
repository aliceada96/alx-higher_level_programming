#!/usr/bin/node
const request = require('request-promise');
const url = 'https://swapi.co/api/films/' + process.argv[2];

async function fetchFilmCharacters(url) {
  try {
    const body = await request(url);
    const film = JSON.parse(body);
    const characters = film.characters;
    await printCharacters(characters);
  } catch (error) {
    console.error('Error:', error);
  }
}

async function printCharacters(characters) {
  for (const characterURL of characters) {
    try {
      const body = await request(characterURL);
      const character = JSON.parse(body);
      console.log(character.name);
    } catch (error) {
      console.error('Error:', error);
    }
  }
}

fetchFilmCharacters(url);
