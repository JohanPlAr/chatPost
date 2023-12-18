// Keep scroll position when reloading page  
document.addEventListener("DOMContentLoaded", function(event) { 
  var scrollpos = sessionStorage.getItem('scrollpos');
  if (scrollpos) window.scrollTo(0, scrollpos);
});

window.onbeforeunload = function(e) {
  localStorage.setItem('scrollpos', window.scrollY);
};


// Toggle sidebar profile menu
function toggleDisplay(element) {
    element.style.display = element.style.display === 'none' ? 'block' : 'none';
  }
  
  document.getElementById('toggleLink').addEventListener('click', function() {
    toggleDisplay(document.getElementById('content'));
  });


