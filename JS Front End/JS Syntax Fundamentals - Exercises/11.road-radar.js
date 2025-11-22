function solve(speed, zone) {
    let limit = 0;

    switch (zone) {
        case "motorway":     limit = 130; break;
        case "interstate":   limit = 90; break;
        case "city":         limit = 50; break;
        case "residential":  limit = 20; break;
    }

    const diff = speed - limit;

    if (diff <= 0) {
        console.log(`Driving ${speed} km/h in a ${limit} zone`);
        return;
    }

    let status = "";

    if (diff <= 20) {
        status = "speeding";
    } else if (diff <= 40) {
        status = "excessive speeding";
    } else {
        status = "reckless driving";
    }

    console.log(`The speed is ${diff} km/h faster than the allowed speed of ${limit} - ${status}`);
}

solve(40, "city");
solve(21, "residential");
solve(120, "interstate");
solve(200, "motorway");
