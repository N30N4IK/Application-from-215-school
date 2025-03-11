document.addEventListener('DOMContentLoaded', function() {
    const menuButtons = document.querySelectorAll('.menu-button');

    menuButtons.forEach(button => {
      button.addEventListener('click', function(event) {
        event.preventDefault();

        const page = this.dataset.page;

        switch (page) {
          case 'myapplication':
            window.location.href = '/myapplication';
            break;
          case 'frequent-requests':
            window.location.href = '/frequent';
            break;
          case 'reviews':
            window.location.href = '/reviews';
            break;
          case 'faq':
            window.location.href = '/frequent';
            break;
          default:
            console.warn('Unknown page:', page);
        }
      });
      });

  const navIcons = document.querySelectorAll('.nav-icon');

    navIcons.forEach(icon => {
      icon.addEventListener('click', function(event) {
        event.preventDefault();

        const page = this.dataset.page;

        switch (page) {
          case 'home':
            window.location.href = '/home';
            break;
          case 'myapplication':
            window.location.href = '/myapplication';
            break;
          case 'frequent':
            window.location.href = '/frequent';
            break;
          case 'profile':
            window.location.href = '../profile';
            break;
          default:
            console.warn('Unknown page:', page);
        }
      });
    });
  });
