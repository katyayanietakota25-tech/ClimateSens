const textInput = document.getElementById("textInput");
const predictBtn = document.getElementById("predictBtn");
const charCount = document.getElementById("charCount");
const statusBox = document.getElementById("status");
const resultBox = document.getElementById("result");
const sentimentPill = document.getElementById("sentimentPill");
const confidence = document.getElementById("confidence");
const meterFill = document.getElementById("meterFill");
const modelNote = document.getElementById("modelNote");

textInput.addEventListener("input", () => {
  charCount.textContent = `${textInput.value.length} / 1500 characters`;
});
document.querySelectorAll(".example").forEach(button => {
  button.addEventListener("click", () => {
    textInput.value = button.dataset.text;
    textInput.dispatchEvent(new Event("input"));
    statusBox.textContent = "";
    resultBox.classList.add("hidden");
  });
});
predictBtn.addEventListener("click", async () => {
  const text = textInput.value.trim();
  statusBox.textContent = "";
  resultBox.classList.add("hidden");
  if (!text) {
    statusBox.textContent = "Please enter a sentence before analyzing.";
    textInput.focus();
    return;
  }
  predictBtn.disabled = true;
  predictBtn.textContent = "Analyzing…";
  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({text})
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "Prediction failed.");
    const label = data.sentiment;
    sentimentPill.textContent = label;
    sentimentPill.className = "pill " + label.toLowerCase();
    const score = data.confidence;
    confidence.textContent = score === null ? "Not available" : `${score}%`;
    meterFill.style.width = score === null ? "0%" : `${score}%`;
    modelNote.textContent = data.note || "";
    resultBox.classList.remove("hidden");
  } catch (error) {
    statusBox.textContent = error.message || "Could not connect to the model. Please try again.";
  } finally {
    predictBtn.disabled = false;
    predictBtn.innerHTML = 'Analyze sentiment <span aria-hidden="true">→</span>';
  }
});
