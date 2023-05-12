function openDropDown() {
    document.querySelector('header ion-icon').classList.toggle('active')
    document.querySelector('header .lang .list').classList.toggle('active')
}

function focusInput(num) {
    document.querySelector(`#input${num}`).focus()
    document.querySelector(`.input${num}`).classList.add('focused')

    document.querySelector(`#input${num}`).addEventListener("focusout", (e) => {
        document.querySelector(`.input${num}`).classList.remove('focused')
    });
}

function activeItem(id) {
    document.querySelector(`.item${id}`).classList.toggle('active')
}

function openMenu() {
    document.querySelector('.navigation').classList.toggle('active')
}