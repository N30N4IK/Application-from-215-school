document.addEventListener("DOMContentLoaded", function() {

    const navIcon = document.querySelectorAll('.nav-icon');
            navIcon.forEach(icon => {
                icon.addEventListener('click', function(event) {
                    event.preventDefault();

                    const page = this.dataset.page;

                    switch (page) {
                        case 'home':
                            window.location.href = '/';
                            break;
                        case 'myapplication':
                            window.location.href = '/myapplication';
                            break;
                        case 'frequent':
                            window.location.href = '/frequent';
                            break;
                        case 'profile':
                            window.location.href = '/profile';
                            break;
                        default:
                            console.warn('Unknown page:', page);
                    }
            });
        });
});