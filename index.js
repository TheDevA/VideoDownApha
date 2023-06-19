import express from 'express'
const app = express()
const port = 3000
import {PythonShell} from 'python-shell';

// let options = {
//   mode: 'text',
//   args: ['value1','value2','value3']
// };

// PythonShell.run('main.py', options).then(messages=>{
//   // results is an array consisting of messages collected during execution
//   console.log(messages)
//   let arrayMessage = messages[0].replace(/\[|\]|\'/g,"").trim()  
//   arrayMessage = arrayMessage.split(",")
//   arrayMessage.forEach(x=>console.log(x.trim()))
// });

// deffining the routs for static files
app.use(express.static("static"))
app.use(express.static("static/js"))
app.use(express.static("static/css"))
app.use(express.static("static/files"))


app.get('/video', (req, res) => {
  let options = {
  mode: 'json',
  args: [req.query.url,'INFO']
  };

  PythonShell.run('main.py', options).then(messages=>{
    console.log(messages)
    res.send(messages)
    // results is an array consisting of messages collected during execution
    // console.log(messages)
    // let arrayMessage = messages[0].replace(/\[|\]|\'/g,"").trim()  
    // arrayMessage = arrayMessage.split(",")
    // arrayMessage.forEach(x=>console.log(x.trim()))
  });
  
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
