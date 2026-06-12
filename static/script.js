const searchInput = document.getElementById("searchInput");
const suggestionsBox = document.getElementById("suggestions");

searchInput.addEventListener("input", async () => {
    const query = searchInput.value;

    if (query.length < 2) {
        suggestionsBox.innerHTML = "";
        return;
    }

    const response = await fetch(`/suggest?q=${query}`);
    const suggestions = await response.json();

    suggestionsBox.innerHTML = "";

    suggestions.forEach(item => {
        const div = document.createElement("div");
        div.className = "suggestion-item";
        div.textContent = item;

        div.onclick = () => {
            searchInput.value = item;
            suggestionsBox.innerHTML = "";
        };

        suggestionsBox.appendChild(div);
    });
});