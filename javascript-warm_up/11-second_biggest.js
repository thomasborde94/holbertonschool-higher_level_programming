#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  let first = -1; let second = -1;
  for (let i = 0; i <= process.argv.length - 1; i++) {
    if (process.argv[i] > first) {
      second = first;
      first = process.argv[i];
    } else if (process.argv[i] > second && process.argv[i] !== first) {
      second = process.argv[i];
    }
  }
  console.log(second);
}
