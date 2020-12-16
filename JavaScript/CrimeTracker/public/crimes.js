const api = 'https://data.princegeorgescountymd.gov/resource/wb4e-w4nf.json';

const restArray = [];

fetch(api)
    .then(blob => blob.json())
    .then(data => restArray.push(...data));



function findMatches(wordToMatch, restArray) {
    return restArray.filter(place => {
        const regex = new RegExp(wordToMatch, 'gi');
        if (place.clearance_code_inc_type.includes('')) {
            return place.clearance_code_inc_type.match(regex) || place.date.match(regex)
        }
    });
}
const searchInput = document.querySelector('.UserInput');
const suggestions = document.querySelector('.suggestions')


function displayMatches() {
    const matchArray = findMatches(this.value, restArray);
    const html = matchArray.map(place => {
        if (this.value != '') {
            return `
            <li class="filteredDisplay">
                <ul>
                    <li>
                        ${place.clearance_code_inc_type}
                    </li>
                    <li>
                        ${place.date}
                    </li>
                    <address>
                        ${place.street_number} ${place.street_address}<br>
                    </address>
                    <br>
                </ul>
            </li>
            `;
        }
    }).join('');
    
    searchInput.innerHTML = html;
    suggestions.innerHTML = html;
}

searchInput.addEventListener('keyup', displayMatches);