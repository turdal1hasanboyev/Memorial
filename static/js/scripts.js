window.onload = function () {
    const errorMessage = document.querySelector('.error-message');
    setTimeout(() => {
        errorMessage.classList.add('show');
    }, 500);
};
