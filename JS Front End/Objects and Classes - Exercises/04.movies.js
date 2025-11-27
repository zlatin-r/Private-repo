function movies(arr) {
    let movies = [];

    for (let info of arr) {
        if (info.includes("addMovie")) {
            let movieName = info.replace("addMovie ", "");
            movies.push({name: movieName});
        } else if (info.includes("directedBy")) {
            let [movieName, director] = info.split(" directedBy ");
            let movie = movies.find(movie => movie.name === movieName);
            if (movie) {
                movie.director = director;
            }
        } else if (info.includes("onDate")) {
            let [movieName, date] = info.split(" onDate ");
            let movie = movies.find(movie => movie.name === movieName);
            if (movie) {
                movie.date = date;
            }
        }
    }
    movies
        .filter(movie => movie.name && movie.director && movie.date)
        .forEach(movie => console.log(JSON.stringify(movie)));
}

movies([
    'addMovie Fast and Furious',
    'addMovie Godfather',
    'Inception directedBy Christopher Nolan',
    'Godfather directedBy Francis Ford Coppola',
    'Godfather onDate 29.07.2018',
    'Fast and Furious onDate 30.07.2018',
    'Batman onDate 01.08.2018',
    'Fast and Furious directedBy Rob Cohen'
])