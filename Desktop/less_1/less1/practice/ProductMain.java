package less1.practice;

import less1.practice.impl.*;
import less1.practice.impl.Package;

import java.util.List;

import java.time.LocalDate;

public class ProductMain {

    public static void main(String[] args) {
        Product bottle1 = new BottleOfWater("Родники", 55, LocalDate.of(2024, 5, 1));
        Product bottle2 = new BottleOfWater("Родники Газированная", 55, LocalDate.of(2024, 5, 1),
                true, Package.GLASS.getMaterial(),0.5F);

        VendingMachine vm = new WaterVendingMachine();

        System.out.println(vm.getProducts());

        vm.addProducts(List.of(bottle1, bottle2,bottle1, bottle2,bottle1, bottle2,bottle1, bottle2));

        System.out.println(vm.getProducts());
        vm.getProduct("Родники Газированная");

        System.out.println(vm.getProducts());


        Product tea = new HotDrink("Green Dragon",750,58);

        Product coffee = new HotDrink("Pele",750,58);

        VendingMachine hvm = new HotDrinkVendingMachine();

        System.out.println(hvm.getProducts());

        hvm.addProducts(List.of(tea, coffee,tea, coffee,tea, coffee,tea, coffee,tea, coffee,tea, coffee));
        System.out.println(hvm.getProducts());

        hvm.getProduct("Pele");

        System.out.println(hvm.getProducts());


    }
}
