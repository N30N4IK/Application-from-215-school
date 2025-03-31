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
 
       const menuButtons = document.querySelectorAll('.cancel-button');
 
       menuButtons.forEach(button => {
           button.addEventListener('click', function(event) {
               event.preventDefault();

               const page = this.dataset.page;

               switch (page) {
                case 'cancel':
                  window.location.href = '../myapplication';
                  break
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
 
       const dataButtons = document.querySelectorAll('.data-button');
 
       dataButtons.forEach(button => {
           button.addEventListener('click', function() {
               // Remove active class from all buttons
               dataButtons.forEach(btn => btn.classList.remove('active'));
               // Add active class to the clicked button
               this.classList.add('active');
           });
       });
 });
 