async function sendEmail() {
    try {
        const email = document.getElementById("email").value;

        if (!email.trim()) {
            alert("Please enter an email!");
            return;
        }

        const btn = document.getElementById("btn");
        btn.innerText = "Generating...";
        btn.disabled = true;

        const res = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ email: email })
        });

        const data = await res.json();
        console.log(data); // 🔥 DEBUG

        // ✅ FIX: ensure proper IDs
        document.getElementById("intent").innerText = "Intent: " + data.intent;
        document.getElementById("tone").innerText = "Tone: " + data.tone;
        document.getElementById("response").innerText = "Response: " + data.response;

        btn.innerText = "Generate Reply";
        btn.disabled = false;

    } catch (error) {
        console.error("Error:", error);
        alert("Something went wrong. Check console.");
    }
}