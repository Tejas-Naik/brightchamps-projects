const header = document.getElementById("head");

window.addEventListener("scroll", () => {
  if (window.scrollY > 0) {
    header.classList.add("scrolled");
  } else {
    header.classList.remove("scrolled");
  }
});

const optionsDropdown = document.getElementById("options");
const contentSections = document.querySelectorAll(".content");

function showContent(selectedValue) {
  contentSections.forEach((section) => {
    section.style.display = "none"; // Hide all content sections
  });

  const selectedContent = document.getElementById(`content-${selectedValue}`);
  if (selectedContent) {
    selectedContent.style.display = "block"; // Show the selected content
  }
}

if (optionsDropdown) {
  optionsDropdown.addEventListener("change", function () {
    const selectedOptionValue = this.value;
    showContent(selectedOptionValue);
  });
  // Show the first option by default
  showContent(optionsDropdown.value);
}

//------------------------------------------------------------

const navLinks = document.querySelectorAll(".nav-menu a");
const content = document.querySelectorAll(".imgcont");

// Display the first content section by default
content[0].classList.add("active");

navLinks.forEach((link) => {
  link.addEventListener("click", function (e) {
    e.preventDefault();
    const targetSectionId = this.getAttribute("href");

    // Remove active class from all content sections
    content.forEach((section) => {
      section.classList.remove("active");
    });

    // Add active class to the targeted content section
    const targetSection = document.querySelector(targetSectionId);
    if (targetSection) {
      targetSection.classList.add("active");
    }
  });
});
