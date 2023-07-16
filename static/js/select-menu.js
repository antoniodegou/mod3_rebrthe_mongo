document.addEventListener('DOMContentLoaded', function() {
    var categorySelect = document.getElementById('categorySelect');
    var exerciseItems = document.querySelectorAll('.accordion .col-12');

    categorySelect.addEventListener('change', function() {
        var selectedCategory = categorySelect.value;

        exerciseItems.forEach(function(item) {
            if (selectedCategory === 'all' || item.getAttribute('data-category') === selectedCategory) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    });
});