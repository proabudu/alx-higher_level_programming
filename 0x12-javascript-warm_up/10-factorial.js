#!/usr/bin/node

<<<<<<< HEAD
function factorial (n) {
=======

function factorial(n) {
>>>>>>> 27dc5cacce0c9d67dcdadd432adde77e50d0332f
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
