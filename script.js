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

/*load screan*/ 

window.addEventListener("load", function() {
    var loader = document.getElementById("Background");
    setTimeout(function() {
      loader.style.display = "none";
    }, 2000);
  });