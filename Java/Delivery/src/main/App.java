package main;

import javax.swing.JOptionPane;

/**
 * Classe com o método principal para iniciar a aplicação
 */
public class App {
    public static void main(String[] args) {
        Pedido pedido = new Pedido(1001);
        pedido.adicionaItem(new Item("Marmita", 12.5));
        pedido.adicionaItem(new Item("Coca-cola 2litros", 5.5));
        pedido.adicionaItem(new Item("Pudim de leite", 8));

        int opcaoPagamento = Integer.parseInt(JOptionPane.showInputDialog(null, "1 - Cartao / 2 - Boleto"));

        if (opcaoPagamento == 1) {
            CartaoCredito cartaoCredito = new CartaoCredito();
            cartaoCredito.leitura();
            cartaoCredito.processamento();
            cartaoCredito.emissao(pedido);
        } else if (opcaoPagamento == 2) {
            Boleto boleto = new Boleto();
            boleto.leitura();
            boleto.processamento();
            boleto.processamento();
            boleto.emissao(pedido);
        }
    }
}
