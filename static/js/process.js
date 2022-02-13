let process = document.querySelector(".process");
let total = document.querySelector(".total").value;
let target = document.querySelector(".target").value;
let percentage = parseInt(total) / parseInt(target) * 100;

process.style.background = `conic-gradient(
    #4d5bf9 ${percentage * 3.6}deg,
    #cadcff ${percentage * 3.6}deg
)`;