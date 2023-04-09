#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= number; i++) {
    console.log('X'.repeat(number));
  }
}
