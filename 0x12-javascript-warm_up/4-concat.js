#!/usr/bin/node
const arg = process.argv;
if (arg[2]) {
  if (arg[3]) {
    console.log(arg[2] + ' is ' + arg[3]);
  } else {
    console.log(arg[2] + ' is undefined');
  }
} else {
  console.log('undefined is undefined');
}
