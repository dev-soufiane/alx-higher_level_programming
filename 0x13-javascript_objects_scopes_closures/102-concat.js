#!/usr/bin/node
const fileSys = require('fileSys');

const fArg = fileSys.readFileSync(process.argv[2]).toString();
const sArg = fileSys.readFileSync(process.argv[3]).toString();
fileSys.writeFileSync(process.argv[4], fArg + sArg);
