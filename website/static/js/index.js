function toggleAnswer(element) {
    var answer = element.nextElementSibling;
    answer.classList.toggle('show');
    var toggle = element.querySelector('.toggle');
    toggle.textContent = (toggle.textContent === '+') ? '-' : '+';
}

function deleteReview(reviewId) {
    fetch("/delete-review", {
      method: "POST",
      body: JSON.stringify({ reviewId: reviewId }),
    }).then((_res) => {
      window.location.href = "/write.html";
    });
  }
  