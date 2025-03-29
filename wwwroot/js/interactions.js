document.getElementById('shakeBtn').addEventListener('click', function () {
    let question = document.getElementById('questionInput').value;
    document.getElementById('thinkingMessage').classList.remove('hidden');
    document.getElementById('shakeBtn').disabled = true;
    document.getElementById('magicBall').style.transform = "rotate(20deg)";

    setTimeout(function () {
        fetch('/Magic8Ball/GetAnswer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question: question })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('thinkingMessage').classList.add('hidden');
            document.getElementById('answerArea').innerText = data.Answer;
            document.getElementById('answerArea').classList.remove('hidden');
            document.getElementById('resetBtn').classList.remove('hidden');
            document.getElementById('magicBall').style.transform = "rotate(0deg)";
        });
    }, 3000);
});

document.getElementById('resetBtn').addEventListener('click', function () {
    document.getElementById('answerArea').classList.add('hidden');
    document.getElementById('resetBtn').classList.add('hidden');
    document.getElementById('shakeBtn').disabled = false;
    document.getElementById('questionInput').value = '';
});
