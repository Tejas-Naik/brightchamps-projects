/* Pomodoro app logic (fixed timing)
   - More precise tick: use floating-point delta (seconds) between ticks
   - lastTick used to compute accurate elapsed time
   - display uses Math.ceil so UI shows expected MM:SS behaviour (24:59 after ~1s)
   - preserves settings, stats, notifications, sound etc.
*/

"use strict";

const DEFAULTS = {
  focus: 25,
  shortBreak: 5,
  longBreak: 15,
  roundsBeforeLong: 4,
  autoStart: false,
  sound: true,
  notify: false,
};

const SELECTORS = {
  timeDisplay: "#timeDisplay",
  modeLabel: "#modeLabel",
  startPause: "#startPause",
  skip: "#skip",
  reset: "#reset",
  ringProgress: ".ring-progress",
  completedCount: "#completedCount",
  streak: "#streak",
  currentMode: "#currentMode",
  settingsBtn: "#settingsBtn",
  settingsModal: "#settingsModal",
  closeSettings: "#closeSettings",
  saveSettings: "#saveSettings",
  restoreDefaults: "#restoreDefaults",
  focusMinutes: "#focusMinutes",
  shortBreakMinutes: "#shortBreakMinutes",
  longBreakMinutes: "#longBreakMinutes",
  roundsBeforeLong: "#roundsBeforeLong",
  autoStart: "#autoStart",
  soundToggle: "#soundToggle",
  notifyToggle: "#notifyToggle",
  presetBtns: ".preset",
  statsBtn: "#statsBtn",
  statsModal: "#statsModal",
  closeStats: "#closeStats",
  todayCompleted: "#todayCompleted",
  totalCompleted: "#totalCompleted",
  longestStreak: "#longestStreak",
  clearStats: "#clearStats",
};

const el = (sel) => document.querySelector(sel);
const els = (sel) => Array.from(document.querySelectorAll(sel));

let settings = loadSettings();
let state = {
  mode: "focus", // 'focus' | 'shortBreak' | 'longBreak'
  remaining: settings.focus * 60,
  running: false,
  intervalId: null,
  completedPomodoros: 0,
  streak: 0,
  roundsCompleted: 0,
  lastTick: null,
};

// Element refs
const timeDisplay = el(SELECTORS.timeDisplay);
const modeLabel = el(SELECTORS.modeLabel);
const startPauseBtn = el(SELECTORS.startPause);
const skipBtn = el(SELECTORS.skip);
const resetBtn = el(SELECTORS.reset);
const ringProgress = document.querySelector(SELECTORS.ringProgress);
const completedCountEl = el(SELECTORS.completedCount);
const streakEl = el(SELECTORS.streak);
const currentModeEl = el(SELECTORS.currentMode);
const ding = document.getElementById("ding");

/* bootstrap */
init();

