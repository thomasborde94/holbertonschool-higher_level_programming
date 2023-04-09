#!/usr/bin/node
function factorial (number) {
  if (number > 0) {
    return number * factorial(number - 1);
  } else { return 1; }
}

const number = parseInt(process.argv[2]);
console.log(factorial(number));
