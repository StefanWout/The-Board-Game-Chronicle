document.addEventListener("DOMContentLoaded", function () {
  const editButtons = document.getElementsByClassName("btn-edit");
  const reviewText = document.getElementById("id_body");
  const reviewForm = document.getElementById("reviewForm");
  const submitButton = document.getElementById("submitButton");

  for (let button of editButtons) {
      button.addEventListener("click", (e) => {
          let reviewId = e.target.getAttribute("review_id");
          let reviewContent = document.getElementById(`review${reviewId}`).innerText;
          reviewText.value = reviewContent;
          submitButton.innerText = "Update";
          reviewForm.setAttribute("action", `edit_review/${reviewId}`);
      });
  }

  const deleteButtons = document.getElementsByClassName("btn-delete");
  const deleteConfirm = document.getElementById("deleteConfirm");

  for (let button of deleteButtons) {
      button.addEventListener("click", (e) => {
          e.preventDefault();  // Prevent the default action
          let reviewId = e.target.getAttribute("review_id");
          deleteConfirm.setAttribute("href", `/delete_review/${reviewId}`);
      });
  }
});