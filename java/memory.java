class memory extends hardware {
    // atribut
    private int frequency;
    private int memorySize;
    private String supportsCuda;

    // constructor kosong
    memory(){}

    // Setter dan Getter

    public int getFrequency() {
        return frequency;
    }
    public void setFrequency(int frequency) {
        this.frequency = frequency;
    }
    public int getMemorySize() {
        return memorySize;
    }
    public void setMemorySize(int memorySize) {
        this.memorySize = memorySize;
    }
    public String getSupportsCuda() {
        return supportsCuda;
    }
    public void setSupportsCuda(String supportsCuda) {
        this.supportsCuda = supportsCuda;
    }

}