
const render = (type) => {
    const btns = document.querySelectorAll('#btn');
    const lists = document.querySelectorAll('#list')

    lists.forEach(list => list.style.display = type === list.dataset.menu ? 'block' : 'none');

    btns.forEach(btn => {
        const isCurrent=  btn.dataset.menu === type

        if (isCurrent) btn.classList.add('active')
        else btn.classList.remove('active')
    });
}

render('ios')

