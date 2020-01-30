function myFunction() {
  var inpObj = document.getElementById("id2");
  if (!inpObj.checkValidity()) {
    document.getElementById("disp").innerHTML = inpObj.validationMessage;
  } else {
    document.getElementById("disp").innerHTML = "Input OK";
  } 
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