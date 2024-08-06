'use strict';
{
    window.addEventListener('load', function (e) {

        function setTheme(mode) {
            if (mode !== "light" && mode !== "dark" && mode !== "auto") {
                console.error(`Got invalid theme mode: ${mode}. Resetting to auto.`);
                mode = "auto";
            }
            document.documentElement.dataset.theme = mode;
            localStorage.setItem("theme", mode);
        }

        function cycleTheme() {
            const currentTheme = localStorage.getItem("theme") || "auto";
            const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

            let newTheme;
            if (prefersDark) {
                // Auto (dark) -> Light -> Dark
                if (currentTheme === "auto") {
                    newTheme = "light";
                } else if (currentTheme === "light") {
                    newTheme = "dark";
                } else {
                    newTheme = "auto";
                }
            } else {
                // Auto (light) -> Dark -> Light
                if (currentTheme === "auto") {
                    newTheme = "dark";
                } else if (currentTheme === "dark") {
                    newTheme = "light";
                } else {
                    newTheme = "auto";
                }
            }
            setTheme(newTheme);
            // after cycle theme change comments style
            changeGiscusTheme(newTheme);
        }

        function initTheme() {
            // set theme defined in localStorage if there is one, or fallback to auto mode
            const currentTheme = localStorage.getItem("theme");
            currentTheme ? setTheme(currentTheme) : setTheme("auto");
        }

        function setupTheme() {
            // Attach event handlers for toggling themes
            const buttons = document.getElementsByClassName("theme-toggle");
            Array.from(buttons).forEach((btn) => {
                btn.addEventListener("click", cycleTheme);
            });
            initTheme();
        }

        setupTheme();
        changeGiscusTheme('auto');
    });

    function changeGiscusTheme (newTheme) {
        //const theme = document.documentElement.getAttribute('data-theme') === 'dark' ?  'dark' : 'light'
        let theme = newTheme;

        if (theme == 'auto'){
            theme = 'preferred_color_scheme';
        }

        function sendMessage(message) {
          const iframe = document.querySelector('iframe.giscus-frame');
          if (!iframe) return;
          iframe.contentWindow.postMessage({ giscus: message }, 'https://giscus.app');
        }
    
        sendMessage({
          setConfig: {
            theme: theme
          }
        });
      }
}