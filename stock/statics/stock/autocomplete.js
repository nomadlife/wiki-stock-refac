$(function autocomplete(endpoint) {
  const companies = [];
console.log('endpoint:',endpoint);

  $.ajax({
    type: "GET",
    url: endpoint,
    success: function (data) {
      console.log("success")
      companies.push(...data)

    },
    error: function (error_data) {
      console.log("error")
      console.log('url:', url)
      console.log(error_data)
    }
  });

  function findMatches(wordToMatch, companies) {
    return companies.filter(place => {
      // here we need to figure out if the city on state matches what was searched
      const regex = new RegExp(wordToMatch, 'gi'); 
      return place.name.match(regex) || place.ticker.match(regex)
    });
  }

  function displayMatches() {
    // console.log('this.value:',this.value);
    if(this.value == ''){
      // console.log('valu is empty');
      suggestions.innerHTML = ''
    }else{

      const matchArray = findMatches(this.value, companies).slice(0, 10);
      
      const html = matchArray.map(place => {
        const regex = new RegExp(this.value, 'gi');
        const companyName = place.name.replace(regex, `<span class ="">${this.value.toUpperCase()}</span>`);
        const tickerNumber = place.ticker.replace(regex, `<span class ="">${this.value}</span>`);
        
        return `
            <li><a class="btn btn-block text-left" href="{% url 'stock-detail' ticker_id=12345 %}">
              <span class="name"> ${companyName}, ${tickerNumber}</span>
              </a>
            </li>`.replace(/12345/, place.id.toString());
      }).join('');
      suggestions.innerHTML = html;
    }
  }

  const searchInput = document.querySelector('.search');
  const suggestions = document.querySelector('.suggestions');

  searchInput.addEventListener('change', displayMatches);
  searchInput.addEventListener('keyup', displayMatches);

});