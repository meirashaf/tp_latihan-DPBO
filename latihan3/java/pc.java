public class pc {
    // atribut serta nama objek
    private processor pObj;   
    private disk dObj;   
    private ram rObj;
    private int totalPrice;

    // constructor
    public pc() {
    }

    public pc(processor pObj, disk dObj, ram rObj) {
        this.pObj = pObj;
        this.dObj = dObj;
        this.rObj = rObj;
        this.totalPrice = pObj.getPrice() + dObj.getPrice() + rObj.getPrice();
    }

    // setter dan getter
    public processor getpObj() {
        return pObj;
    }

    public void setpObj(processor pObj) {
        this.pObj = pObj;
    }

    public disk getdObj() {
        return dObj;
    }

    public void setdObj(disk dObj) {
        this.dObj = dObj;
    }

    public ram getrObj() {
        return rObj;
    }

    public void setrObj(ram rObj) {
        this.rObj = rObj;
    }

    public int getTotalPrice() {
        return totalPrice;
    }

    public void setTotalPrice(int totalPrice) {
        this.totalPrice = totalPrice;
    }   

    // untuk menampilkan output
    public void print(){
        System.out.println("\nProcessor");
        System.out.println("Nama : " + pObj.getName());
        System.out.println("Harga : " + pObj.getPrice());
        
        System.out.println("\nDisk");
        System.out.println("Type : " + dObj.getType());
        System.out.println("Kapasitas : " + dObj.getCapacity());
        System.out.println("Harga : " + dObj.getPrice());

        System.out.println("\nRAM");
        System.out.println("Kapasitas : " + rObj.getCapacity());
        System.out.println("Harga : " + rObj.getPrice());

    }
    
    
}
