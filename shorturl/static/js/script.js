function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
var csrftoken = getCookie("csrftoken");

const postUrlToBackend = (urlToShorten) => {
  const url = "https://url-shortener-avatarr95.herokuapp.com/url-generator/";
  // const url = "http://127.0.0.1:8000/url-generator/";
  fetch(url, {
    method: "POST",
    headers: {
      "X-CSRFToken": csrftoken,
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify({
      urlToShorten: urlToShorten,
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      document.querySelector(".form-control").value = "";
      document.querySelector(".shortened-url").innerHTML = ` 
      <a href="${data["long_url"]}" class="text-none text-white">Your shortened link is https://url-shortener-avatarr95.herokuapp.com/${data["short_url"]}/</a>
      `;

      debugger;
    })
    .catch((err) => console.log(err));
};

const submitButton = document.querySelector(".url-submit");
submitButton.addEventListener("click", () => {
  $(".shortened-url").fadeOut(250, () => {
    const urlInputVal = document.querySelector(".form-control").value;
    postUrlToBackend(urlInputVal);
    $(".shortened-url").fadeIn();
  });
});
