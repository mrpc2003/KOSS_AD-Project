module.exports = {
    first:function(){
      return `
      <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>StartPage</title>
    <link rel="stylesheet" href="firstpage.css">
  </head>
  <body>
    <div id="page2" class="slide-in">
      <h1>Welcome to Entrance Detection!</h1>
      <a href="switch">Home</a>
      <div>
        <img class="thief" src="svg/thief.svg">
        <img class="car" src="svg/policecar.svg">
        <img class="shocked" src="svg/shocked.svg">
      </div>
    </div>
  </body>
</html>
      `;
    },switch:function(){
        return `
        <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SWITCH</title>
  <link rel="stylesheet" href="switch.css">
</head>

<body>
<div class="container">
  <div class="title">
    <h1>Entrance Detection</h1>
  </div>
  <img id="img" style="height:200px; margin-left:350px; margin-top:100px" src="svg/unlock.svg">

  <input type="checkbox" onClick="toggleImg(); door();" id="toggle" hidden> 
  <label for="toggle" class="toggleSwitch">
    <span class="toggleButton"></span>
    <img class="click" src="svg/click.svg">
    <span class="text">click here!</span>
  </label>

  <img style="height:320px; position: absolute; transform: translate(280%, -10%);" src="svg/house.svg">
  <img id="img1" style="height:200px; width: 130px; position: absolute; transform: translate(760%, 55%);" src="svg/opened-door.svg">
</div>
</body>

<script>
  const ws = new WebSocket("ws://localhost:3001")
  var count = 'on';

  let flag = true;
  function toggleImg() {
  if (count === 'on'){
    ws.send("1"); // 서버에 데이터 전송
    count = 'off'
  }else {
    ws.send("2")
    count='on'
  }
  document.getElementById("img").src = flag
  ? "svg/lock.svg"
  : "svg/unlock.svg";

  flag = !flag;
  }

  let flag1 = true;
  function door() {
  document.getElementById("img1").src = flag1
  ? "svg/closed-door.svg"
  : "svg/opened-door.svg";

  flag1 = !flag1;
  }
</script>


<nav role='navigation'>
  <div id="menuToggle">
    
    <input type="checkbox" />
    
    <span></span>
    <span></span>
    <span></span>
  
    <ul id="menu">
      <a href="/switch"><li>Home</li></a>
      <a href="/"><li>firstpage</li></a>
      <a href="#"><li>About</li></a>
      <a href="#"><li>Info</li></a>
      <a href="/noinvasion"><li>NoInvasion</li></a>
      <a href="#"><li>Show me more</li></a>
    </ul>
  </div>
</nav>


</html>

        `
    }, noinvasion:function(){
        return `
        <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NoInvasion</title>
  <link rel="stylesheet" href="noinvasion.css">
  <script>

    const ws = new WebSocket("ws://localhost:3001")


    ws.onmessage = function (event) {
        
        console.log(event.data)
        if (event.data === 'PIR: on'){
            document.getElementById('name').innerHTML=event.data
            document.getElementById('b').src="svg/cloudy.svg" ;
            document.getElementsByClassName("container")[0].style.backgroundImage = "linear-gradient(to bottom,  rgba(255,168,76,0.6) 0%,rgba(255,123,13,0.6) 100%), url('https://images.unsplash.com/photo-1446824505046-e43605ffb17f')";
            document.getElementById('c').src="svg/thief.svg";
            document.getElementById('c').style="height:200px; margin-left: -40ch; margin-top:200px; transform: scaleX(-1);"
            document.getElementById('introImg').src="svg/s2.gif"
        }else if (event.data === 'PIR: off'){
            document.getElementById('name').innerHTML=event.data
            document.getElementById('b').src="svg/bird.svg" ;
            document.getElementsByClassName("container")[0].style.backgroundImage = "linear-gradient(to bottom,  rgba(80, 190, 89, 0.6) 0%,rgba(22, 140, 26, 0.6) 100%), url('https://images.unsplash.com/photo-1446824505046-e43605ffb17f')";
            document.getElementById('c').src="";
            document.getElementById('c').style=""
            document.getElementById('introImg').src=""
        }

        if (event.data === 'test: box'){
            document.getElementById('test').innerHTML=event.data
            document.getElementById('box').src='svg/box.svg'
            document.getElementById('box').type='image'
        }
        
      }

  </script>
</head>

<body>
    <p id="name"></p>
    <p id="test"></p>
    <div class="container">
        
        <h1>Entrance Detection</h1>

        <img id='b' style="height:100px; margin-left:100px; margin-top:-300px" src="svg/bird.svg">
        <img style="height:300px; margin-left:-10px; margin-top:200px" src="svg/door.svg">
        <img id='c' style="" src="">
        <img style="width: 300px; margin-left: 10ch;" id="introImg" border="0">
        <input id="box" type="hidden" style="height:100px; margin-left: -40ch; margin-top:200px; transform: scaleX(-1);" src="" onclick="
        document.getElementById('box').type='hidden'
        ">
            
        <div class="bird-container bird-container--one">
            <div class="bird bird--one"></div>
        </div>
        
        <div class="bird-container bird-container--two">
            <div class="bird bird--two"></div>
        </div>
        
        <div class="bird-container bird-container--three">
            <div class="bird bird--three"></div>
        </div>
        
        <div class="bird-container bird-container--four">
            <div class="bird bird--four"></div>
        </div>

        <a href="/switch">Home</a>

    </div>
</body>
</html>

        `
    }
  }