$(document).ready(function () {

    // Helpers 

    // Marks a field as invalid and shows an error message below it
    function showError($field, message) {
        $field.addClass("input-error");
        // Remove any existing error for this field before adding a new one
        $field.siblings(".error-msg").remove();
        $field.after(`<span class="error-msg">${message}</span>`);
    }

    // Removes the error state from a field
    function clearError($field) {
        $field.removeClass("input-error");
        $field.siblings(".error-msg").remove();
    }

    // Returns true if the string is a valid email address
    function isValidEmail(value) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
    }

    // Returns true if the name contains only letters and spaces (no numbers or special chars)
    // The regex allows: a-z, A-Z, spaces, and accented letters like á é í ó ú ñ ü
    function isValidName(value) {
        return /^[a-zA-ZÀ-ÿ\s]+$/.test(value.trim());
    }

    // Live validation: clear error as soon as the user fixes the field 

    $(".contact-form input, .contact-form textarea, .contact-form select")
        .on("input change", function () {
            if ($(this).val().trim() !== "") {
                clearError($(this));
            }
        });

    // Submit handler 

    $(".contact-form").on("submit", function (e) {
        e.preventDefault();

        let isValid = true;

        // 1. Full Name — only letters and spaces, no numbers or special characters
        const $name = $("#fullname");
        if ($name.val().trim() === "") {
            showError($name, "Please enter your full name.");
            isValid = false;
        } else if (!isValidName($name.val())) {
            showError($name, "Name can only contain letters and spaces (no numbers or special characters).");
            isValid = false;
        } else {
            clearError($name);
        }

        if (isValid) {
            alert("Form submitted successfully!");
            this.reset();
        }
    });

});
