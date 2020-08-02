// index.js
// to execute ==>  cd ecomm; npm run dev
const express = require('express');
const app = express();

app.get('/ecomm',(req, res) => {
  res.send("Hi from express server! Test ecomm app");
});

app.listen(3000, () =>{
  console.log('Hello world from express!!')
});
