import { ref, watchEffect } from "vue"

const darkMode = ref(localStorage.getItem("darkMode") === "true")

export function useDarkMode() {
    watchEffect(() => {
        if (darkMode.value) {
            document.documentElement.classList.add("dark")
            localStorage.setItem("darkMode", "true")
        } else {
            document.documentElement.classList.remove("dark")
            localStorage.setItem("darkMode", "false")
        }
    })

    return {
        darkMode,
        toggleDarkMode: () => (darkMode.value = !darkMode.value),
    }
}
