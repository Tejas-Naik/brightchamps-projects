// Example: Array Operations - Search Techniques in Java
// Simple examples of different search methods

public class ArrayOperations {
    public static void main(String[] args) {
        System.out.println("===== SEARCHING IN ARRAYS =====");
        
        // Create an array of numbers
        int[] numbers = {5, 12, 8, 42, 17, 23, 9, 31, 16, 4};
        printArray("Original array", numbers);
        
        // LINEAR SEARCH EXAMPLE
        System.out.println("\n===== LINEAR SEARCH =====");
        int searchValue = 17;
        int linearResult = linearSearch(numbers, searchValue);
        if (linearResult != -1) {
            System.out.println("Found " + searchValue + " at position " + linearResult + " using Linear Search!");
        } else {
            System.out.println(searchValue + " was not found in the array.");
        }
        
        // Try searching for a value that doesn't exist
        searchValue = 99;
        linearResult = linearSearch(numbers, searchValue);
        if (linearResult != -1) {
            System.out.println("Found " + searchValue + " at position " + linearResult + " using Linear Search!");
        } else {
            System.out.println(searchValue + " was not found in the array.");
        }
        
        // BINARY SEARCH EXAMPLE
        System.out.println("\n===== BINARY SEARCH =====");
        System.out.println("Binary search requires a sorted array!");
        
        // Sort the array first (using built-in sort)
        int[] sortedNumbers = {4, 5, 8, 9, 12, 16, 17, 23, 31, 42};
        printArray("Sorted array", sortedNumbers);
        
        searchValue = 23;
        int binaryResult = binarySearch(sortedNumbers, searchValue);
        if (binaryResult != -1) {
            System.out.println("Found " + searchValue + " at position " + binaryResult + " using Binary Search!");
        } else {
            System.out.println(searchValue + " was not found in the array.");
        }
        
        // Try searching for a value that doesn't exist
        searchValue = 99;
        binaryResult = binarySearch(sortedNumbers, searchValue);
        if (binaryResult != -1) {
            System.out.println("Found " + searchValue + " at position " + binaryResult + " using Binary Search!");
        } else {
            System.out.println(searchValue + " was not found in the array.");
        }
        
        // SEARCHING STRINGS EXAMPLE
        System.out.println("\n===== SEARCHING FOR STRINGS =====");
        String[] fruits = {"Apple", "Banana", "Orange", "Grape", "Mango", "Pineapple", "Strawberry"};
        printArray("Fruit array", fruits);
        
        String fruitToFind = "Mango";
        int fruitPosition = linearSearchString(fruits, fruitToFind);
        if (fruitPosition != -1) {
            System.out.println("Found " + fruitToFind + " at position " + fruitPosition + "!");
        } else {
            System.out.println(fruitToFind + " was not found in the array.");
        }
        
        // SEARCH APPLICATION: FINDING STUDENTS BY ID
        System.out.println("\n===== SEARCH APPLICATION: FIND STUDENT =====");
        int[] studentIds = {101, 102, 105, 109, 113, 118, 121};
        String[] studentNames = {"Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"};
        
        printStudents(studentIds, studentNames);
        
        int studentIdToFind = 113;
        int studentPosition = linearSearch(studentIds, studentIdToFind);
        if (studentPosition != -1) {
            System.out.println("Student with ID " + studentIdToFind + " is " + 
                               studentNames[studentPosition] + ".");
        } else {
            System.out.println("No student found with ID " + studentIdToFind + ".");
        }
    }
    
    // LINEAR SEARCH
    // This method searches through each element one by one
    public static int linearSearch(int[] array, int valueToFind) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == valueToFind) {
                return i; // Found it! Return the position
            }
        }
        return -1; // Not found
    }
    
    // BINARY SEARCH
    // This method is more efficient but requires a sorted array
    public static int binarySearch(int[] array, int valueToFind) {
        int left = 0;
        int right = array.length - 1;
        
        while (left <= right) {
            int middle = (left + right) / 2;
            
            // Check if value is at the middle
            if (array[middle] == valueToFind) {
                return middle; // Found it!
            }
            
            // If value is greater, ignore left half
            if (array[middle] < valueToFind) {
                left = middle + 1;
            } 
            // If value is smaller, ignore right half
            else {
                right = middle - 1;
            }
        }
        
        return -1; // Not found
    }
    
    // LINEAR SEARCH FOR STRINGS
    public static int linearSearchString(String[] array, String valueToFind) {
        for (int i = 0; i < array.length; i++) {
            if (array[i].equals(valueToFind)) {
                return i; // Found it! Return the position
            }
        }
        return -1; // Not found
    }
    
    // HELPER METHODS
    public static void printArray(String label, int[] array) {
        System.out.print(label + ": [");
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i]);
            if (i < array.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
    
    public static void printArray(String label, String[] array) {
        System.out.print(label + ": [");
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i]);
            if (i < array.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
    
    public static void printStudents(int[] ids, String[] names) {
        System.out.println("Student List:");
        for (int i = 0; i < ids.length; i++) {
            System.out.println("  ID: " + ids[i] + ", Name: " + names[i]);
        }
    }
}
