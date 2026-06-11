//async and await functions use to run data in the background

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

function loadCharts(){
    //correlation chart
    const corrData = [{
        //hard coded data
        x:["Aces", "Blocks", "Kills"],
        y:[0.353, 0.210, 0.166],
        type: "bar",
        marker: {
            color: ["#000000", "#000000", "#000000"],
            opacity: 0.8
        }
    }]

    Plotly.newPlot("chart-correlation", corrData, {
        paper_bgcolor: "#1a1a2e",
        plot_bgcolor: "#1a1a2e",
        font: { color: "#ffffff" },
        margin: { t: 20 },
        yaxis: { title: "Correlation with Winning" }
    })

    // Chart 2 - home vs away
    const homeAwayData = [{
        x: ["Home", "Away"],
        y: [37.1, 62.9],
        type: "bar",
        marker: {
            color: ["#4facfe", "#00f2fe"],
            opacity: 0.8
        },
        text: ["37.1%", "62.9%"],
        textposition: "outside"
    }]

    Plotly.newPlot("chart-homeaway", homeAwayData, {
        paper_bgcolor: "#1a1a2e",
        plot_bgcolor: "#1a1a2e",
        font: { color: "#ffffff" },
        margin: { t: 20 },
        yaxis: { title: "Win Rate %", range: [0, 100] }
    })

    // Chart 3 - team wins
    const teamData = [{
        x: ["Brazil", "Bulgaria", "Ukraine", "Germany", "Poland", 
            "Italy", "China", "Serbia", "Argentina", "France",
            "Cuba", "Iran", "Japan", "Netherlands", "Slovenia",
            "Türkiye", "USA", "Canada"],
        y: [8, 5, 4, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        type: "bar",
        marker: {
            color: "#4facfe",
            opacity: 0.8
        }
    }]

    Plotly.newPlot("chart-teams", teamData, {
        paper_bgcolor: "#1a1a2e",
        plot_bgcolor: "#1a1a2e",
        font: { color: "#ffffff" },
        margin: { t: 20 },
        xaxis: { tickangle: -45 },
        yaxis: { title: "Home Wins" }
    })
}

//run page
loadTeams()
loadHistory()
loadCharts()
