document.addEventListener('DOMContentLoaded', function() {
            const dateInput = document.getElementById('appointment-date');
            const unavailableDates = JSON.parse('{{ unavailable_dates|safe|escapejs }}');
            
            flatpickr(dateInput, {
                dateFormat: 'Y-m-d',
                disable: unavailableDates.map(date => {
                    return new Date(date);
                }),
                inline: true, // Exibir calendário inline
                minDate: 'today' // Permitir apenas datas a partir de hoje
            });
        });