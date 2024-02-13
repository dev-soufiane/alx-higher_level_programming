#!/usr/bin/node
exports.esrever = function (list) {
  const reversed_list = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversed_list.push(list[i]);
  }
  return reversed_list;
};