function init() {
  // Setup ring circumference if present
  try {
    const r = 52;
    const circumference = 2 * Math.PI * r;
    if (ringProgress) ringProgress.style.strokeDasharray = circumference;
  } catch (e) {
    console.warn("ring init failed", e);
  }

  loadStats(); // initialize stats storage/day rollover
  applyUIFromSettings();
  updateModeLabel();
  updateTimeDisplay();
  updateRing();
  updateStatsUI();

  // Buttons / UI handlers
  startPauseBtn.addEventListener("click", toggleStartPause);
  skipBtn.addEventListener("click", skipSession);
  resetBtn.addEventListener("click", resetSession);

  els(SELECTORS.presetBtns).forEach((b) => {
    b.addEventListener("click", (e) => {
      const f = Number(e.currentTarget.dataset.focus);
      const br = Number(e.currentTarget.dataset.break);
      settings.focus = f;
      settings.shortBreak = br;
      saveSettings();
      applyUIFromSettings();
      resetSession();
    });
  });

  // Keyboard shortcuts
  window.addEventListener("keydown", (e) => {
    if (
      document.activeElement &&
      ["INPUT", "TEXTAREA"].includes(document.activeElement.tagName)
    )
      return;
    if (e.code === "Space") {
      e.preventDefault();
      toggleStartPause();
    }
    if (e.key.toLowerCase() === "k") skipSession();
    if (e.key.toLowerCase() === "r") resetSession();
    if (e.key.toLowerCase() === "s") openSettings();
    if (e.key.toLowerCase() === "t") openStats();
  });

  // Settings modal
  el(SELECTORS.settingsBtn).addEventListener("click", openSettings);
  el(SELECTORS.closeSettings).addEventListener("click", closeSettings);
  el(SELECTORS.saveSettings).addEventListener("click", saveSettingsFromUI);
  el(SELECTORS.restoreDefaults).addEventListener("click", restoreDefaults);

  // Stats modal
  el(SELECTORS.statsBtn).addEventListener("click", openStats);
  el(SELECTORS.closeStats).addEventListener("click", closeStats);
  el(SELECTORS.clearStats).addEventListener("click", clearStats);

  // Sound and notification
  ding.volume = 0.9;

  // persist runtime occasionally
  setInterval(() => {
    const toSave = {
      completedPomodoros: state.completedPomodoros,
      streak: state.streak,
      roundsCompleted: state.roundsCompleted,
      mode: state.mode,
      remaining: state.remaining,
    };
    localStorage.setItem("pomodoro.runtime", JSON.stringify(toSave));
  }, 2000);

  // Restore runtime counts (not running timer)
  tryRestoreState();
}

/* Settings storage */
function loadSettings() {
  try {
    const raw = localStorage.getItem("pomodoro.settings");
    if (raw) return Object.assign({}, DEFAULTS, JSON.parse(raw));
  } catch (e) {}
  return Object.assign({}, DEFAULTS);
}
function saveSettings() {
  localStorage.setItem("pomodoro.settings", JSON.stringify(settings));
}
function applyUIFromSettings() {
  el(SELECTORS.focusMinutes).value = settings.focus;
  el(SELECTORS.shortBreakMinutes).value = settings.shortBreak;
  el(SELECTORS.longBreakMinutes).value = settings.longBreak;
  el(SELECTORS.roundsBeforeLong).value = settings.roundsBeforeLong;
  el(SELECTORS.autoStart).checked = settings.autoStart;
  el(SELECTORS.soundToggle).checked = settings.sound;
  el(SELECTORS.notifyToggle).checked = settings.notify;

  if (!state.running) {
    if (state.mode === "focus") state.remaining = settings.focus * 60;
    if (state.mode === "shortBreak") state.remaining = settings.shortBreak * 60;
    if (state.mode === "longBreak") state.remaining = settings.longBreak * 60;
  }
  updateModeLabel();
  updateTimeDisplay();
  updateRing();
}

/* Settings modal controls */
function openSettings() {
  el(SELECTORS.settingsModal).setAttribute("aria-hidden", "false");
  el(SELECTORS.settingsModal).style.display = "flex";
  el(SELECTORS.focusMinutes).focus();
}
function closeSettings() {
  el(SELECTORS.settingsModal).setAttribute("aria-hidden", "true");
  el(SELECTORS.settingsModal).style.display = "none";
}
function saveSettingsFromUI() {
  const f = parseInt(el(SELECTORS.focusMinutes).value) || DEFAULTS.focus;
  const s =
    parseInt(el(SELECTORS.shortBreakMinutes).value) || DEFAULTS.shortBreak;
  const l =
    parseInt(el(SELECTORS.longBreakMinutes).value) || DEFAULTS.longBreak;
  const rounds =
    parseInt(el(SELECTORS.roundsBeforeLong).value) || DEFAULTS.roundsBeforeLong;
  settings.focus = Math.max(1, f);
  settings.shortBreak = Math.max(1, s);
  settings.longBreak = Math.max(1, l);
  settings.roundsBeforeLong = Math.max(1, rounds);
  settings.autoStart = el(SELECTORS.autoStart).checked;
  settings.sound = el(SELECTORS.soundToggle).checked;
  settings.notify = el(SELECTORS.notifyToggle).checked;
  saveSettings();
  applyUIFromSettings();
  closeSettings();
}
function restoreDefaults() {
  settings = Object.assign({}, DEFAULTS);
  saveSettings();
  applyUIFromSettings();
}

