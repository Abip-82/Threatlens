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

function showPage(id){
    document.querySelectorAll('.page-content').forEach(p => p.style.display =  'none');
    document.getElementById(id).style.display = 'flex';
}

async function crypto(mode){
    let text = document.getElementById("cryptotext").value;
    let key = document.getElementById("cryptokey").value;
    let display = document.getElementById("cryptoresult");

    display.innerText = "Processing ...";

    let response = await fetch('http://127.0.0.1:5000/crypto', {
        method : 'POST',
        headers : {'Content-Type' : 'application/json'},
        body : JSON.stringify({text:text , key:key , mode: mode})
    });
    let data = await response.json();
    display.innerText = "Result : " + data.result;
}