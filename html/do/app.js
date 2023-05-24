const name = document.querySelector('#name');
const index = document.querySelector('#index');
const tmi = document.querySelector('#tmi');

name.addEventListener('click', e => {
    index.classList.remove('hide');
    index.classList.add('show');
}); 

index.addEventListener('click', e => {
    tmi.classList.remove('hide');
    tmi.classList.add('show');
});