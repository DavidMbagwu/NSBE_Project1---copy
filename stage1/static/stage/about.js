const imgs = document.querySelectorAll('.slideshow ul img');
const prev_btn = document.querySelector('.prev_btn');
const next_btn = document.querySelector('.next_btn');

let n = 0;

function changeSlide(){
    for (let i = 0; i < imgs.length; i++) {
        imgs[i].style.display = 'none';
    }
    imgs[n].style.display = 'block';
}

changeSlide();

prev_btn.addEventListener('click', ()=>{

    if (n == 0) {
        n = imgs.length - 1;
    } else {
        n--;
    }
    changeSlide();
});

next_btn.addEventListener('click', ()=>{

    if (n == imgs.length - 1) {
        n = 0;
    } else {
        n++;
    }
    changeSlide();
});