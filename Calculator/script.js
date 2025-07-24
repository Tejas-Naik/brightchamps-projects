var currentvalue = "";
var displayscreen = document.getElementById("display");
const boxElement = document.querySelector("#whole");

function display(num) {
  displayscreen.style.background = "#D3D3D3";
  boxElement.style.background = "#32DD7D";
  boxElement.style.transform = "scale(1)";
  currentvalue += num;
  displayscreen.innerHTML = currentvalue;
}

function clearscreen() {
  displayscreen.style.background = "#D3D3D3";
  boxElement.style.background = "#32DD7D";
  boxElement.style.transform = "scale(1)";
  currentvalue = "";
  displayscreen.innerHTML = currentvalue;
}

function equals() {
  try {
    displayscreen.style.background = "#D3D3D3";
    boxElement.style.transform = "scale(1.2)";
    currentvalue = eval(currentvalue);
    displayscreen.innerHTML = currentvalue;
  } catch (error) {
    displayscreen.innerHTML = "ERROR";
    boxElement.style.background = "#FF2E2E";
    displayscreen.style.background = "#FF2E2E";
  }
}
