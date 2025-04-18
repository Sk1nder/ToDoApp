// Date in footer
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("year").innerHTML = new Date().getFullYear();
});


// Calendar
document.addEventListener("DOMContentLoaded", function() {
  flatpickr("#DateField", {
    enableTime: true,
    dateFormat: "d-m-Y H:i",
    time_24hr: true,
    });
   flatpickr("#endDateField", {
    enableTime: true,
    dateFormat: "d-m-Y H:i",
    time_24hr: true,
    });
  flatpickr("#dueDateField", {
    enableTime: true,
    dateFormat: "d-m-Y H:i",
    time_24hr: true,
    });
});

document.addEventListener("DOMContentLoaded", function() {
  function toggleText() {
      var checkBox = document.querySelector("[name='checkbox']");
      var text = document.getElementById("displayText");

      if (checkBox.checked == true){
          text.innerHTML = "Status: completed";
      } else {
          text.innerHTML = "Status: not completed";
      }
    }
    window.onload = function() {
            toggleText();
    };
});


document.addEventListener("DOMContentLoaded", function () {
    function toggleText() {
        var checkBox = document.querySelector("[name='checkbox']");
        var text = document.getElementById("displayText");
        var endDateField = document.getElementById("endDateField");

        if (checkBox.checked) {
            text.innerHTML = "Status: completed";
            endDateField.disabled = false;
            endDateField.required = true;
        } else {
            text.innerHTML = "Status: not completed";
            endDateField.value = ""; // Kasowanie wartości
            endDateField.disabled = true;
            endDateField.required = false;
        }
    }

    // Inicjalizacja stanu przy załadowaniu strony
    function initialize() {
        var checkBox = document.querySelector("[name='checkbox']");
        var endDateField = document.getElementById("endDateField");
        var endDateValue = document.getElementById("endDateValue").value;

        if (checkBox.checked) {
            endDateField.value = endDateValue; // Ustawienie daty tylko dla checked
            endDateField.disabled = false;
            endDateField.required = true;
        } else {
            endDateField.value = ""; // Kasowanie wartości
            endDateField.disabled = true;
            endDateField.required = false;
        }
    }

    // Wywołanie funkcji inicjalizacji na start
    initialize();

    // Dodanie nasłuchiwacza zdarzeń dla checkboxa
    var checkBox = document.querySelector("[name='checkbox']");
    checkBox.addEventListener("change", toggleText);
});


