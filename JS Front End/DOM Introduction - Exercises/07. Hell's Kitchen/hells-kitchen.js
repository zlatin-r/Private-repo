function solve() {
    const inputData = JSON.parse(document.querySelector("#inputs textarea").value);

    const restaurants = {};
    const outputRestaurantDataElement = document.querySelector("#bestRestaurant p");
    const outputEmployeesDataElement = document.querySelector("#workers p");

    inputData.forEach(entry => {
        let [name, workers] = entry.split(" - ");
        let workerList = workers.split(", ");

        if (!restaurants[name]) {
            restaurants[name] = {employees: {}, avgSalary: 0, bestSalary: 0};
        }

        workerList.forEach(person => {
            let [workerName, salary] = person.split(" ");
            salary = Number(salary);

            restaurants[name].employees[workerName] = salary;
        });

        let allSalaries = Object.values(restaurants[name].employees);
        let total = allSalaries.reduce((a, b) => a + b, 0);

        restaurants[name].avgSalary = total / allSalaries.length;
        restaurants[name].bestSalary = Math.max(...allSalaries);
    });

    let best = Object.entries(restaurants)
        .sort((a, b) => b[1].avgSalary - a[1].avgSalary)[0];

    let [bestName, bestData] = best;

    let sortedWorkers = Object.entries(bestData.employees)
        .sort((a, b) => b[1] - a[1]);

    outputRestaurantDataElement.textContent =
        `Name: ${bestName} ` +
        `Average Salary: ${bestData.avgSalary.toFixed(2)} ` +
        `Best Salary: ${bestData.bestSalary.toFixed(2)}`;

    outputEmployeesDataElement.textContent = sortedWorkers
        .map(([name, salary]) => `Name: ${name} With Salary: ${salary}`)
        .join(" ");
}
