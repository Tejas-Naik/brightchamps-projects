const qualityStars = document.querySelectorAll(".quality-stars i");
const qualityRatingElement = document.querySelector(".quality-rating");
const qualityCommentInput = document.querySelector(".quality-comment");
const qualitySubmitButton = document.querySelector(".quality-submit");
const qualityCommentDisplay = document.querySelector(
  ".quality-comment-display"
);

const deliveryStars = document.querySelectorAll(".delivery-stars i");
const deliveryRatingElement = document.querySelector(".delivery-rating");
const deliveryCommentInput = document.querySelector(".delivery-comment");
const deliverySubmitButton = document.querySelector(".delivery-submit");
const deliveryCommentDisplay = document.querySelector(
  ".delivery-comment-display"
);

const serviceStars = document.querySelectorAll(".service-stars i");
const serviceRatingElement = document.querySelector(".service-rating");
const serviceCommentInput = document.querySelector(".service-comment");
const serviceSubmitButton = document.querySelector(".service-submit");
const serviceCommentDisplay = document.querySelector(
  ".service-comment-display"
);

let qualityRating = 0;
let deliveryRating = 0;
let serviceRating = 0;
let qualityComment = "";
let deliveryComment = "";
let serviceComment = "";

function updateCategoryRating(stars, ratingElement, category) {
  stars.forEach((star, index1) => {
    star.addEventListener("click", () => {
      stars.forEach((star, index2) => {
        index1 >= index2
          ? star.classList.add("active")
          : star.classList.remove("active");
      });
      const categoryRating = index1 + 1;
      ratingElement.textContent = categoryRating;
      switch (category) {
        case "quality":
          qualityRating = categoryRating;
          break;
        case "delivery":
          deliveryRating = categoryRating;
          break;
        case "service":
          serviceRating = categoryRating;
          break;
        default:
          break;
      }
    });
  });
}

updateCategoryRating(qualityStars, qualityRatingElement, "quality");
updateCategoryRating(deliveryStars, deliveryRatingElement, "delivery");
updateCategoryRating(serviceStars, serviceRatingElement, "service");
function submitComment(category) {
  const commentInput = document.querySelector(`.${category}-comment`);
  const commentDisplay = document.querySelector(`.${category}-comment-display`);
  commentInput.addEventListener("input", (event) => {
    const value = event.target.value;
    switch (category) {
      case "quality":
        qualityComment = value;
        break;
      case "delivery":
        deliveryComment = value;
        break;
      case "service":
        serviceComment = value;
        break;
      default:
        break;
    }
  });

  const submitButton = document.querySelector(`.${category}-submit`);
  submitButton.addEventListener("click", () => {
    if (category === "quality") {
      qualityCommentDisplay.textContent = `Comment: ${qualityComment}`;
    } else if (category === "delivery") {
      deliveryCommentDisplay.textContent = `Comment: ${deliveryComment}`;
    } else if (category === "service") {
      serviceCommentDisplay.textContent = `Comment: ${serviceComment}`;
    }
    commentInput.style.display = "none";
    submitButton.style.display = "none";
  });
}

submitComment("quality");
submitComment("delivery");
submitComment("service");
