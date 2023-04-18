$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  // variable for each movie
  const list = data.results;
  // iterate through each movie
  for (let i = 0; i < list.length; i++) {
    $('UL#list_movies').append('<li>' + list[i].title + '</li>');
  }
});
