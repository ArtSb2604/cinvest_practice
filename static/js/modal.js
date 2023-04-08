let isOpen = false;
let isOpenForm = false
const modal = document.querySelector('#modal')
const form = document.querySelector('#form_modal')

const setScrollDisable = isDisable => {

    if (isDisable) {
        document.querySelector('body').style.overflowY = 'hidden'
        document.querySelector('html').style.overflowY = 'hidden'

        document.querySelector('html').style.touchAction = 'none'
        document.querySelector('body').style.touchAction = 'none'

    } else {
        document.querySelector('body').style.overflowY = 'visible'
        document.querySelector('html').style.overflowY = 'visible'

        document.querySelector('html').style.touchAction = 'auto'
        document.querySelector('body').style.touchAction = 'auto'
    }
}

const switchOpen = () => {
    setScrollDisable(!isOpen)
    modal.style.display = !isOpen ? 'block' : 'none'
    isOpen = !isOpen
}

const switchFormOpen = () => {
    setScrollDisable(!isOpenForm)
    form.style.display = !isOpenForm ? 'block' : 'none'
    isOpenForm = !isOpenForm
    if (isOpen === isOpenForm) {
        modal.style.display = !isOpen ? 'block' : 'none'
        isOpen = !isOpen
    }
    isOpen = !isOpen
}