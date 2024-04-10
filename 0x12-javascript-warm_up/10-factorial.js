#!/usr/bin/node

'use strict'; // Enable strict mode
// Function to calculate factorial of a number
function factorial (n) {
  // If n is 0 or NaN, return 1 (base case for factorial)
  return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
} // End of factorial function

// Get the input number from command line arguments and calculate its factorial
console.log(factorial(Number(process.argv[2])));
