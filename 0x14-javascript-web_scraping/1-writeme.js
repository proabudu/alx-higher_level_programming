#!/usr/bin/node

const fs = require('fs');

// Check for arguments
if (process.argv.length < 4) {
  console.error('Usage: node write_string.js <file path> <string to write>');
  process.exit(1);
}

// Get file path and string to write
const filePath = process.argv[2];
const content = process.argv[3];

// Write the string to the file with UTF-8 encoding
fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error('Error writing to file:', err);
  } else {
    console.log(`Successfully wrote content to ${filePath}`);
  }
});
