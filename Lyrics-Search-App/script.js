const searchForm = document.querySelector(".search-form");
const songInput = document.querySelector(".song");
const artistInput = document.querySelector(".artist");
const lyricsSection = document.getElementById("lyrics-section");
const closeBtn = document.getElementById("close-btn");
const songInfo = document.getElementById("song-info");
const lyricsText = document.getElementById("lyrics-text");

// A helper function to fetch data from an API
async function fetchFromAPI(url) {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching API data:", error);
    return null;
  }
}

// Search for lyrics when the form is submitted
searchForm.addEventListener("submit", async function (e) {
  e.preventDefault();
  const songName = songInput.value.trim();
  const artistName = artistInput.value.trim();

  if (!songName || !artistName) {
    alert("Please enter both song and artist name");
    return;
  }

  const searchUrl = `https://api.lyrics.ovh/v1/${encodeURIComponent(
    artistName
  )}/${encodeURIComponent(songName)}`;

  // Show loading state
  songInfo.textContent = "Searching...";
  lyricsText.textContent = "Loading lyrics...";
  lyricsText.innerHTML = '<span class="loader"></span>'; // Show spinner
  lyricsSection.style.display = "block";

  const result = await fetchFromAPI(searchUrl);
  lyricsText.innerHTML = ""; // Clear spinner
  displayLyrics(result, songName, artistName);
});

// Display the lyrics or an appropriate message
function displayLyrics(data, songName, artistName) {
  if (data && data.lyrics) {
    songInfo.textContent = `${songName} by ${artistName}`;
    // The API returns a lot of newlines at the start, so we trim them.
    lyricsText.textContent = data.lyrics.trim();
    // Clear form inputs
    songInput.value = "";
    artistInput.value = "";
  } else {
    songInfo.textContent = "Lyrics not found";
    lyricsText.textContent = `Sorry, we could not find lyrics for "${songName}" by ${artistName}. Please check the spelling and try again.`;
  }
}

// Close button functionality
closeBtn.addEventListener("click", function () {
  lyricsSection.style.display = "none";
});

// A generic function to load and display chart data
function displayChartNotAvailable(listElementSelector) {
  const listElement = document.querySelector(listElementSelector);
  listElement.innerHTML =
    "<li>Chart feature not available with the current API.</li>";
}

// Load all charts when the page loads
window.addEventListener("load", () => {
  // The new API (lyrics.ovh) does not support charts.
  displayChartNotAvailable(".most-searched-list");
  displayChartNotAvailable(".newly-added-list");
});
