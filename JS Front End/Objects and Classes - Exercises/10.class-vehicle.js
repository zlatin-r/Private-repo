class Vehicle {
    constructor(type, model, parts, fuel) {
        this.type = type;
        this.model = model;

        this.parts = {
            engine: parts.engine,
            power: parts.power,
            get quality() {
                return this.engine * this.power;
            }
        };

        this.fuel = fuel;
    }

    drive(fuelLoss) {
        if (fuelLoss < 0) throw new Error("Fuel loss cannot be negative");
        this.fuel -= fuelLoss;
        if (this.fuel < 0) this.fuel = 0;
    }
}