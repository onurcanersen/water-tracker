let dates = JSON.parse(document.querySelector(".dates").value);
let amounts = JSON.parse(document.querySelector(".amounts").value);

new Chart("chart", {
    type: "bar",
    data: {
        labels: dates,
        datasets: [{
            label: "Amount",
            data: amounts
        }]
    }
});