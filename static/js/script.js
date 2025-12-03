/* ------------------------------------------- */
/*            DARK MODE HANDLING               */
/* ------------------------------------------- */

// Run when page loads
document.addEventListener("DOMContentLoaded", () => {
    const isDark = localStorage.getItem("darkModeEnabled");

    if (isDark === "true") {
        document.body.classList.add("dark-mode");
    }

    const darkSwitch = document.querySelector("#darkSwitch");
    if (darkSwitch) {
        darkSwitch.addEventListener("change", () => {
            if (darkSwitch.checked) {
                document.body.classList.add("dark-mode");
                localStorage.setItem("darkModeEnabled", "true");
            } else {
                document.body.classList.remove("dark-mode");
                localStorage.setItem("darkModeEnabled", "false");
            }
        });
    }

    // Auto-scroll chat on page load
    scrollChatToBottom();
});


/* ------------------------------------------- */
/*        AUTO-SCROLL IN CHAT PAGE             */
/* ------------------------------------------- */

function scrollChatToBottom() {
    const chatBox = document.querySelector(".chat-box");
    if (chatBox) {
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}


/* ------------------------------------------- */
/*         SIMPLE "SAVED!" POPUP               */
/* ------------------------------------------- */

function showSavedPopup() {
    const popup = document.createElement("div");
    popup.innerText = "Settings saved!";
    popup.style.position = "fixed";
    popup.style.bottom = "20px";
    popup.style.right = "20px";
    popup.style.padding = "12px 18px";
    popup.style.background = "#0d6efd";
    popup.style.color = "white";
    popup.style.borderRadius = "8px";
    popup.style.boxShadow = "0 3px 10px rgba(0,0,0,0.2)";
    popup.style.opacity = "0";
    popup.style.transition = "0.4s";

    document.body.appendChild(popup);

    setTimeout(() => (popup.style.opacity = "1"), 100);
    setTimeout(() => {
        popup.style.opacity = "0";
        setTimeout(() => popup.remove(), 500);
    }, 2000);
}


/* ------------------------------------------- */
/*     MOOD BUTTON WAVE EFFECT (FUN)           */
/* ------------------------------------------- */

const moodButtons = document.querySelectorAll(".mood-btn");
moodButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
        btn.style.transform = "scale(0.9)";
        setTimeout(() => {
            btn.style.transform = "scale(1)";
        }, 150);
    });
});
