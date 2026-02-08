async function searchWord() {
    const word = document.getElementById("wordInput").value;

    const res = await fetch(`/api/get/${word}`);
    const data = await res.json();

    const resultDiv = document.getElementById("result");

    if (!res.ok) {
        resultDiv.innerHTML = `<div class="alert alert-danger">Word not found</div>`;
        return;
    }

    let meaningsHTML = data.meanings.map(m => `<li>${m}</li>`).join("");
    let synonymsHTML = data.synonyms.join(", ");

    resultDiv.innerHTML = `
        <div class="card p-3 shadow">
            <h3>${data.word}</h3>
            <h5>Meanings</h5>
            <ul>${meaningsHTML}</ul>
            <h5>Synonyms</h5>
            <p>${synonymsHTML}</p>
        </div>
    `;
}
