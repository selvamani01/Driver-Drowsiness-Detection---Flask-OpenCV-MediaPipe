// Driver Drowsiness UI Controller

const statusBox = document.getElementById("statusBox");

// Simulate monitoring + alert (temporary)
// Later we can connect to Flask backend for real-time status
let isAlert = false;

// Function to update UI
function updateStatus() {
    if (isAlert) {
        statusBox.classList.remove("normal");
        statusBox.classList.add("alert");
        statusBox.innerText = "⚠️ Drowsiness Detected!";
    } else {
        statusBox.classList.remove("alert");
        statusBox.classList.add("normal");
        statusBox.innerText = "🟢 Monitoring Driver...";
    }
}

// TEMP: Toggle alert every few seconds (demo only)
setInterval(() => {
    isAlert = !isAlert;
    updateStatus();
}, 5000);

// Initial state
updateStatus();

console.log("Driver Drowsiness UI Loaded");