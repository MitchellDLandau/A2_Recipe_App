const showSearch = document.querySelector('.show-search');
const searchForm = document.querySelector('.form');
const hideSearch = document.querySelector('.hide-search');
const submit = document.querySelector('.submit');

const isSearchFormVisible = localStorage.getItem('searchFormVisible') === 'true';

function toggleSearchForm() {
    if (isSearchFormVisible) {
        searchForm.style.display = "block";
        showSearch.style.display = "none";
        hideSearch.style.display = "block";
    } else {
        searchForm.style.display = "none";
        showSearch.style.display = "block";
        hideSearch.style.display = "none";
    }
}

toggleSearchForm();

showSearch.addEventListener('click', () => {
    searchForm.style.display = "block"
    showSearch.style.display = "none"
    hideSearch.style.display = "block"
    localStorage.setItem('searchFormVisible', 'true');
});

hideSearch.addEventListener('click', () => {
    searchForm.style.display = "none"
    showSearch.style.display = "block"
    hideSearch.style.display = "none"
    localStorage.setItem('searchFormVisible', 'false');
});

