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
const cursorRounded = document.querySelector('.cursor');

document.addEventListener('mousemove', e => {
    const mouseX = e.pageX;
    const mouseY = e.pageY;

    cursorRounded.style.top = mouseY + "px";
    cursorRounded.style.left = mouseX + "px";
})

//scroll

// Supprimer la classe 'no-scroll' après 2 secondes
document.body.style.overflowY = 'hidden';
setTimeout(()=> {
    document.body.style.overflowY = 'auto';
    console.log("salut");
}, 2000);
