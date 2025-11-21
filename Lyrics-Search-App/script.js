// Function to generate the Musixmatch API URL
function updateURL(songName = "", artistName = "") {
  return `https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?format=jsonp&callback=searchLyrics&q_track=${songName}&q_artist=${artistName}&apikey=f90cd35582c176dbcfd3ecebcc227390`;
}

// Get DOM elements
const searchForm = document.querySelector('.search-form');
const songInput = document.querySelector('.song');
const artistInput = document.querySelector('.artist');
const lyricsSection = document.getElementById('lyrics-section');
const closeBtn = document.getElementById('close-btn');
const songInfo = document.getElementById('song-info');
const lyricsText = document.getElementById('lyrics-text');

// Event listener for form submission
searchForm.addEventListener('submit', function(e) {
  e.preventDefault();
  const songName = songInput.value.trim().replace(/ /g, "%20");
  const artistName = artistInput.value.trim().replace(/ /g, "%20");
  
  if (!songName || !artistName) {
    alert('Please enter both song and artist name');
    return;
  }
  
  const newURL = updateURL(songName, artistName);
  
  // Show loading state
  songInfo.textContent = 'Searching...';
  lyricsText.textContent = 'Loading lyrics...';
  lyricsSection.style.display = 'block';
  
  updateScript(newURL);
});

function updateScript(url) {
  let newScript = document.createElement("script");
  newScript.src = url;
  newScript.setAttribute("id", "head-script");

  let oldScript = document.getElementById("head-script");
  let head = document.getElementsByTagName("head")[0];

  if (oldScript === null) {
    head.appendChild(newScript);
  } else {
    head.replaceChild(newScript, oldScript);
  }
}

function searchLyrics(object) {
  if (object.message.header.status_code === 404) {
    songInfo.textContent = 'Song not found';
    lyricsText.textContent = 'Sorry, we could not find lyrics for this song. Please check the song and artist name and try again.';
  } else {
    const songName = songInput.value.trim();
    const artistName = artistInput.value.trim();
    songInfo.textContent = `${songName} by ${artistName}`;
    lyricsText.textContent = object.message.body.lyrics.lyrics_body;
    
    // Clear form inputs
    songInput.value = '';
    artistInput.value = '';
  }
}

// Close button functionality
closeBtn.addEventListener('click', function() {
  lyricsSection.style.display = 'none';
});

// Event listener for page load
window.addEventListener("load", function() {
  loadMostSearchedLyrics();
  loadNewlyAddedLyrics();
});

function loadMostSearchedLyrics() {
  const mostSearchedURL = "https://api.musixmatch.com/ws/1.1/chart.tracks.get?format=jsonp&callback=displayMostSearched&chart_name=top&page=1&page_size=5&apikey=f90cd35582c176dbcfd3ecebcc227390";
  const mostSearchedScript = document.createElement("script");
  mostSearchedScript.src = mostSearchedURL;
  document.head.appendChild(mostSearchedScript);
}

function displayMostSearched(data) {
  const mostSearchedList = document.querySelector(".most-searched-list");
  const tracks = data.message.body.track_list;

  if (!tracks || tracks.length === 0) {
    mostSearchedList.innerHTML = "<li>No most searched lyrics found.</li>";
    return;
  }

  tracks.forEach((track) => {
    const trackName = track.track.track_name;
    const artistName = track.track.artist_name;
    const listItem = document.createElement("li");
    listItem.textContent = `${trackName} by ${artistName}`;
    mostSearchedList.appendChild(listItem);
  });
}

function loadNewlyAddedLyrics() {
  const newlyAddedURL = "https://api.musixmatch.com/ws/1.1/chart.tracks.get?format=jsonp&callback=displayNewlyAdded&chart_name=new&page=1&page_size=5&apikey=f90cd35582c176dbcfd3ecebcc227390";
  const newlyAddedScript = document.createElement("script");
  newlyAddedScript.src = newlyAddedURL;
  document.head.appendChild(newlyAddedScript);
}

function displayNewlyAdded(data) {
  const newlyAddedList = document.querySelector(".newly-added-list");
  const tracks = data.message.body.track_list;

  if (!tracks || tracks.length === 0) {
    newlyAddedList.innerHTML = "<li>No newly added lyrics found.</li>";
    return;
  }

  tracks.forEach((track) => {
    const trackName = track.track.track_name;
    const artistName = track.track.artist_name;
    const listItem = document.createElement("li");
    listItem.textContent = `${trackName} by ${artistName}`;
    newlyAddedList.appendChild(listItem);
  });
}


