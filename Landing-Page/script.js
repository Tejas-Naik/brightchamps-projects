var p=document.getElementById("programming");
  var b=document.getElementById("business");
  var d=document.getElementById("designing");

function programming()
{
  p.style.display="block";
  b.style.display="none";
  d.style.display="none";
 
}

function business()
{
  p.style.display="none";
  b.style.display="block";
  d.style.display="none";
  
}

function designing()
{
  p.style.display="none";
  b.style.display="none";
  d.style.display="block";
  
}

var element = document.querySelector("#free");
document.addEventListener("DOMContentLoaded", function() {
  setTimeout(function() {
    element.style.display = "block";
    document.documentElement.style.overflow = 'hidden';
    document.body.style.overflow = 'hidden';
   }, 3000);
 document.documentElement.style.overflow = 'visible';
 document.body.style.overflow = 'visible';
});


var close=document.getElementById("close");
close.addEventListener("click", function() {
  element.style.display="none";
  document.documentElement.style.overflow = 'visible';
  document.body.style.overflow = 'visible';
      });




var form=document.getElementById("form");
var done=document.getElementById("done");
var formdet=document.getElementById("formdetails");
var free=document.getElementById("free");
var count=0;

function delay()
{
  form.style.display="none";
  event.preventDefault();
}

function send()
{
  count+=1;
  form.style.display="block";
  formdet.style.display="none";
  done.style.display="block";
  setTimeout(delay,3000);
  
}

function details()
{ free.style.display="none";
  form.style.display="block";
  if(count>1)
  {
     done.style.display="block";
     formdet.style.display="none";
     setTimeout(delay,3000);
   
  }
 else{formdet.style.display="block";}
  document.documentElement.style.overflow = 'visible';
  document.body.style.overflow = 'visible';
 event.preventDefault();
}
