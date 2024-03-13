#!/usr/bin/node

function factorial(n) {
  if (isNaN(n) || n < 0) {
    throw new Error("Input must be a non-negative number");
  }

  // Iterative approach to avoid potential stack overflow
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
}

const number = Number(process.argv[2]);
try {
  console.log(factorial(number));
} catch (error) {
  console.error("Error:", error.message);
}
