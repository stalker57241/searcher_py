const query = document.getElementById("query")

function search() {
    if (query.value === "") {
        window.location.assign("/");
        return;
    }
    window.location.assign("/search?query=" + encodeURIComponent(query.value));
}