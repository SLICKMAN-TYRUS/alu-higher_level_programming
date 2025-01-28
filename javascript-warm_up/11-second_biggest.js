#!/usr/bin/node
const argArray = process.argv.slice(2);
if (argArray.length < 2) {
  console.log(0);
} else {
  argArray.sort((a, b) => (a - b));
  argArray.pop();
  console.log(argArray.pop());
}
