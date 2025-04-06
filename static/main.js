async function fetchNews() {
    const container = document.getElementById("news-container");
    container.innerHTML = "<p>Loading news...</p>";

    try {
        const response = await fetch("/api/news");
        const data = await response.json();

        if (data.news && data.news.length > 0) {
            container.innerHTML = "<h2>📰 Live Crypto News:</h2>";
            data.news.forEach(item => {
                const div = document.createElement("div");
                div.className = "news-item";
                div.innerHTML = `
                    <p><strong>Headline:</strong> ${item.headline}</p>
                    <p><strong>Sentiment:</strong> ${item.sentiment}</p>
                    <p><strong>Confidence:</strong> ${item.confidence}</p>
                    <hr>
                `;
                container.appendChild(div);
            });
        } else {
            container.innerHTML = "<p>No news found.</p>";
        }
    } catch (err) {
        container.innerHTML = "<p>Error fetching news.</p>";
        console.error(err);
    }
}
