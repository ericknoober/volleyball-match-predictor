const API = "http://localhost:8000"

// load teams into dropdowns
async function loadTeams(){
    const response = await fetch(`${API}/teams`)
    const data = await response.json()

    const homeSelect = document.getElementById("home-team")
    const awaySelect = document.getElementById("away-team")

    data.teams.forEach(team => {
       homeSelect.innerHTML += `<option value="${team}">${team}</option>`,
        awaySelect.innerHTML += `<option value="${team}">${team}</option>`
    })
}

//predict match outcomes
async function predict(){
    const home = document.getElementById("home-team").value
    const away = document.getElementById("away-team").value

//validation
//if one team is not selected
if(!home || !away){
    alert("Please select both teams.")
    return
}

//if both teams selected are the same
if (home === away){
    alert("Please select two different teams")
}

//call backend
//formatted to url
const response = await fetch(`${API}/predict?home=${home}&away=${away}`)
const data = await response.json()

//display results
document.getElementById("winner").innerText = data.predicted_winner
document.getElementById("confidence").innerText = `Confidence: ${data.confidence}`
document.getElementById("result").classList.remove("hidden")

//refresh history
loadHistory()

}

//load past predictions into table

async function loadHistory(){
    const response = await fetch(`${API}/history`)
    const data = await response.json()

    const tbody = document.getElementById("history-body")
    tbody.innerHTML = ""

    data.predictions.forEach(p => {
        tbody.innerHTML += `
        <tr>
                <td>${p.home_team}</td>
                <td>${p.away_team}</td>
                <td>${p.predicted_winner}</td>
                <td>${p.confidence}</td>
                <td>${p.timestamp}</td>
            </tr>
        `
    })
}

//run page
loadTeams()
loadHistory()
