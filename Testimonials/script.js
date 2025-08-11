var arr = [
  "I am Clara a dedicated developer, found myself increasingly frustrated with my demanding work.",
  "Feeling overwhelmed by deadlines and code bugs, my days grew more stressful.",
  "One day, seeking solace, I joined a Palm yoga class. As I embraced the soothing poses and focused breaths, a sense of tranquility gradually enveloped me.",
  "With time, the harmony I discovered on the yoga mat began to seep into my work life, transforming my frustration into happiness and calm.",
];
var imgs = ["woman1.png", "woman2.png", "woman3.jpeg", "woman4.png"];
var text = document.getElementById("lines");
var image = document.getElementById("image");
var i = 0;
function next() {
  if (i == 3) {
    i = 0;
  } else {
    i++;
  }
  text.innerHTML = arr[i];
  image.src = imgs[i];
  image.style.width = "500px";
  image.style.height = "400px";
}

function previous() {
  if (i == 0) {
    i = 3;
  } else {
    i--;
  }
  text.innerHTML = arr[i];
  image.src = imgs[i];
  image.style.width = "500px";
  image.style.height = "400px";
}

function add() {
  var fbsection = document.getElementById("feedback");
  var newdiv = document.createElement("div");
  var name = document.createElement("h5");
  var para = document.createElement("p");
  var hr = document.createElement("hr");
  name.textContent = document.getElementById("name").value;
  para.textContent = document.getElementById("para").value;
  newdiv.appendChild(name);
  newdiv.appendChild(para);
  fbsection.appendChild(newdiv);
  fbsection.appendChild(hr);
}
