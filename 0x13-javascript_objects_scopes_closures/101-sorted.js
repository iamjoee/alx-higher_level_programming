#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = Object.keys(dict).reduce((result, key) => {
  const value = dict[key];
  result[value] = result[value] || [];
  result[value].push(key);
  return result;
}, {});

console.log(newDict);