/* Timer control (fixed timing) */
function toggleStartPause() {
  if (state.running) return pauseTimer();
  startTimer();
}
function startTimer() {
  if (state.running) return;
  state.running = true;
  state.lastTick = Date.now();
  startPauseBtn.textContent = "⏸ Pause";
  startPauseBtn.classList.add("active");
  state.intervalId = setInterval(tick, 250); // 250ms offers reasonable responsiveness
}
function pauseTimer() {
  if (!state.running) return;
  state.running = false;
  startPauseBtn.textContent = "▶️ Start";
  startPauseBtn.classList.remove("active");
  clearInterval(state.intervalId);
  state.intervalId = null;
  state.lastTick = null;
}

function resetSession() {
  pauseTimer();
  if (state.mode === "focus") state.remaining = settings.focus * 60;
  else if (state.mode === "shortBreak")
    state.remaining = settings.shortBreak * 60;
  else state.remaining = settings.longBreak * 60;
  updateTimeDisplay();
  updateRing();
}

function skipSession() {
  // Force complete this session and move to next
  completeSession(true);
}

/* The precise tick: subtract fractional seconds */
function tick() {
  if (!state.lastTick) state.lastTick = Date.now();
  const now = Date.now();
  const deltaSeconds = (now - state.lastTick) / 1000; // fractional seconds
  state.lastTick = now;

  // subtract fractional seconds for precise countdown
  state.remaining = Math.max(0, state.remaining - deltaSeconds);
  updateTimeDisplay();
  updateRing();

  if (state.remaining <= 0) {
    completeSession();
  }
}

function completeSession(skip = false) {
  // stop running first
  pauseTimer();

  // play sound & optionally notify
  if (settings.sound) playSound();
  if (settings.notify) showNotification(`${modeName(state.mode)} ended`);

  // update stats
  if (state.mode === "focus") {
    state.completedPomodoros++;
    state.roundsCompleted++;
    state.streak++;
    saveCompletionStats();
  } else {
    state.streak = 0;
  }

  // decide next mode
  if (state.mode === "focus") {
    if (
      state.roundsCompleted > 0 &&
      state.roundsCompleted % settings.roundsBeforeLong === 0
    ) {
      switchMode("longBreak");
    } else {
      switchMode("shortBreak");
    }
  } else {
    switchMode("focus");
  }

  updateStatsUI();

  if (settings.autoStart && !skip) {
    // slight delay to show transition
    setTimeout(() => startTimer(), 500);
  }
}

/* Mode switching and UI */
function switchMode(newMode) {
  state.mode = newMode;
  if (newMode === "focus") state.remaining = settings.focus * 60;
  if (newMode === "shortBreak") state.remaining = settings.shortBreak * 60;
  if (newMode === "longBreak") state.remaining = settings.longBreak * 60;
  updateModeLabel();
  updateTimeDisplay();
  updateRing();
}

function updateTimeDisplay() {
  // Use ceil so 24:59 displays when remaining is 1499.x
  const secs = Math.max(0, Math.ceil(state.remaining));
  timeDisplay.textContent = formatSecs(secs);
}
function updateModeLabel() {
  modeLabel.textContent = modeName(state.mode);
  currentModeEl.textContent = modeName(state.mode);
}
function updateRing() {
  const total =
    state.mode === "focus"
      ? settings.focus * 60
      : state.mode === "shortBreak"
      ? settings.shortBreak * 60
      : settings.longBreak * 60;
  const fraction = total === 0 ? 0 : state.remaining / total;
  const strokeLength =
    Number(ringProgress && ringProgress.style.strokeDasharray) ||
    2 * Math.PI * 52;
  const offset = strokeLength * (1 - fraction);
  if (ringProgress) ringProgress.style.strokeDashoffset = offset;
  // subtle UI tweaks
  if (state.mode === "focus") {
    modeLabel.style.color = "";
    timeDisplay.style.color = "";
  } else {
    modeLabel.style.color = "#9fb0d6";
  }
}

