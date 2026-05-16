async function analyze(){
    const url = document.getElementById("urlInput").value;

    document.getElementById("result").innerText = "Analyzing...";

    const res = await fetch("http://127.0.0.1:5000/analyze",{
        method : "POST",
        headers : {'Content-Type' : 'application/json'},
        body : JSON.stringify({url:url})
    });

    const data = await res.json();
    document.getElementById("result").innerText = `${data.verdict} \n Risk Score: ${data.risk_score}\n\n` + data.reasons.join('\n');
}