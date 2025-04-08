document.addEventListener('DOMContentLoaded', function() {

    const filterButtons = document.querySelectorAll('.filter-buttons button');
 
       filterButtons.forEach(button => {
         button.addEventListener('click', function(event) {
           event.preventDefault();
 
           const page = this.dataset.page;
 
           switch (page) {
             case 'filter':
               window.location.href = '/myapplication/filter';
               break;
             case 'create':
               window.location.href = '/myapplication/';
               break;
             case 'chats':
               window.location.href = '/myapplication/chats';
               break;
             default:
               console.warn('Unknown page:', page);
           }
         });
       });

      const officeInputs = document.querySelectorAll('.data-input');

      officeInputs.forEach(input => {
          input.addEventListener('input', function (e) {
            this.value = this.value.slice(0, 4); // Ограничиваем ввод до 4 символов
          });
      });


       const menuButtons1 = document.querySelectorAll('.cancel-button');
 
       menuButtons1.forEach(button => {
           button.addEventListener('click', function(event) {
               event.preventDefault();

               const page = this.dataset.page;
               console.log('Clicked page:', page); // Отладка

               switch (page) {
                case 'cancel':
                  window.location.href = '../myapplication';
                  break;
               }
           });
       });

       const menuButtons2 = document.querySelectorAll('.save-button');
 
       menuButtons2.forEach(button => {
           button.addEventListener('click', function(event) {
               event.preventDefault();

               const page = this.dataset.page;
               console.log('Clicked page:', page); // Отладка

               switch (page) {
                case 'complete':
                  window.location.href = '../myapplication/create/complete';
                  break;
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
 
       const dataButtons = document.querySelectorAll('.type-button');
 
       dataButtons.forEach(button => {
           button.addEventListener('click', function() {
               // Remove active class from all buttons
               dataButtons.forEach(btn => btn.classList.remove('active-button'));
               // Add active class to the clicked button
               this.classList.add('active-button');
           });
       });
 });
 