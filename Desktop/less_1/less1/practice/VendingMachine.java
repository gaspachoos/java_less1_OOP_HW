package less1.practice;

import java.util.ArrayList;
import java.util.List;

public class VendingMachine {

    private List<Product> products;

    public VendingMachine() {
        this.products = new ArrayList<>();
    }

    public VendingMachine(List<Product> products) {
        this.products = products;
    }

    public void addProducts(List<Product> products) {
        this.products.addAll(products);
    }

    public Product getProduct(String productName) {
        for (Product product : products) {
            if (product.getProductName().equals(productName)) {
                products.remove(product);
                return product;
            }
        }

        System.out.println("No such product: " + productName);
        return null;
    }

    public List<Product> getProducts() {
        return products;

    }

}