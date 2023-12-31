// Keep scroll position when reloading page  

    document.addEventListener("DOMContentLoaded", function(event) { 
        var scrollpos = sessionStorage.getItem('scrollpos');
        if (scrollpos) window.scrollTo(0, scrollpos);
    });

    window.onbeforeunload = function(e) {
        sessionStorage.setItem('scrollpos', window.scrollY);
    };


// Toggle sidebar profile menu
function toggleDisplay(element) {
    element.style.display = element.style.display === 'none' ? 'block' : 'none';
  }
  
  document.getElementById('toggleLink').addEventListener('click', function() {
    toggleDisplay(document.getElementById('content'));
  });

// Close button inside sidebar profile menu  
function hideMenu() {
    var list = document.getElementById("content");
        list.style.display = "none";
    }


// Select the timeout element
var alert = document.querySelector('.timeout');

// Set a timeout to remove the alert after 3 seconds
setTimeout(function() {
  alert.remove();
}, 3000);