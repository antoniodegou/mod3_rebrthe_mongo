document.addEventListener('DOMContentLoaded', function() {
    let categorySelect = document.getElementById('categorySelect');
    let exerciseItems = document.querySelectorAll('.accordion .col-12');

    categorySelect.addEventListener('change', function() {
        let selectedCategory = categorySelect.value;

        exerciseItems.forEach(function(item) {
            if (selectedCategory === 'all' || item.getAttribute('data-category') === selectedCategory) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    });
});