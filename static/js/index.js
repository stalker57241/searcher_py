const query = document.getElementById("query")

function search() {
    window.location.assign("/search?query=" + encodeURIComponent(query.value));
}