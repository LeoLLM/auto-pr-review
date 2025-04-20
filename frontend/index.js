// Frontend entry point

document.addEventListener('DOMContentLoaded', function() {
  const app = document.getElementById('app');
  
  if (app) {
    app.innerHTML = '<h1>PR Automation Test App</h1>';
    
    // Add a simple UI component
    const statusElement = document.createElement('div');
    statusElement.classList.add('status');
    statusElement.textContent = 'Ready to test PR automation';
    
    app.appendChild(statusElement);
  }
});