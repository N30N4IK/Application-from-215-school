document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.action-buttons');

    buttons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();

            const page = this.dataset.page;

            switch (page) {
                case 'cancel':
                    window.location.href = '../';
                    break;
                case 'okay':
                    window.location.href = '../complete';
                    break;
                default:
                    console.warn('Unknown page:', page);
            }
        });
    });
})