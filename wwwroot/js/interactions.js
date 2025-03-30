document.getElementById('shakeBtn').addEventListener('click', function (e) {
    e.preventDefault();  // Prevent accidental form GET
    let question = document.getElementById('questionInput').value;

    // Hide the button immediately
    shakeBtn.classList.add('hidden');
    thinkingMessage.classList.remove('hidden');
    magicBall.style.transform = "rotate(20deg)";

    setTimeout(function () {
        fetch('/Magic8Ball/GetAnswer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question: question })
        })
        .then(response => response.json())
        .then(data => {
            console.log("[CLIENT DEBUG] Response:", data);
        
            const answer = data.Answer || data.answer || "No wisdom returned...";
            document.getElementById('answerArea').innerText = answer;
        
            document.getElementById('thinkingMessage').classList.add('hidden');
            document.getElementById('answerArea').classList.remove('hidden');
            document.getElementById('resetBtn').classList.remove('hidden');
            document.getElementById('magicBall').style.transform = "rotate(0deg)";
        })
        .catch(err => {
            console.error("[CLIENT ERROR]", err);
            document.getElementById('answerArea').innerText = "An error occurred...";
        });        
    }, 3000);
});

document.getElementById('resetBtn').addEventListener('click', function () {
    document.getElementById('answerArea').classList.add('hidden');
    document.getElementById('resetBtn').classList.add('hidden');
    document.getElementById('shakeBtn').classList.remove('hidden'); // bring it back
    document.getElementById('questionInput').value = '';
});
