function toggleDisplay(element) {
    element.style.display = element.style.display === 'none' ? 'block' : 'none';
  }
  
  document.getElementById('toggleLink').addEventListener('click', function() {
    toggleDisplay(document.getElementById('content'));
  });