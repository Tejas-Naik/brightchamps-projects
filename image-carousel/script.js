const images = document.querySelectorAll('.carousel-1 .imagesBox img');
let currentIndex = 0;

function showNextImage() {
  images[currentIndex].style.display = 'none';
  currentIndex++;

  if (currentIndex >= images.length) {
    currentIndex = 0;
  }
  images[currentIndex].style.display = 'block';
}

setInterval(showNextImage, 3000);

// Initialize a variable to keep track of the current slide index.
let currentSlide = 0;

// Get references to HTML elements using their class and ID attributes.
const slider = document.querySelector('.slider');  // Selects an element with the class "slider."
const prevBtn = document.getElementById('prevBtn'); // Selects an element with the ID "prevBtn."
const nextBtn = document.getElementById('nextBtn'); // Selects an element with the ID "nextBtn."

// Initialize a variable to keep track of the slide index.
let slideIndex = 0;

// Define a function to show a specific slide based on its index.
function showSlide(n) {
  // Select all elements with the class "slider" that contain slides.
  const slides = document.querySelectorAll('.slider .box');
  
  // If the given index (n) is greater than or equal to the total number of slides,
  // reset the index to the first slide (index 0).
  if (n >= slides.length) {
    slideIndex = 0;
  }
  // If the given index (n) is less than 0, set the index to the last slide.
  else if (n < 0) {
    slideIndex = slides.length - 1;
  }

  // Hide all slides by setting their display style to 'none'.
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = 'none';
  }

  // Display the slide at the current index by setting its display style to 'block'.
  slides[slideIndex].style.display = 'block';
}

// Define a function to show the next slide.
function nextSlide() {
  // Increment the slide index.
  slideIndex++;
  // Call the showSlide function to display the updated slide.
  showSlide(slideIndex);
}

// Define a function to show the previous slide.
function prevSlide() {
  // Decrement the slide index.
  slideIndex--;
  // Call the showSlide function to display the updated slide.
  showSlide(slideIndex);
}

// Show the initial slide (at index 0) when the script is first executed.
showSlide(slideIndex);

// Add click event listeners to the previous and next buttons to handle slide navigation.
nextBtn.addEventListener('click', nextSlide);
prevBtn.addEventListener('click', prevSlide);



// Select all list items within elements with class "faq-text"
let li = document.querySelectorAll(".faq-text li");

// Loop through each list item
for (var i = 0; i < li.length; i++) {
  // Add a click event listener to each list item
  li[i].addEventListener("click", (e) => {
    let clickedLi;

    // Check if the clicked element has class "question-arrow"
    if (e.target.classList.contains("question-arrow")) {
      // If yes, set "clickedLi" to the parent of the clicked element
      clickedLi = e.target.parentElement;
    } else {
      // If not, set "clickedLi" to the parent of the parent of the clicked element
      clickedLi = e.target.parentElement.parentElement;
    }

    // Toggle the class "showAnswer" for the clicked list item
    // (This class controls whether the answer is shown or hidden)
    clickedLi.classList.toggle("showAnswer");
  });
}
