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