package less1.practice;

import java.time.LocalDate;

public class Product {

    protected String productName;

    protected double productPrice;

    protected LocalDate releaseDate;

    public Product(LocalDate releaseDate, double productPrice, String productName) {
        this.releaseDate = releaseDate;
        this.productPrice = productPrice;
        this.productName = productName;
    }

    public Product( String productName) {
        this.productName = productName;
    }
    public void setProductPrice(double productPrice) {
        this.productPrice = productPrice;
    }

    public String getProductName() {
        return productName;
    }

    public double getProductPrice() {
        return productPrice;
    }

    public LocalDate getReleaseDate() {
        return releaseDate;
    }

    @Override
    public String toString() {
        return "Product{" +

                "productName='" + productName + '\'' +
                ", productPrice=" + productPrice +
                ", releaseDate=" + releaseDate +
                '}';
    }
}
