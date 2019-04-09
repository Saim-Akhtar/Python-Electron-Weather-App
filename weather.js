function get_weather() {
    var {PythonShell} = require("python-shell")
    var path = require("path")
    
    var city = document.getElementById("city").value
    document.getElementById("city").value = "";
    let cols = document.querySelectorAll(".query");
    console.log(cols.length);
    var options = {
      scriptPath : path.join(__dirname, './pythonCode/'),
      args : [city]
    }
    var weather = new PythonShell('weather request.py', options);
  
    weather.on('message', function(message) {
        if(message !== "error"){
        let values=message.split('&')
        for(let i=0;i<values.length;i++){
            cols[i].innerHTML=values[i];
        }}
        else{
            alert("Error City Not found")
        }
    })
  }
  document.getElementById("button_check").addEventListener('click',get_weather);