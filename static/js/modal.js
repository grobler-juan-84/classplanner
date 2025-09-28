// Open modal
function openModal(studentName) {
    const modal = document.getElementById("studentModal");
    const modalTitle = document.getElementById("modalTitle");
    const modalBody = document.getElementById("modalBody");
  
    modalTitle.textContent = studentName;
    modalBody.textContent = `${studentName}'s details will appear here.`;
  
    modal.style.display = "block";
  }
  
  // Close modal
  function closeModal() {
    const modal = document.getElementById("studentModal");
    modal.style.display = "none";
  }
  
  // Close modal if user clicks outside
  window.onclick = function(event) {
    const modal = document.getElementById("studentModal");
    if (event.target === modal) {
      modal.style.display = "none";
    }
  };
  