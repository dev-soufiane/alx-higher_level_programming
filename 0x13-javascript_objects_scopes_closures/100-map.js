#!/usr/bin/node
const { list } = require('./100-data');
const newList = list.map((i, nbr) => i * nbr);
console.log(list);
console.log(newList);
