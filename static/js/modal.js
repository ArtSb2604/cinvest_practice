let isOpen = false;
const modal = document.querySelector('#modal')

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