let myFridge = document.getElementById("fridge");
let addItem = document.getElementById("addItem");
let updateFridge = document.getElementById("updateFridge");

let showFridge = document.getElementById("myFridge-content");
let showAddItem = document.getElementById("addItem-content");
let showUpdate = document.getElementById("updateFridge-content");

let tempUp = document.getElementById("temp-up");
let tempDown = document.getElementById("temp-down");

let divTemp = document.getElementById("temp");
let tempNum = 40;

function myFridgeClick() {
    showFridge.style.display = "block";
    showUpdate.style.display = "none";
    showAddItem.style.display = "none";
}

function addItemClick() {
    showAddItem.style.display = "block";
    showUpdate.style.display = "none";
    showFridge.style.display = "none";
}

function updateFridgeClick() {
    showUpdate.style.display = "block";
    showAddItem.style.display = "none";
    showFridge.style.display = "none";
}

myFridge.addEventListener('click', myFridgeClick);
addItem.addEventListener('click', addItemClick);
updateFridge.addEventListener('click', updateFridgeClick);

function updateTempUp() {
    tempNum += -1;
    divTemp.innerHTML = tempNum + ' °F';
}

function updateTempDown() {
    tempNum += 1;
    divTemp.innerHTML = tempNum + ' °F';
}

tempUp.addEventListener('click', updateTempUp);
tempDown.addEventListener('click', updateTempDown);