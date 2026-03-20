const container = document.getElementById("container");
const colorPicker = document.getElementById("colorPicker");
const resetButton = document.getElementById("resetButton");
const SQUARES = 400;

for (let i = 0; i < SQUARES; i++) {
  const square = document.createElement("div");
  square.classList.add("square");

  square.addEventListener("mouseover", () => setColor(square));
  square.addEventListener("mouseout", () => removeColor(square));

  container.appendChild(square);
}

function setColor(element) {
  const color = colorPicker.value;
  element.style.background = color;
  element.style.boxShadow = `0 0 2px ${color}, 0 0 10px ${color}`;
  // Instant color change, keep transform smooth
  element.style.transition =
    "transform 0.5s ease, background-color 0s, box-shadow 0s";
}

function removeColor(element) {
  element.style.background = "#1d1d1d";
  element.style.boxShadow = "0 0 2px #000";
  // Slow fade out
  element.style.transition =
    "transform 0.5s ease, background-color 5s ease, box-shadow 2s ease";
}

resetButton.addEventListener("click", () => {
  document.querySelectorAll(".square").forEach(removeColor);
});
