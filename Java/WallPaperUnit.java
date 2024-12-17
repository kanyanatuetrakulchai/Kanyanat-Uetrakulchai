public class WallPaperUnit {
    public String name;
    public double length;

    // Constructor to initialize the House object
    public WallPaperUnit(String name, double length) {
        this.name = name;
        this.length = length;
    }

    // Getter for address
    public String getName() {
        return name;
    }

    // Setter for address
    public void setName(String name) {
        this.name = name;
    }

    // Getter for number of rooms
    public double getLength() {
        return length;
    }

    // Setter for number of rooms
    public void setLength(double length) {
        this.length = length;
    }

    // Method to display house details
    public void displayDetails() {
        System.out.println("Name: " + name);
        System.out.println("Length: " + length);
    }

    // Main method for demonstration
    public static void main(String[] args) {
        WallPaperUnit myWallPaperUnit = new WallPaperUnit("Pudding", 6);
        myWallPaperUnit.displayDetails();
    }
}