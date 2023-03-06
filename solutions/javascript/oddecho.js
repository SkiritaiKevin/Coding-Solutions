// https://open.kattis.com/problems/oddecho
// 1.3 (Easy)

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let words = [];

rl.question('', (n) => {
  rl.on('line', (line) => {
    words.push(line);
    if (words.length == n) {
      for (let i = 0; i < n; i += 2) {
        console.log(words[i]);
      }
      rl.close();
    }
  });
})
