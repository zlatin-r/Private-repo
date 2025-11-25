function cats(arr) {
    let cats = [];

    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }

        speak() {
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    }

    arr.forEach((item) => {
        let [name, age] = item.split(' ');
        cats.push(new Cat(name, age));
    });

    for (let cat of cats) {
        cat.speak();
    }
}

