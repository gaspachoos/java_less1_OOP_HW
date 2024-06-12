package less1.practice.impl;

import less1.practice.Product;

import java.time.LocalDate;

public class BottleOfWater extends Product {

    private float volume;

    private String pack;

    private boolean carbonated;

    public BottleOfWater(String name, double price, LocalDate releaseDate) {

        super(releaseDate, price, name);
        this.carbonated = false;
        this.volume = 1;
        this.pack = Package.PLASTIC.getMaterial();
    }

    public BottleOfWater(String name, double price, LocalDate releaseDate, boolean carbonated, String pack, float volume) {
        super(releaseDate, price, name);
        this.carbonated = carbonated;
        this.volume = volume;
        this.pack = pack;


    }


    public float getVolume() {
        return volume;
    }

    public String getPack() {
        return pack;
    }

    public boolean isCarbonated() {
        return carbonated;
    }

    @Override
    public String toString() {
        return "BottleOfWater{" +
                "productName='" + productName + '\'' +
                ", productPrice=" + productPrice +
                ", releaseDate=" + releaseDate +
                "volume=" + volume +
                ", pack='" + pack + '\'' +
                ", carbonated=" + carbonated +
                '}';
    }
}
