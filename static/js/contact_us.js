const sendbutton = document.querySelector('btnSendMessage');
const name = document.querySelector('txtName')
const email = document.querySelector('txtEmail')
const phone = document.querySelector('txtPhone')
const message = document.querySelector('txtMsg')

sendbutton.addEventListener('click', SendMessage, false);

function SendMessage() {
    const url = 'http://127.0.0.1:8000/name=' + name + '&email=' + email + '&phone=' + phone + '&message=' + message
    $.post(url, function(){})
}