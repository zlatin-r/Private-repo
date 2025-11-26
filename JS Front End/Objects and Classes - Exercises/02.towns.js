function towns(arr) {
    const data = [];
    arr.forEach((item) => {
        let [city, lat, lon] = item.split(' | ');
        lat = Number(lat).toFixed(2);
        lon = Number(lon).toFixed(2);

        data.push({
            town: city,
            latitude: lat,
            longitude: lon
        });
    });
    data.forEach((item) => {
        console.log(item)
    });
}

towns(['Sofia | 42.696552 | 23.32601',
    'Beijing | 39.913818 | 116.363625']);
