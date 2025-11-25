function meeting(arr) {
    let data = {}

    arr.forEach(element => {
        const [day, name] = element.split(' ');

        if (data.hasOwnProperty(day)) {
            console.log(`Conflict on ${day}!`)
        } else {
            data[day] = name;
            console.log(`Scheduled for ${day}`);
        }
    });
    for (let day in data) {
        console.log(`${day} -> ${data[day]}`);
    }
}

meeting(['Monday Peter',
    'Wednesday Bill',
    'Monday Tim',
    'Friday Tim'])
