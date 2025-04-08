document.addEventListener('DOMContentLoaded', function() {
    const navIcons = document.querySelectorAll('.nav-icon');

        navIcons.forEach(icon => {
            icon.addEventListener('click', function(event) {
                event.preventDefault();

                const page = this.dataset.page;

                switch (page) {
                    case 'home':
                        window.location.href = '../';
                        break;
                    case 'myapplication':
                        window.location.href = '../myapplication';
                        break;
                    case 'frequent':
                        window.location.href = '../frequent';
                        break;
                    case 'profile':
                        window.location.href = '../profile';
                        break;
                    default:
                        console.warn('Unknown page:', page);
                }
            });
        });


    document.querySelectorAll('.expand-button').forEach(button => {
        button.addEventListener('click', () =>{
            const content = button.parentElement.nextElementSibling;
            if (content.style.maxHeight === '0px' || content.style.maxHeight === '') {
                content.style.maxHeight = content.scrollHeight + 'px';
                content.style.padding = '10px 10px';
                button.textContent = 'x';
            } else {
                content.style.maxHeight = '0';
                content.style.padding = '0 10px';
                button.textContent = '+';
            }
        });
    });
})