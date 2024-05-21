const showMsg = document.querySelector('[data-showMsg]')
const msg = document.querySelector('.msg')

showMsg.addEventListener("click", () => {
    msg.textContent = "A senha foi redefinida com sucesso!"
    msg.style.color = "red"
    msg.style.fontSize = "20px"
    msg.style.border = "1px solid red"
    msg.style.borderRadius = "5px"
    msg.style.padding = "10px"
    msg.style.display = "block"
})
