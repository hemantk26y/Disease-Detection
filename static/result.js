function showResult() {
    const form = document.getElementById('upload-form');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText);
                    displayResult(response);
                } else {
                    console.error('Error:', xhr.status);
                }
            }
        };
        xhr.open('POST', form.action, true);
        xhr.send(formData);
    });
}

function displayResult(response) {
    const popDiv = document.getElementById('pop');
    popDiv.style.display = 'block';

    const outputImg = document.getElementById('output');
    if (response.image) {
        outputImg.src = response.image;
        outputImg.style.display = 'block';
    } else {
        outputImg.style.display = 'none';
    }

    const p1 = document.getElementById('p1');
    p1.textContent = 'Name: ' + response.first_name + ' ' + response.last_name;
    const p2 = document.getElementById('p2');
    p2.textContent = 'Age: ' + response.age;
    const p3 = document.getElementById('p3');
    p3.textContent = 'Gender: ' + response.gender;
    const p4 = document.getElementById('p4');
    p4.textContent = 'Result: ' + response.prediction;
}
function showResult() {
    const form = document.getElementById('upload-form');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText);
                    displayResult(response);
                } else {
                    console.error('Error:', xhr.status);
                }
            }
        };
        xhr.open('POST', form.action, true);
        xhr.send(formData);
    });
}

function displayResult(response) {
    const popDiv = document.getElementById('pop');
    popDiv.style.display = 'block';

    const outputImg = document.getElementById('output');
    if (response.image) {
        outputImg.src = response.image;
        outputImg.style.display = 'block';
    } else {
        outputImg.style.display = 'none';
    }

    const p1 = document.getElementById('p1');
    p1.textContent = 'Name: ' + response.first_name + ' ' + response.last_name;
    const p2 = document.getElementById('p2');
    p2.textContent = 'Age: ' + response.age;
    const p3 = document.getElementById('p3');
    p3.textContent = 'Gender: ' + response.gender;
    const p4 = document.getElementById('p4');
    p4.textContent = 'Result: ' + response.prediction;
}
function showResult() {
    const form = document.getElementById('upload-form');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText);
                    displayResult(response);
                } else {
                    console.error('Error:', xhr.status);
                }
            }
        };
        xhr.open('POST', form.action, true);
        xhr.send(formData);
    });
}

function displayResult(response) {
    const popDiv = document.getElementById('pop');
    popDiv.style.display = 'block';

    const outputImg = document.getElementById('output');
    if (response.image) {
        outputImg.src = response.image;
        outputImg.style.display = 'block';
    } else {
        outputImg.style.display = 'none';
    }

    const p1 = document.getElementById('p1');
    p1.textContent = 'Name: ' + response.first_name + ' ' + response.last_name;
    const p2 = document.getElementById('p2');
    p2.textContent = 'Age: ' + response.age;
    const p3 = document.getElementById('p3');
    p3.textContent = 'Gender: ' + response.gender;
    const p4 = document.getElementById('p4');
    p4.textContent = 'Result: ' + response.prediction;
}
