#!/usr/bin/node

const request = require('request');

// Check if URL argument is provided
if (process.argv.length < 3) {
  console.error('Usage: node script.js <URL>');
  process.exit(1);
}

// Get the URL from the first argument
const url = process.argv[2];

// Make the GET request
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    // Print the status code
    console.log(`code: ${response.statusCode}`);
  }
});
