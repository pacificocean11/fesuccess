function showSpinner() {
  document.getElementById("spinner").style.display = "block";
}

function hidespinner() {
  document.getElementById("spinner").style.display = "none";
}

function showCorrectIcon() {
  let selectedAnswer = document.querySelector('input[name="option"]:checked');
  let divClass = selectedAnswer.id;
  icon = document.createElement("i");
  icon.setAttribute("class", "bi bi-check-circle ms-4");
  icon.setAttribute("style", "color:green;");
  document.getElementsByClassName(divClass)[0].appendChild(icon);
}

function showWrongIcon(cad) {
  let selectedAnswer = document.querySelector('input[name="option"]:checked');
  let divClass = selectedAnswer.id;
  icon = document.createElement("i");
  icon.setAttribute("class", "bi bi-x-circle ms-4");
  icon.setAttribute("style", "color:red;");
  document.getElementsByClassName(divClass)[0].appendChild(icon);

  icon_r = document.createElement("i");
  icon_r.setAttribute("class", "bi bi-check-circle ms-4");
  icon_r.setAttribute("style", "color:green;");
  document.getElementsByClassName(cad)[0].appendChild(icon_r);
}
