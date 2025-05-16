const faders = document.querySelectorAll(".fade-in");
const rotate = document.querySelectorAll(".rotate");

const appearOptions = {
    threshold: 0,
    rootMargin: "0px 0px -300px 0px"
};

const appearOnScroll = new IntersectionObserver(function(
    entries,
    appearOnScroll
) {
    entries.forEach(entry => {
        if (!entry.isIntersecting) {
            return;
        } else {
            entry.target.classList.add("appear");
            appearOnScroll.unobserve(entry.target)
        }
    });
},
appearOptions);


faders.forEach(fader => {
    appearOnScroll.observe(fader);
});


$(".images img").click(function(){
    $("#full-image").attr("src", $(this).attr("src"));
    $('#image-viewer').show();
});

$("#image-viewer .close").click(function(){
    $('#image-viewer').hide();
});
