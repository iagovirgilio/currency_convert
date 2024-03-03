const form = document.getElementById('currency-form');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const formData = new FormData(this);
    const fromCurrency = formData.get('from');
    const toCurrency = formData.get('to');
    const amount = formData.get('amount');

    try {
        const response = await fetch(`/api/convert/?from=${fromCurrency}&to=${toCurrency}&amount=${amount}`);
        const data = await response.json();

        if (response.ok) {
            resultDiv.textContent = `Resultado: ${data.converted_amount}`;
        } else {
            resultDiv.textContent = data.error || 'Erro ao converter moeda.';
        }
    } catch (error) {
        console.error('Erro:', error);
        resultDiv.textContent = 'Erro ao processar a solicitação.';
    }
});
