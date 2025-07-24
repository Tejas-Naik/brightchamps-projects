// Example: Arrays in Java
// Simple examples of different types of arrays

public class ArrayExamples {
    public static void main(String[] args) {
        System.out.println("===== FRUIT BASKET =====");
        // 1. Creating and using a simple array of strings
        String[] fruitBasket = {"Apple", "Banana", "Orange", "Grapes", "Strawberry"};
        
        // Printing all fruits using a loop
        System.out.println("Fruits in my basket:");
        for (int i = 0; i < fruitBasket.length; i++) {
            System.out.println((i+1) + ". " + fruitBasket[i]);
        }
        
        // Accessing specific elements
        System.out.println("\nMy favorite fruit is: " + fruitBasket[0]);
        System.out.println("The last fruit is: " + fruitBasket[4]);
        
        System.out.println("\n===== STUDENT SCORES =====");
        // 2. Creating and using an array of integers
        int[] studentScores = new int[5]; // Creating an empty array with 5 spaces
        
        // Adding values to the array
        studentScores[0] = 95;
        studentScores[1] = 85;
        studentScores[2] = 90;
        studentScores[3] = 100;
        studentScores[4] = 88;
        
        // Calculating the average score
        int sum = 0;
        for (int i = 0; i < studentScores.length; i++) {
            sum += studentScores[i];
            System.out.println("Student " + (i+1) + " score: " + studentScores[i]);
        }
        
        double average = (double) sum / studentScores.length;
        System.out.println("Average score: " + average);
        
        System.out.println("\n===== TEMPERATURE CHART =====");
        // 3. Creating and using a 2D array (week temperatures)
        int[][] weekTemperatures = {
            {32, 30, 31, 35, 29, 33, 32}, // Week 1 temperatures
            {28, 29, 30, 31, 32, 31, 30}  // Week 2 temperatures
        };
        
        String[] days = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"};
        
        // Displaying the temperature chart
        System.out.println("       " + days[0] + "  " + days[1] + "  " + days[2] + "  " + days[3] + "  " + days[4] + "  " + days[5] + "  " + days[6]);
        System.out.println("Week 1: " + weekTemperatures[0][0] + "°C " + weekTemperatures[0][1] + "°C " + 
                           weekTemperatures[0][2] + "°C " + weekTemperatures[0][3] + "°C " + 
                           weekTemperatures[0][4] + "°C " + weekTemperatures[0][5] + "°C " + 
                           weekTemperatures[0][6] + "°C");
        System.out.println("Week 2: " + weekTemperatures[1][0] + "°C " + weekTemperatures[1][1] + "°C " + 
                           weekTemperatures[1][2] + "°C " + weekTemperatures[1][3] + "°C " + 
                           weekTemperatures[1][4] + "°C " + weekTemperatures[1][5] + "°C " + 
                           weekTemperatures[1][6] + "°C");
        
        // Finding the hottest day
        int maxTemp = 0;
        int maxWeek = 0;
        int maxDay = 0;
        
        for (int week = 0; week < weekTemperatures.length; week++) {
            for (int day = 0; day < weekTemperatures[week].length; day++) {
                if (weekTemperatures[week][day] > maxTemp) {
                    maxTemp = weekTemperatures[week][day];
                    maxWeek = week + 1;
                    maxDay = day;
                }
            }
        }
        
        System.out.println("\nThe hottest day was: " + days[maxDay] + " of Week " + maxWeek + 
                           " with temperature: " + maxTemp + "°C");
    }
}
