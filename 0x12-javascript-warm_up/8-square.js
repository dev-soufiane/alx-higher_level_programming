#!/usr/bin/node
const size = Number(process.argv[2]);
if (size) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
