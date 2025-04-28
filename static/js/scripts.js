document.addEventListener('DOMContentLoaded', function() {
    // Auto-cerrar alertas después de 5 segundos
    setTimeout(function() {
        let alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            let bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);
    
    // Activar todos los tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Formatear campos de fecha y hora para mejor UX
    const fechaHoraInputs = document.querySelectorAll('input[type="datetime-local"]');
    fechaHoraInputs.forEach(input => {
        input.addEventListener('focus', function() {
            if (!this.value) {
                // Establecer valor predeterminado al actual + 1 hora, redondeado a la próxima hora
                const now = new Date();
                now.setHours(now.getHours() + 1);
                now.setMinutes(0);
                now.setSeconds(0);
                
                // Formato YYYY-MM-DDTHH:MM requerido para datetime-local
                const year = now.getFullYear();
                const month = String(now.getMonth() + 1).padStart(2, '0');
                const day = String(now.getDate()).padStart(2, '0');
                const hours = String(now.getHours()).padStart(2, '0');
                const minutes = String(now.getMinutes()).padStart(2, '0');
                
                this.value = `${year}-${month}-${day}T${hours}:${minutes}`;
            }
        });
    });
    
    // Mejora para tablas responsivas
    const tables = document.querySelectorAll('.table-responsive');
    if (window.innerWidth < 768) {
        tables.forEach(table => {
            table.classList.add('table-sm');
        });
    }
});