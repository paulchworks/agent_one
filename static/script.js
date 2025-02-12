async function submitTopic() {
    const topic = document.getElementById('topicInput').value;
    if (!topic.trim()) {
        alert('Please enter a topic.');
        return;
    }

    // Clear previous results
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '<p>Loading...</p>';

    try {
        // Send the topic to the Flask backend
        const response = await fetch('/run', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ topic })
        });

        const data = await response.json();

        if (response.ok) {
            // Parse and format the result as a report
            const formattedReport = formatReport(data.result);
            resultDiv.innerHTML = `<strong>Result:</strong> ${formattedReport}`;
        } else {
            // Display error message
            resultDiv.innerHTML = `<strong>Error:</strong> ${data.error}`;
        }
    } catch (error) {
        // Handle network or other errors
        resultDiv.innerHTML = `<strong>Error:</strong> Failed to fetch data. Please try again.`;
    }
}

function formatReport(reportContent) {
    // Convert Markdown-like content into HTML
    return reportContent
        .replace(/# (.+)/g, '<h2>$1</h2>') // Convert headings
        .replace(/## (.+)/g, '<h3>$1</h3>') // Convert subheadings
        .replace(/\n\n/g, '</p><p>') // Convert paragraphs
        .replace(/\n/g, '<br>') // Handle line breaks
        .replace(/<\/p><p>$/, ''); // Remove trailing paragraph tags
}