// Initializing Python Script=
const spawn = require('child_process').spawn;
const process = spawn('python', ['./hello.py', "Randy"])
process.stdout.on('data', data => {
console.log(data.toString());
})

function validate() {
    const spawn = require('child_process').spawn;
    const process = spawn('python', ['./hello.py', "Randy"])
    process.stdout.on('data', data => {
    console.log(data.toString());
    })
}




