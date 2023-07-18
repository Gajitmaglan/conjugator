var essereElements = document.getElementsByClassName('essereBox');
var avereElements = document.getElementsByClassName('avereBox');

document.addEventListener("DOMContentLoaded", function() {
    if (essereElements.length > 0 && avereElements.length > 0) {
        for (var i = 0; i < essereElements.length; i++) {
            essereElements[i].style.display = 'none';
        }
    }
});

let switcher = document.getElementById("switcher");
if (switcher) {
    switcher.addEventListener('click', function() {
        for (var i = 0; i < essereElements.length; i++) {
            essereElements[i].style.display = (essereElements[i].style.display === 'none') ? 'block' : 'none';
        }
    
        for (var j = 0; j < avereElements.length; j++) {
            avereElements[j].style.display = (avereElements[j].style.display === 'none') ? 'block' : 'none';
        }
    });
}