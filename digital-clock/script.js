var seconds = 0,
  minutes = 0,
  hours = 0,
  selectedOption = "24hour";
function clock() {
  var dhours = document.getElementById("hours");
  var dminutes = document.getElementById("minutes");
  var dseconds = document.getElementById("seconds");
  var ampm = document.getElementById("ampm");
  var optionsDropdown = document.getElementById("options");

  var presentTime = new Date();
  var seconds = String(presentTime.getSeconds()).padStart(2, "0");
  var minutes = String(presentTime.getMinutes()).padStart(2, "0");
  var hours = String(presentTime.getHours()).padStart(2, "0");

  dhours.innerHTML = hours;
  dminutes.innerHTML = minutes;
  dseconds.innerHTML = seconds;

  optionsDropdown.addEventListener("change", (event) => {
    selectedOption = event.target.value;
  });

  if (selectedOption == "12hour") {
    if (hours >= 12) {
      dhours.innerHTML = hours - 12;
      ampm.innerHTML = "PM";
    } else {
      ampm.innerHTML = "AM";
    }
    ampm.style.display = "inline";
    dminutes.innerHTML = minutes;
    dseconds.innerHTML = seconds;
  } else {
    dhours.innerHTML = hours;
    ampm.style.display = "none";
  }
}
setInterval(clock, 1000);
