// Menu Items Data
const menu = [
  {
    id: 1,
    title: "buttermilk pancakes",
    category: "breakfast",
    price: 15.99,
    img: "menu-item.jpg",
    desc: "Fluffy, golden pancakes made with fresh buttermilk and served with butter and maple syrup. A classic breakfast favorite that melts in your mouth.",
  },
  {
    id: 2,
    title: "avocado toast",
    category: "breakfast", 
    price: 12.99,
    img: "menu-item.jpg",
    desc: "Fresh smashed avocado on artisan sourdough bread, topped with cherry tomatoes, feta cheese, and a drizzle of olive oil.",
  },
  {
    id: 3,
    title: "grilled chicken salad",
    category: "lunch",
    price: 18.99,
    img: "menu-item.jpg",
    desc: "Tender grilled chicken breast served over mixed greens with cherry tomatoes, cucumbers, and balsamic vinaigrette dressing.",
  },
  {
    id: 4,
    title: "classic beef burger",
    category: "lunch",
    price: 16.99,
    img: "menu-item.jpg",
    desc: "Juicy beef patty with lettuce, tomato, onion, pickles, and special sauce on a toasted brioche bun. Served with crispy fries.",
  },
  {
    id: 5,
    title: "chocolate milkshake",
    category: "shakes",
    price: 8.99,
    img: "menu-item.jpg",
    desc: "Rich and creamy chocolate milkshake made with premium vanilla ice cream and chocolate syrup. Topped with whipped cream.",
  },
  {
    id: 6,
    title: "strawberry delight",
    category: "shakes",
    price: 9.99,
    img: "menu-item.jpg",
    desc: "Fresh strawberry milkshake blended with real strawberries and vanilla ice cream. A refreshing and fruity treat.",
  },
  {
    id: 7,
    title: "eggs benedict",
    category: "breakfast",
    price: 14.99,
    img: "menu-item.jpg",
    desc: "Poached eggs on English muffins with Canadian bacon, topped with hollandaise sauce. Served with roasted potatoes.",
  },
  {
    id: 8,
    title: "caesar salad",
    category: "lunch",
    price: 13.99,
    img: "menu-item.jpg",
    desc: "Crisp romaine lettuce tossed with our homemade Caesar dressing, parmesan cheese, and garlic croutons.",
  },
  {
    id: 9,
    title: "vanilla bean shake",
    category: "shakes",
    price: 7.99,
    img: "menu-item.jpg",
    desc: "Classic vanilla milkshake made with real vanilla beans and premium ice cream. Simple yet delicious.",
  }
];

// Reviews Data
const reviews = [
  {
    id: 1,
    name: "sarah jones",
    job: "ux designer",
    img: "person-1.jpg",
    text: "The food here is absolutely amazing! I've tried multiple dishes and each one exceeded my expectations. The atmosphere is cozy and the staff is incredibly friendly."
  },
  {
    id: 2,
    name: "michael chen",
    job: "software developer",
    img: "person-1.jpg",
    text: "Best pancakes in town! The buttermilk pancakes are fluffy and perfectly sweet. Great place for weekend brunch with family and friends."
  },
  {
    id: 3,
    name: "emma rodriguez",
    job: "marketing manager",
    img: "person-1.jpg",
    text: "I love the variety of healthy options available. The avocado toast and grilled chicken salad are my go-to choices. Fresh ingredients and great presentation!"
  },
  {
    id: 4,
    name: "david wilson",
    job: "food blogger",
    img: "person-1.jpg",
    text: "As a food blogger, I've visited many restaurants, but this place stands out. The attention to detail in every dish is remarkable. Highly recommended!"
  },
  {
    id: 5,
    name: "lisa thompson",
    job: "graphic designer",
    img: "person-1.jpg",
    text: "The milkshakes are incredible! Rich, creamy, and the perfect way to end a meal. The chocolate milkshake is my absolute favorite."
  }
];

// Get DOM elements
const sectionCenter = document.querySelector(".section-center");
const filterBtns = document.querySelectorAll(".filter-btn");

// Reviews elements
const author = document.getElementById("author");
const job = document.getElementById("job");
const img = document.getElementById("person-img");
const info = document.getElementById("info");
const prevBtn = document.querySelector(".prev-btn");
const nextBtn = document.querySelector(".next-btn");
const randomBtn = document.querySelector(".random-btn");

