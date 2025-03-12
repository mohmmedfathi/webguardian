document.getElementById('linkForm').addEventListener('submit', function(e) {
    const urlInput = document.getElementById('urlInput');
    if (urlInput.value.trim() === "") {
        e.preventDefault();
        urlInput.classList.add('is-invalid');
    } else {
        urlInput.classList.remove('is-invalid');
    }
});