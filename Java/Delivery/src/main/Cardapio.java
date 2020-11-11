package main;

import java.util.ArrayList;
import java.util.List;

/**
 * Cardápio de itens 
 */
public class Cardapio {
    private List<Item> itens; 

    public Cardapio() {
        itens = new ArrayList<>();
        itens.add(new Item("Cerveja Heineken Premium Long Neck 330ml", 4.98));
        itens.add(new Item("Cerveja Eisenbahn Premium Long Neck", 3.99));
        itens.add(new Item("Coca-cola Sabor original 2 litros", 7.89));
        itens.add(new Item("Água mineral Crystal sem gás 300ml", 1.15));
        itens.add(new Item("Sanduíche Hot Pocket X Burguer Sadia", 3.99));
        itens.add(new Item("Macarrão instantâneo Nissin Miojo Carne 85g", 1.49));
    }

    /**
     * List many itens 
     */
    public void listAll() {
        System.out.println ("Cardápio");
        for (int i = 0; i < itens.size(); i++)
            System.out.println (i + "\t: " + 
                itens.get(i).getDescricao() + "\t - R$ " + 
                itens.get(i).getPreco());
    }

    /**
     * Returns a item
     * @param index Position of list
     * @return new item
     */
    public Item getItem (int index) {
        return new Item (itens.get(index).getDescricao(),
                         itens.get(index).getPreco());
    }
}
