// copy-to-clipboard functionality
document.addEventListener('DOMContentLoaded', () => {

    const button = document.getElementsByClassName('copy-button')[0];
    const copySvg = document.getElementsByClassName('copy-svg')[0];

    button.addEventListener('click', (event) => {
        event.preventDefault();

        const outputBox = document.getElementsByClassName('output-box')[0];
        const text = outputBox.textContent;

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
        svg.setAttribute("height", "24");
        svg.setAttribute("viewBox", "0 -960 960 960");
        svg.setAttribute("width", "24");
        svg.setAttribute("class", "copy-svg")
        const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
        path.setAttribute("d", "M382-240 154-468l57-57 171 171 367-367 57 57-424 424Z");

        svg.appendChild(path);

        if (navigator.clipboard) {
            navigator.clipboard.writeText(text.trim())
                .then(() => {
                    console.log('Text copied to clipboard successfully');
                    button.innerHTML = '';
                    button.appendChild(svg);
                    setTimeout(function() {
                        button.innerHTML = '';
                        button.appendChild(copySvg);
                    }, 3000);
                })
                .catch((error) => {
                    console.error('Unable to copy text to clipboard:', error);
                });
        } else {
            console.warn('Clipboard API not supported');
        }
    });
});

// element height modifier functionality 
document.addEventListener('DOMContentLoaded', function() {
    const outputBox = document.getElementById('outputBox');
    const inputBox = document.getElementById('input-field');
    const inputContainer = document.getElementById('input-container');
    const outputContainer = document.getElementById('output-container');
    console.log('Output Box:', outputBox);
    console.log('ClientHeight:', outputBox.clientHeight, inputBox.clientHeight)
    const maxHeight = 380;

    if (outputBox.clientHeight === maxHeight) {
        console.log('Maximum height reached!');
        outputBox.style.overflowY = 'scroll';
        inputBox.style.height = '380px'
        inputContainer.style.height = '465px'
    
    } else {
        if (outputBox.clientHeight > 214) {
            inputBox.style.height = 'auto';
        }
        inputContainer.style.height = outputContainer.clientHeight + 'px';
        console.log('Maximum height not reached yet.');
    }

});







  