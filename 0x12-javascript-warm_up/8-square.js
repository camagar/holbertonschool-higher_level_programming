#!/usr/bin/node
const Size = parseInt(process.argv[2]);
if (isNaN(Size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Size; i++) {
    console.log('X'.repeat(Size));
  }
}
