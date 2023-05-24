const blackBox = document.querySelector('#black');
const text = document.querySelector('#text');

blackBox.addEventListener('click', e => {
    text.classList.toggle('big');
    // blackBox.style.backgroundColor = 'red';
}); 