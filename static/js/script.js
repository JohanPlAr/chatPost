let scrollId = document.getElementById()

// Save the scroll position before the form is submitted
$('form').submit(function() {
    var scrollPos = $('#like_comment{{comment.pk}}').scrollSnap();
    console.log(#like_comment{{comment.pk}})
    localStorage.setItem('scrollPos', scrollPos);
});

// Restore the scroll position after the page is reloaded
$(document).ready(function() {
    var scrollPos = localStorage.getItem('scrollPos');
    if (scrollPos) {
        $('#like_comment{{comment.pk}}').scrollSnap(scrollPos);
        localStorage.removeItem('scrollPos'); // Optional: remove the stored scroll position
    }
});

