document.addEventListener('DOMContentLoaded', function(){
    const navIcons = document.querySelectorAll('.nav-icon');
 
       navIcons.forEach(icon => {
         icon.addEventListener('click', function(event) {
           event.preventDefault();
 
           const page = this.dataset.page;
 
           switch (page) {
             case 'home':
               window.location.href = '../';
               break;
             case 'tasks':
               window.location.href = '../myapplication';
               break;
             case 'clipboard':
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
})