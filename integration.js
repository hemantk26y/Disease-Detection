function getData() {
    const fName = document.getElementById('name1').value;
    const lName = document.getElementById('name2') .value;
    const name = fName + ' ' + lName;
    const phone = document.getElementById('phone').value;
    const gen = document.getElementById('gender').value;
    const email = document.getElementById('email').value;
    const age = document.getElementById('age').value;
    return name, phone, gen, email, age;
}