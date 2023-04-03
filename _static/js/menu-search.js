/* Left menu - Search */

document.addEventListener("DOMContentLoaded", () => {
    let search_input = '<form id="search" action="https://duckduckgo.com/"><input id="search-input" type="search" placeholder="Search..." name="q" onfocusout="onFormSubmit(); this.form"><input id="search-submit" type="submit" value="" onclick="onFormSubmit();"></form>'
    document.querySelectorAll('div[role="search"]')[0].innerHTML = search_input;

});

function onFormSubmit() {
    let query = document.getElementById("search-input");
    if (query.value) {
        query.value += ' site:python3.info';
        document.getElementById("search").submit();
        return true;
    }
}