// Set starting item for reviews
let currentItem = 0;

// Load items when page loads
window.addEventListener("DOMContentLoaded", function () {
  displayMenuItems(menu);
  showPerson(currentItem);
});

// Display menu items
function displayMenuItems(menuItems) {
  let displayMenu = menuItems.map(function (item) {
    return `<article class="menu-item" data-id="${item.category}">
          <img src="${item.img}" alt="${item.title}" class="photo"/>
          <div class="item-info">
            <header>
              <h4>${item.title}</h4>
              <h4 class="price">$${item.price}</h4>
            </header>
            <p class="item-text">
              ${item.desc}
            </p>
          </div>
        </article>`;
  });
  displayMenu = displayMenu.join("");
  sectionCenter.innerHTML = displayMenu;
}

// Filter items
filterBtns.forEach(function (btn) {
  btn.addEventListener("click", function (e) {
    // Remove active class from all buttons
    filterBtns.forEach(function (button) {
      button.classList.remove("active");
    });
    // Add active class to clicked button
    e.currentTarget.classList.add("active");
    
    const category = e.currentTarget.dataset.id;
    const menuCategory = menu.filter(function (menuItem) {
      if (menuItem.category === category) {
        return menuItem;
      }
    });
    
    if (category === "all") {
      displayMenuItems(menu);
    } else {
      displayMenuItems(menuCategory);
    }
  });
});

// Set initial active button
document.querySelector('.filter-btn[data-id="all"]').classList.add("active");

// Show person based on item
function showPerson(person) {
  const item = reviews[person];
  img.src = item.img;
  author.textContent = item.name;
  job.textContent = item.job;
  info.textContent = item.text;
}

// Show next person
nextBtn.addEventListener("click", function () {
  currentItem++;
  if (currentItem > reviews.length - 1) {
    currentItem = 0;
  }
  showPerson(currentItem);
});

// Show prev person
prevBtn.addEventListener("click", function () {
  currentItem--;
  if (currentItem < 0) {
    currentItem = reviews.length - 1;
  }
  showPerson(currentItem);
});

// Show random person
randomBtn.addEventListener("click", function () {
  currentItem = Math.floor(Math.random() * reviews.length);
  showPerson(currentItem);
});

// Auto-slide reviews (optional)
setInterval(function() {
  currentItem++;
  if (currentItem > reviews.length - 1) {
    currentItem = 0;
  }
  showPerson(currentItem);
}, 5000); // Change review every 5 seconds

// Add smooth scrolling animation for menu items
function animateMenuItems() {
  const menuItems = document.querySelectorAll('.menu-item');
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, {
    threshold: 0.1
  });

  menuItems.forEach(item => {
    item.style.opacity = '0';
    item.style.transform = 'translateY(30px)';
    item.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(item);
  });
}

// Call animation function after menu items are displayed
setTimeout(animateMenuItems, 100);

// Add loading animation
function showLoadingAnimation() {
  const loadingHTML = `
    <div class="loading">
      <div class="loading-spinner"></div>
      <p>Loading delicious menu items...</p>
    </div>
  `;
  sectionCenter.innerHTML = loadingHTML;
  
  setTimeout(() => {
    displayMenuItems(menu);
    setTimeout(animateMenuItems, 100);
  }, 1000);
}

// Enhanced filter functionality with loading
filterBtns.forEach(function (btn) {
  btn.addEventListener("click", function (e) {
    // Remove active class from all buttons
    filterBtns.forEach(function (button) {
      button.classList.remove("active");
    });
    // Add active class to clicked button
    e.currentTarget.classList.add("active");
    
    const category = e.currentTarget.dataset.id;
    
    // Show loading animation
    showLoadingAnimation();
    
    setTimeout(() => {
      const menuCategory = menu.filter(function (menuItem) {
        if (menuItem.category === category) {
          return menuItem;
        }
      });
      
      if (category === "all") {
        displayMenuItems(menu);
      } else {
        displayMenuItems(menuCategory);
      }
      
      // Re-animate items
      setTimeout(animateMenuItems, 100);
    }, 500);
  });
});
