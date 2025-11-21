// Discord-like client-side behavior: channels, messages per channel, and input handling
(function () {
  const channelList = document.getElementById("channel-list");
  const chatScroll = document.getElementById("chat-scroll");
  const chatForm = document.getElementById("chat-form");
  const chatInput = document.getElementById("chat-input");
  const headerTitle = document.querySelector(".chat-header-title");

  const STORAGE_KEY = "discord_like_messages_by_channel";

  function getState() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {};
    } catch (e) {
      return {};
    }
  }

  function setState(state) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  }

  function getActiveChannelId() {
    const active = channelList.querySelector(".channel.active");
    return active ? active.getAttribute("data-channel") : "#general";
  }

  function formatTime(date) {
    return date.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  }

  function renderMessages(channelId) {
    const state = getState();
    const messages = state[channelId] || [];
    chatScroll.innerHTML = messages
      .map((m) => {
        return `
        <div class="message-row">
          <div class="avatar"><img src="user-png.png" alt="avatar"></div>
          <div class="message-content">
            <div class="message-header">
              <span class="message-username">${m.author}</span>
              <span class="message-time">${m.time}</span>
            </div>
            <div class="message-text">${escapeHtml(m.text)}</div>
          </div>
        </div>`;
      })
      .join("");
    chatScroll.scrollTop = chatScroll.scrollHeight;
  }

  function escapeHtml(text) {
    const div = document.createElement("div");
    div.innerText = text;
    return div.innerHTML;
  }

  function setActiveChannel(li) {
    channelList
      .querySelectorAll(".channel")
      .forEach((el) => el.classList.remove("active"));
    li.classList.add("active");
    const id = li.getAttribute("data-channel");
    const name = li.textContent.trim();
    headerTitle.textContent = name;
    chatInput.placeholder = `Message ${id}`;
    renderMessages(id);
  }

  // Initial activation
  document.addEventListener("DOMContentLoaded", () => {
    const initial =
      channelList.querySelector(".channel.active") ||
      channelList.querySelector(".channel");
    if (initial) setActiveChannel(initial);
  });

  // Channel switching
  channelList.addEventListener("click", (e) => {
    const li = e.target.closest(".channel");
    if (!li) return;
    setActiveChannel(li);
  });

  // Sending a message
  chatForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const text = chatInput.value.trim();
    if (!text) return;

    const channelId = getActiveChannelId();
    const state = getState();
    const entry = {
      author: "You",
      text,
      time: formatTime(new Date()),
    };
    state[channelId] = state[channelId] || [];
    state[channelId].push(entry);
    setState(state);

    chatInput.value = "";
    renderMessages(channelId);
  });
})();
