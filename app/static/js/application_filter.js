document.addEventListener('DOMContentLoaded', function() {
    const statusButton = document.querySelectorAll('.status-button');

    statusButton.forEach(button => {
        button.addEventListener('click', function() {
            statusButton.forEach(btn => btn.classList.remove('active-button'));
            this.classList.add('active-button')
        });
    });

    const filterButton = document.querySelectorAll('.direction-button');

    filterButton.forEach(button => {
        button.addEventListener('click', function() {
            console.log(this);
            filterButton.forEach(btn => btn.classList.remove('active-buttons'));
            this.classList.add('active-buttons');
        });
    });
    
    const dateInput = document.querySelector('.date-input');
    dateInput.addEventListener('input', function (e) {
        // Удаляем все символы, кроме цифр
        let value = this.value.replace(/\D/g, '');
        // Добавляем точки в нужных местах
        if (value.length >= 2) {
            value = value.slice(0, 2) + '.' + value.slice(2);
        }
        if (value.length >= 5) {
            value = value.slice(0, 5) + '.' + value.slice(5);
        }
        // Ограничиваем длину ввода до 10 символов
        this.value = value.slice(0, 10);
    });
    // Обработчик события для удаления символов
    dateInput.addEventListener('keydown', function (e) {
        if (e.key === 'Backspace') {
            const value = this.value;
            // Проверяем, если последний символ - это точка
            if (value[value.length - 1] === '.') {
                // Удаляем точку вместе с предыдущим символом
                this.value = value.slice(0, -1);
            }
        }
    });
})