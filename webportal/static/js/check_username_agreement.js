var element = document.getElementById("id_username");
element.classList.add("form-control");

let isChecked = document.getElementById("id_name_agreement").value === "Yes"

document.getElementById("name_checkbox").checked = isChecked;

function changeUserAgreement() {
  if (isChecked) {
      document.getElementById("id_name_agreement").value = "No";
      isChecked = false;
      return;
  }
  document.getElementById("id_name_agreement").value = "Yes";
  isChecked = true;
}


var element = document.getElementById("name_checkbox");
element.classList.add("form-control");

let isChecked = document.getElementById("id_user-name_agreement").value === "Yes"

document.getElementById("name_checkbox").checked = isChecked;

function changeUserAgreement() {
  if (isChecked) {
      document.getElementById("id_user-name_agreement").value = "No";
      isChecked = false;
      return;
  }
  document.getElementById("id_user-name_agreement").value = "Yes";
  isChecked = true;
}