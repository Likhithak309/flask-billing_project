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
    attachListeners();
    updateTotal();
}

function removeItem(button) {
    button.parentElement.remove();
    updateTotal();
}

function updateTotal() {
    const quantities = document.querySelectorAll('.quantity');
    const prices = document.querySelectorAll('.price');
    const taxInput = document.querySelector('input[name="tax"]');
    const discountInput = document.querySelector('input[name="discount"]');

    let subtotal = 0;
    for (let i = 0; i < quantities.length; i++) {
        const qty = parseFloat(quantities[i].value) || 0;
        const price = parseFloat(prices[i].value) || 0;
        subtotal += qty * price;
    }

    const tax = parseFloat(taxInput.value) || 0;
    const discount = parseFloat(discountInput.value) || 0;
    const grandTotal = subtotal + (subtotal * tax / 100) - discount;

    document.getElementById('grandTotal').textContent = grandTotal.toFixed(2);
}

function attachListeners() {
    const quantities = document.querySelectorAll('.quantity');
    const prices = document.querySelectorAll('.price');
    const taxInput = document.querySelector('input[name="tax"]');
    const discountInput = document.querySelector('input[name="discount"]');

    quantities.forEach(input => input.addEventListener('input', updateTotal));
    prices.forEach(input => input.addEventListener('input', updateTotal));
    taxInput.addEventListener('input', updateTotal);
    discountInput.addEventListener('input', updateTotal);
}

attachListeners();
updateTotal();