async function submitTopic() {
    const topic = document.getElementById('topicInput').value;
    if (!topic.trim()) {
        alert('Please enter a topic.');
        return;
    }

    // Send the topic to the Flask backend
    const response = await fetch('/run', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ topic })
    });

    const data = await response.json();
    const resultDiv = document.getElementById('result');

    if (response.ok) {
        resultDiv.innerHTML = `<strong>Result:</strong> ${data.result}`;
    } else {
        resultDiv.innerHTML = `<strong>Error:</strong> ${data.error}`;
    }
}