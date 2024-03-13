#!/usr/bin/node

function factorial(n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }

  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
}


console.log(factorial(Number(process.argv[2])));
