document.getElementById('fraudForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const get = id => parseFloat(document.getElementById(id).value);

    const data = {
        Time: get('time'),
        V1: get('v1'), V2: get('v2'), V3: get('v3'), V4: get('v4'), V5: get('v5'),
        V6: get('v6'), V7: get('v7'), V8: get('v8'), V9: get('v9'), V10: get('v10'),
        V11: get('v11'), V12: get('v12'), V13: get('v13'), V14: get('v14'), V15: get('v15'),
        V16: get('v16'), V17: get('v17'), V18: get('v18'), V19: get('v19'), V20: get('v20'),
        V21: get('v21'), V22: get('v22'), V23: get('v23'), V24: get('v24'), V25: get('v25'),
        V26: get('v26'), V27: get('v27'), V28: get('v28'),
        Amount: get('amount')
    };

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        });

        const result = await response.json();

        const resultBox = document.getElementById('result');
        resultBox.innerHTML = `
            <strong>Result:</strong> 
            <span style="color: ${result.isFraud ? 'red' : 'green'}">
                ${result.message}
            </span>
        `;
    } catch (error) {
        console.error('Prediction Error:', error);
        document.getElementById('result').textContent = '❌ Failed to check transaction.';
    }
});
