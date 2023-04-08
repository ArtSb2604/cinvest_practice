let isOpen = false;
let isOpenForm = false
const modal = document.querySelector('#modal')
const form = document.querySelector('#form_modal')
const switchOpen = () => {
    modal.style.display = !isOpen ? 'block' : 'none'
    isOpen = !isOpen
}

const switchFormOpen = () => {
    form.style.display = !isOpenForm ? 'block' : 'none'
    isOpenForm = !isOpenForm
    if (isOpen === isOpenForm) {
        modal.style.display = !isOpen ? 'block' : 'none'
        isOpen = !isOpen
    }
    isOpen = !isOpen
}