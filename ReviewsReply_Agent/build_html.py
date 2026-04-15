import re

with open(r"UI Design\code.html", "r", encoding="utf-8") as f:
    html = f.read()

# -----------------------------
# SIDEBAR UPDATE
# -----------------------------
sidebar = """
<a onclick="navigate('dashboard')">Dashboard</a>
<a onclick="navigate('vault')">Document Vault</a>
<a onclick="navigate('readymade')">Readymade Replies</a>
"""

html = re.sub(r'Dashboard.*Document Vault', sidebar, html, flags=re.DOTALL)

# -----------------------------
# INPUT + REFRESH
# -----------------------------
input_block = """
<input id="reviewer-name" placeholder="Reviewer Name">

<div style="position:relative">
<textarea id="review-text" placeholder="Paste review"></textarea>

<button onclick="clearInput()" style="position:absolute;right:10px;top:10px;">
🔄
</button>
</div>

<button onclick="generateReply()">Generate</button>
"""

html = re.sub(r'<textarea.*?</textarea>', input_block, html, flags=re.DOTALL)

# -----------------------------
# RESPONSE + BUTTONS
# -----------------------------
response_block = """
<div id="ai-response-text">Waiting...</div>

<button onclick="regenerate()">🔁 Regenerate</button>
<button onclick="copyResponse()">📋 Copy</button>
"""

html = html.replace("Waiting for input...", response_block)

# -----------------------------
# JAVASCRIPT
# -----------------------------
js = """
<script>
let currentRestaurant = 'Aroma Indian';
let lastReview = "";

function navigate(page){
    if(page=='readymade') window.location='/readymade';
    if(page=='vault') window.location='/vault';
}

function clearInput(){
    document.getElementById('review-text').value='';
    document.getElementById('reviewer-name').value='';
}

async function generateReply(){
    const text = document.getElementById('review-text').value;

    lastReview = text;

    const res = await fetch('/api/generate',{
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({
            review_text:text,
            restaurant:currentRestaurant
        })
    });

    const data = await res.json();
    document.getElementById('ai-response-text').innerText = data.reply;
}

function regenerate(){
    generateReply();
}

function copyResponse(){
    const text = document.getElementById('ai-response-text').innerText;
    navigator.clipboard.writeText(text);

    // AUTO CLEAR AFTER COPY
    clearInput();
}
</script>
</body>
"""

html = html.replace("</body>", js)

with open(r"templates\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ UI Updated with all features")