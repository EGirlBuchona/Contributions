// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022

// Gráfico de Barras
const ctxBarras = document.getElementById('graficoBarras').getContext('2d');
const graficoBarras = new Chart(ctxBarras, {
    type: 'bar',
    data: {
        labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
        datasets: [{
            label: 'Ventas Mensuales',
            data: [12, 19, 3, 5, 2],
            backgroundColor: 'rgba(54, 162, 235, 0.5)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// Gráfico de Líneas
const ctxLineas = document.getElementById('graficoLineas').getContext('2d');
const graficoLineas = new Chart(ctxLineas, {
    type: 'line',
    data: {
        labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
        datasets: [{
            label: 'Ingresos Mensuales',
            data: [15, 10, 5, 8, 20],
            backgroundColor: 'rgba(255, 99, 132, 0.5)',
            borderColor: 'rgba(255, 99, 132, 1)',
            fill: true
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
