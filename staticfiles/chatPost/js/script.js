// Keep scroll position when reloading page  

    document.addEventListener("DOMContentLoaded", function(event) { 
        var scrollpos = sessionStorage.getItem('scrollpos');
        if (scrollpos) window.scrollTo(0, scrollpos);
    });

    window.onbeforeunload = function(e) {
        sessionStorage.setItem('scrollpos', window.scrollY);
    };

// Toggle sidebar profile menu and close profile menu button
function toggleDisplay(element) {
    element.style.display = element.style.display === 'none' ? 'block' : 'none';
  }
  document.getElementById('toggleLink').addEventListener('click', function() {
    toggleDisplay(document.getElementById('content'));
  });
function closeMenu() {
    let element = document.getElementById('content');
    element.style.display = element.style.display === 'none' ? 'block' : 'none';
  }

// Set a timeout to remove the alert after 3 seconds
if (document.querySelector('.alert')) {
  setTimeout(function() {
    document.querySelector('.alert').remove();
  }, 3000);
}