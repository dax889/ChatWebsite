document.addEventListener('DOMContentLoaded', function () {
        const textInput = document.querySelector('#chat-text-input');
        const fileInput = document.querySelector('#id_image');
        const sendBtn = document.querySelector('#send-button');

        function toggleSendButton() {
          if (
            (textInput && textInput.value.trim() !== '') ||
            (fileInput && fileInput.files.length > 0)
          ) {
            sendBtn.disabled = false;
          } else {
            sendBtn.disabled = true;
          }
        }

        if (textInput) {
          textInput.addEventListener('input', toggleSendButton);
        }
        if (fileInput) {
          fileInput.addEventListener('change', toggleSendButton);
        }

        toggleSendButton(); // run once on load
  });
    // set for time

        function formatChatTimestamp(dateStr) {
          const timestamp = new Date(dateStr);
          const now = new Date();

          // Normalize times
          const isToday = timestamp.toDateString() === now.toDateString();

          const yesterday = new Date();
          yesterday.setDate(now.getDate() - 1);
          const isYesterday = timestamp.toDateString() === yesterday.toDateString();

          const options = { hour: 'numeric', minute: 'numeric', hour12: true };

          if (isToday) {
            return 'Today at ' + timestamp.toLocaleTimeString('en-IN', options);
          } else if (isYesterday) {
            return 'Yesterday at ' + timestamp.toLocaleTimeString('en-IN', options);
          } else {
            const dateOptions = { day: '2-digit', month: 'short', year: 'numeric' };
            return timestamp.toLocaleDateString('en-IN', dateOptions) + ' at ' +
                  timestamp.toLocaleTimeString('en-IN', options);
          }
        }

        // Replace all timestamps
        document.querySelectorAll('.timestamp').forEach(el => {
          const raw = el.dataset.timestamp;
          if (raw) {
            el.innerText = formatChatTimestamp(raw);
          }
        });

        // scroll to bottom
        function scrollToBottom() {
          const chatBox = document.getElementById("chat-box");
          chatBox.scrollTop = chatBox.scrollHeight;
        }

        // Scroll on initial load
        window.addEventListener("load", scrollToBottom);

        // Scroll after form submit (after redirect)
        const form = document.querySelector("form.chat-form");
        if (form) {
          form.addEventListener("submit", () => {
            // Delay a bit to let the message render on the next page load
            setTimeout(scrollToBottom, 100);
          });
        }


        // menu icon (three dots)
          function toggleMenu() {
            const menu = document.getElementById("dropdown-menu");
            menu.style.display = (menu.style.display === "block") ? "none" : "block";
          }

          // Optional: Hide menu if clicked outside
          window.addEventListener("click", function(e) {
            const menu = document.getElementById("dropdown-menu");
            const icon = document.querySelector(".menu-icon");
            if (!icon.contains(e.target)) {
              menu.style.display = "none";
            }
          });

        // emoji icon
           document.addEventListener('DOMContentLoaded', () => {
            const emojiToggle = document.querySelector('.emoji-toggle');
            const emojiDropdown = document.getElementById('emoji-dropdown');
            const input = document.querySelector('.chat-text-input');

            emojiToggle.addEventListener('click', () => {
              emojiDropdown.classList.toggle('show');
            });

            emojiDropdown.addEventListener('click', (e) => {
              if (e.target && e.target.textContent) {
                input.value += e.target.textContent;
                input.focus();
              }
            });

            // Hide emoji dropdown on outside click
            document.addEventListener('click', function(e) {
              if (!emojiDropdown.contains(e.target) && !emojiToggle.contains(e.target)) {
                emojiDropdown.classList.remove('show');
              }
            });
          });