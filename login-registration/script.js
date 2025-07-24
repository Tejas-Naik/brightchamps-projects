var loginmail,loginpswd,rname,rpswd,rcpswd,email;
var lerror=document.querySelector(".error");
var rerror=document.querySelector("#rerror");
var welcome=document.getElementById("welcome");

function login(){
  loginmail=document.getElementById("loginemail").value;
  loginpswd=document.getElementById("loginpswd").value;
  if (loginmail=="" || loginpswd==""){
    lerror.innerHTML="Enter email and password";
  }
  else if (loginmail==email && loginpswd==rpswd)  {
    window.location.href="second.html";
  }
  else  {
    lerror.innerHTML="Please register";
  }
  event.preventDefault();
}

function registration()
{
  rname=document.getElementById("rname").value;
  email=document.getElementById("email").value;
  rpswd=document.getElementById("rpswd").value;
  rcpswd=document.getElementById("rcpswd").value;
  
  if (rname=="" || email==""||rpswd==""||rcpswd=="")
  {
    rerror.innerHTML="Please enter all the fields";
  }
  else if (rcpswd!=rpswd)
  {
     rerror.innerHTML="Password and confirm password not matching";
  }
  else
  {
    sessionStorage.setItem('storedname',document.getElementById("rname").value);
    alert("Registration successful");
    var a=document.getElementById("registration");
    a.style.display="none";
    var logi=document.getElementById("login");
    logi.style.display="block";
  }

  event.preventDefault();
}

function navigation()
{
  var a=document.getElementById("registration");
  a.style.display="block";
  var logi=document.getElementById("login");
  logi.style.display="none";
}

function welcomefun()
{
  var welcome=document.getElementById("welcome");
  welcome.innerHTML="Welcome "+sessionStorage.getItem("storedname")+"!";
}

