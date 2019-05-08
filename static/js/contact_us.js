const sendbutton = document.querySelector('btnSendMessage');
const name = document.querySelector('txtName')
const name = document.querySelector('txtName')
const name = document.querySelector('txtName')

sendbutton.addEventListener('click', SendMessage, false);

function SendMessage() {
  console.log(document.getElementById('number').value);
  document.getElementById("submit").innerHTML = "LOADING...";
}