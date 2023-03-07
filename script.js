//toujours en haut
window.scrollTo(0,0);
console.log("salut");
//no-scroll

document.body.style.overflowY = 'hidden';
setTimeout(()=> {
    document.body.style.overflowY = 'auto';
}, 2000);


/*apparition au deffilement */
const threshold = .1
const options = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
}

const handleIntersect = function (entries, observer) {
    entries.forEach(function (entry) {
        if (entry.intersectionRatio > threshold) {
            entry.target.classList.add('reveal-visible')
            observer.unobserve(entry.target)
        }
    })
}

window.addEventListener("DOMContentLoaded", function () {
    const observer = new IntersectionObserver(handleIntersect, options)
    const targets = document.querySelectorAll('.reveal')
    targets.forEach(function (target) {
        observer.observe(target)
    })
})



//cursor 
const cursor = document.querySelector('.cursor');

document.addEventListener('mousemove', e => {
    cursor.setAttribute('style' , 'top:'+(e.clientY)+"px; left:"+(e.clientX)+"px;")
    /*
    const mouseX = e.clientX;
    const mouseY = e.clientY;

    cursorRounded.style.top = (mouseY-20) + "px";
    cursorRounded.style.left = (mouseX-20) + "px";
    console.log(mouseX);
    console.log(mouseY);
    */
    document.addEventListener('mouseover', e => {
        const target = e.target;
        if(target.matches('.Contact a')){
            cursor.classList.add('active2');
        }
        if (target.matches('a')||target.matches('.name h1')||target.matches('.langages h1')||target.matches('.langagesMax h1')) {
          cursor.classList.add('active');
        } else {
          cursor.classList.remove('active');
          cursor.classList.remove('active2');
        }
      });
});
