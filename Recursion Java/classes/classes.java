// Example: Classes and Objects in Java
// Let's create a simple class called Car

class Car {
    // Fields (attributes)
    String model;
    String color;
    int year;
    
    // Constructor
    Car(String model, String color, int year) {
        this.model = model;
        this.color = color;
        this.year = year;
    }

    
    // Method (behavior)
    void drive() {
        System.out.println("The " + color + " " + model + " from " + year + " is driving!");
    }
}

public class Main {
    public static void main(String[] args) {
        // Creating objects of Car class
        Car car1 = new Car("Toyota", "Red", 2020);
        Car car2 = new Car("Honda", "Blue", 2018);
        
        // Calling methods on objects
        car1.drive();
        car2.drive();
    }
}