/* Stats persistence */
function loadStats(readOnly) {
  let stats = { today: 0, total: 0, longestStreak: 0, lastDate: null };
  try {
    const raw = localStorage.getItem("pomodoro.stats");
    if (raw) stats = JSON.parse(raw);
  } catch (e) {}
  // day rollover handling
  const todayKey = new Date().toISOString().slice(0, 10);
  if (!stats.lastDate || stats.lastDate !== todayKey) {
    stats.today = 0;
    stats.lastDate = todayKey;
    localStorage.setItem("pomodoro.stats", JSON.stringify(stats));
  }
  if (readOnly) return stats;
  return stats;
}
function saveCompletionStats() {
  const stats = loadStats();
  const todayKey = new Date().toISOString().slice(0, 10);
  if (!stats.lastDate || stats.lastDate !== todayKey) {
    stats.lastDate = todayKey;
    stats.today = 0;
  }
  stats.today = (stats.today || 0) + 1;
  stats.total = (stats.total || 0) + 1;
  stats.longestStreak = Math.max(stats.longestStreak || 0, state.streak);
  localStorage.setItem("pomodoro.stats", JSON.stringify(stats));
}
function clearStats() {
  localStorage.removeItem("pomodoro.stats");
  loadStats();
  updateStatsUI();
}
function updateStatsUI() {
  completedCountEl.textContent = state.completedPomodoros;
  streakEl.textContent = state.streak;
  const stats = loadStats(true);
  el("#todayCompleted").textContent = stats.today || 0;
  el("#totalCompleted").textContent = stats.total || 0;
  el("#longestStreak").textContent = stats.longestStreak || 0;
}

/* Stats modal */
function openStats() {
  el(SELECTORS.statsModal).setAttribute("aria-hidden", "false");
  el(SELECTORS.statsModal).style.display = "flex";
}
function closeStats() {
  el(SELECTORS.statsModal).setAttribute("aria-hidden", "true");
  el(SELECTORS.statsModal).style.display = "none";
}

/* Sound & notification */
function playSound() {
  try {
    ding.currentTime = 0;
    ding.play();
  } catch (e) {}
}
function showNotification(text) {
  if (!("Notification" in window)) return;
  if (Notification.permission === "granted") {
    new Notification("Pomodoro", { body: text, silent: !settings.sound });
  } else if (Notification.permission !== "denied") {
    Notification.requestPermission().then((p) => {
      if (p === "granted")
        new Notification("Pomodoro", { body: text, silent: !settings.sound });
    });
  }
}

/* Helpers */
function formatSecs(s) {
  s = Math.max(0, Math.round(s));
  const mm = Math.floor(s / 60);
  const ss = s % 60;
  return `${String(mm).padStart(2, "0")}:${String(ss).padStart(2, "0")}`;
}
function modeName(m) {
  if (m === "focus") return "Focus";
  if (m === "shortBreak") return "Short break";
  return "Long break";
}

/* Try restore counts */
function tryRestoreState() {
  try {
    const raw = localStorage.getItem("pomodoro.runtime");
    if (!raw) return;
    const runtime = JSON.parse(raw);
    state.completedPomodoros = runtime.completedPomodoros || 0;
    state.streak = runtime.streak || 0;
    state.roundsCompleted = runtime.roundsCompleted || 0;
    state.mode = runtime.mode || "focus";
    if (runtime.remaining && typeof runtime.remaining === "number")
      state.remaining = runtime.remaining;
  } catch (e) {}
}

/* notification permission small UX */
document.addEventListener("change", (e) => {
  if (e.target && e.target.id === "notifyToggle" && e.target.checked) {
    if ("Notification" in window && Notification.permission !== "granted") {
      Notification.requestPermission();
    }
  }
});

/* Contact Form Handling */
const contactForm = document.querySelector('.contact-form');
if (contactForm) {
  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const btn = contactForm.querySelector('button');
    const originalText = btn.textContent;
    
    btn.textContent = 'Sending...';
    btn.disabled = true;
    
    // Simulate network request
    setTimeout(() => {
      btn.textContent = 'Message Sent!';
      contactForm.reset();
      
      setTimeout(() => {
        btn.textContent = originalText;
        btn.disabled = false;
      }, 3000);
    }, 1500);
  });
}
