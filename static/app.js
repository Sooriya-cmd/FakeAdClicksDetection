const form = document.querySelector("#score-form");
const userSelect = document.querySelector("#user-id");
const eventSelect = document.querySelector("#event");
const categorySelect = document.querySelector("#category");
const scoreButton = document.querySelector("#score-button");
const formError = document.querySelector("#form-error");
const activityList = document.querySelector("#activity-list");
const analyses = [];

const readable = (value) => value
  .split("_")
  .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
  .join(" ");

async function loadDashboard() {
  const [optionsResponse, summaryResponse] = await Promise.all([
    fetch("/api/options"),
    fetch("/api/summary"),
  ]);
  if (!optionsResponse.ok || !summaryResponse.ok) {
    throw new Error("The demo could not load its model data.");
  }
  const [options, summary] = await Promise.all([
    optionsResponse.json(),
    summaryResponse.json(),
  ]);

  userSelect.replaceChildren();
  for (const userId of options.users) {
    userSelect.add(new Option(`Profile ${String(options.users.indexOf(userId) + 1).padStart(2, "0")} · ${userId}`, userId));
  }
  userSelect.value = options.default_user;
  eventSelect.replaceChildren();
  for (const event of options.events) eventSelect.add(new Option(readable(event), event));
  categorySelect.replaceChildren();
  for (const category of options.categories) categorySelect.add(new Option(category.replaceAll("_", " "), category));

  document.querySelector("#training-count").textContent = Number(summary.training_records).toLocaleString();
  document.querySelector("#profile-count").textContent = Number(summary.user_profiles).toLocaleString();
  document.querySelector("#test-count").textContent = Number(summary.test_records).toLocaleString();
  document.querySelector("#feature-count").textContent = summary.feature_count;
  await analyzeClick();
}

async function analyzeClick(event) {
  if (event) event.preventDefault();
  formError.textContent = "";
  scoreButton.disabled = true;
  scoreButton.querySelector(".button-text").textContent = "Reading click signals…";
  document.querySelector("#score-ring").classList.add("is-loading");

  try {
    const response = await fetch("/api/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        user_id: userSelect.value,
        event: eventSelect.value,
        category: categorySelect.value,
      }),
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.error || "The model could not score this click.");
    showResult(result);
    rememberAnalysis(result);
  } catch (error) {
    formError.textContent = error.message;
  } finally {
    scoreButton.disabled = false;
    scoreButton.querySelector(".button-text").textContent = "Analyze this click";
    document.querySelector("#score-ring").classList.remove("is-loading");
  }
}

function showResult(result) {
  const scorePercent = Math.round(result.score * 100);
  const isFake = result.is_fake;
  const ring = document.querySelector("#score-ring");
  const verdict = document.querySelector("#verdict");

  document.querySelector("#score-value").textContent = `${scorePercent}%`;
  ring.style.setProperty("--score", `${scorePercent}%`);
  ring.classList.toggle("is-fake", isFake);
  verdict.textContent = result.prediction;
  verdict.classList.toggle("fake", isFake);
  verdict.classList.toggle("legit", !isFake);
  document.querySelector("#verdict-copy").textContent = isFake
    ? "This click scored at or above the model’s 50% fake-click threshold."
    : "This click scored below the model’s 50% fake-click threshold.";

  const fill = document.querySelector("#decision-fill");
  fill.style.width = `${scorePercent}%`;
  fill.classList.toggle("is-fake", isFake);
  document.querySelector("#receipt-text").textContent =
    `${readable(result.event)} · ${result.category.replaceAll("_", " ")} · profile ${result.user_id}`;
  document.querySelector("#receipt-status").textContent = isFake ? "FLAGGED" : "CLEARED";
  document.querySelector("#receipt-status").style.color = isFake ? "var(--red)" : "var(--lime)";
}

function rememberAnalysis(result) {
  analyses.unshift({ ...result, time: new Date() });
  analyses.splice(6);
  document.querySelector("#session-count").textContent =
    `${analyses.length} CHECK${analyses.length === 1 ? "" : "S"} THIS SESSION`;
  activityList.replaceChildren();

  analyses.forEach((analysis, index) => {
    const row = document.createElement("div");
    row.className = "activity-row";
    const number = document.createElement("span");
    number.className = "activity-index";
    number.textContent = `0${analyses.length - index}`;
    const detail = document.createElement("span");
    detail.className = "activity-detail";
    for (const value of [readable(analysis.event), analysis.category.replaceAll("_", " "), `Profile ${analysis.user_id}`]) {
      const item = document.createElement("span");
      item.textContent = value;
      detail.append(item);
    }
    const time = document.createElement("span");
    time.className = "activity-time";
    time.textContent = analysis.time.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit", second: "2-digit" });
    const badge = document.createElement("span");
    badge.className = `activity-badge${analysis.is_fake ? " fake" : ""}`;
    badge.textContent = `${analysis.is_fake ? "FAKE" : "LEGIT"} · ${Math.round(analysis.score * 100)}%`;
    row.append(number, detail, time, badge);
    activityList.append(row);
  });
}

form.addEventListener("submit", analyzeClick);
loadDashboard().catch((error) => {
  formError.textContent = error.message;
  scoreButton.disabled = true;
});
