public class disk {
    // atribut
    private String type;
    private int capacity;  
    private int price;
    
    // constructor
    disk(){}

    disk(String type, int capacity, int price){
        this.type = type;
        this.capacity = capacity;
        this.price = price;
    }

    // setter dan getter

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

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
