function addItem() {
    const container = document.getElementById('itemsContainer');
    const newItem = document.createElement('div');
    newItem.className = 'itemRow';
    newItem.innerHTML = `
        <input type="text" name="item" placeholder="Item Name" required>
        <input type="number" name="quantity" placeholder="Quantity" class="quantity" required>
        <input type="number" name="price" placeholder="Price per Item" class="price" required>
        <button type="button" onclick="removeItem(this)">Remove</button>
    `;
    container.appendChild(newItem);
    attachListeners(); // Attach listeners to new inputs
}

// Remove an item row
function removeItem(button) {
    button.parentElement.remove();
    updateTotal();
}

// Calculate total in real-time
function updateTotal() {
    const quantities = document.querySelectorAll('.quantity');
    const prices = document.querySelectorAll('.price');
    let total = 0;

    for (let i = 0; i < quantities.length; i++) {
        const qty = parseFloat(quantities[i].value) || 0;
        const price = parseFloat(prices[i].value) || 0;
        total += qty * price;
    }

    document.getElementById('grandTotal').textContent = total.toFixed(2);
}

// Attach input listeners for real-time calculation
function attachListeners() {
    const quantities = document.querySelectorAll('.quantity');
    const prices = document.querySelectorAll('.price');

    quantities.forEach(input => input.addEventListener('input', updateTotal));
    prices.forEach(input => input.addEventListener('input', updateTotal));
}

// Initial listeners
attachListeners();
updateTotal();