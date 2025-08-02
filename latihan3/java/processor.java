public class processor {
    // atribut
    private int price;
    private String name;

    // constructor
    processor(){}

    processor(int price, String name){
        this.price = price;
        this.name = name;
    }

    // setter dan getter

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    
    
}
