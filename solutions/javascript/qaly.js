// https://open.kattis.com/problems/qaly
// 1.3 (Easy)

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let n = 0; // number of periods
let qaly = 0; // accumulated QALY

rl.on('line', (line) => {
  if (n === 0) {
    n = parseInt(line); // read number of periods
  } else {
    const [q, y] = line.split(' ').map(parseFloat); // read quality and years
    qaly += q * y; // accumulate QALY
    n--; // decrement periods counter
    if (n === 0) {
      console.log(qaly.toFixed(3)); // output accumulated QALY with 3 decimal places
      rl.close(); // close input stream
    }
  }
});
