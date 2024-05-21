const showMsg = document.querySelector('[submit]')
const msg = document.querySelector('.msg')

showMsg.addEventListener("click", () => {
    msg.textContent = "Profissional cadastrado com sucesso!!!"
    msg.style.color = "red"
    msg.style.fontSize = "20px"
    msg.style.border = "1px solid red"
    msg.style.borderRadius = "5px"
    msg.style.padding = "10px"
    msg.style.display = "block"
})
