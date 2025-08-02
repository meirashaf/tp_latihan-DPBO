public class ram {
    // atribut
    private int capacity;   
    private int price;

    // constructor
    ram(){}

    public ram(int capacity, int price) {
        this.capacity = capacity;
        this.price = price;
    }

    // setter dan getter
    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    
}
