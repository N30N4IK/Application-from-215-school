document.addEventListener('DOMContentLoaded', function() {
    const filterbutton = document.querySelectorAll('.filter-buttons button');

    filterbutton.forEach(button => {
      button.addEventListener('click', function(event) {
        event.preventDefault();

        const page = this.dataset.page;

        switch (page) {
          case 'filter':
            window.location.href = '/myapplication/filter';
            break;
          case 'create':
            window.location.href = '/myapplication/create';
            break;
          case 'chats':
            window.location.href = '/myapplication/chats';
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

        switch(page) {
            case 'home':
                window.location.href = '../';
                break;
              case 'tasks':
                window.location.href = '../myapplication';
                break;
              case 'frequent':
                window.location.href = '../frequent';
                break;
              case 'profile':
                window.location.href = '../profile';
                break;
              case 'application':
                window.location.href = '../application';
                break;
              default:
              console.warn('Unknown page:', page);
        }
      });
    });
});
