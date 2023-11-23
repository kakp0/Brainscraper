let divElements = document.querySelectorAll('div.scf-face');
let count = 0;
let outputContent = "";

divElements.forEach((divElement) => {
    let pElements = divElement.querySelectorAll('p');
    pElements.forEach((pElement, index) => {
        outputContent += pElement.innerHTML + "\n";
        count++;
        if (count % 3 === 0) {
            outputContent += "\n";
        }
    });
});

console.log(outputContent);
console.log(`Found and printed ${count} times.`);
