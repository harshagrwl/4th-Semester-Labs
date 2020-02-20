let hash = {};

// function checkpwd(pwd){
// 	if(pwd.length >= 8){
// 		return true;
// 	}
// 	else
// 		retun false;
// }


function myFunction() {
	let u = document.getElementById("un").value;
	let p = document.getElementById("pw").value;

  var inpObj = document.getElementById("id2");
  if (!inpObj.checkValidity()) {
    document.getElementById("disp").innerHTML = inpObj.validationMessage;
  }
  if (p.length > 8){
  	hash[u] = p;
  	alert('Registration Successful. Please proceed to Login');
  }
  else{
  	alert('Password must be of minimum 8 characters. Please Try again');
  }
  
  return false;
} 

function subfn() {
	let subv = document.getElementById("f3").elements["sub"].value;
	let price = document.getElementById("dis");

	if(subv == "weekly"){
		price.innerHTML = "Rs. 50/-"
	}
	if(subv == "monthly"){
		price.innerHTML = "Rs. 180/-"
	}
	if(subv == "yearly"){
		price.innerHTML = "Rs. 2000/-"
	}
}

function randfun() {
  var x = document.getElementById("randdis")
  x.innerHTML = Math.floor((Math.random() * 10) + 1);
}
function login() {
	let u = document.getElementById("uname").value;
	let p = document.getElementById("pwd").value;

	if(hash[u] == p){
		alert('Login Successful')
	}
	else{
		alert('Login Unsuccessful. Please Enter a valid Username or Password')
	}
}


function setCookie(cname,cvalue) {
  var d = new Date();
  // d.setTime(d.getTime() + (exdays*24*60*60*1000));
  // var expires = "expires=" + d.toGMTString();
  document.cookie = cname + "=" + cvalue + ";path=/";
}
let countc = 0;
function getCookie(cname,count) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  count++;
  for(var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }

  return "";
}

var numLoads = parseInt(getCookie('pageLoads'), 10);

if (isNaN(numLoads) || numLoads <= 0) { setCookie('pageLoads', 1); }
else { setCookie('pageLoads', numLoads + 1); }

var x = getCookie('pageLoads');

function namecheck() {
	
	
  var user=getCookie("username",countc);
  if (user != "") {
    alert("Welcome again " + user + " .Thanks to visit again." + " You have vissited this Website " + x + " times.");
  } else {
     user = prompt("Please enter your name:","");
     if (user != "" && user != null) {
       document.cookie = "username" + "=" + user + ";" + ";path=/";
     }
  }
}

