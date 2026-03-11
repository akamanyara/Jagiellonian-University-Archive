function SpawnListener() {
    const boxes = document.querySelectorAll('.FullWidthImg');

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('Visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    boxes.forEach(box => observer.observe(box));
}