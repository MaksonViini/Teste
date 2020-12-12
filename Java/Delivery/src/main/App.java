package main;

import javax.swing.JOptionPane;

/**
 * Classe com o método principal para iniciar a aplicação
 */
public class App {
    
    /** 
     * @param args
     */
    public static void main(String[] args) {
        Cardapio cardapio = new Cardapio();
        cardapio.listAll();
        
        Pedido pedido = new Pedido(1001);
        pedido.adicionaItem(new Item("Marmita", 12.5));
        pedido.adicionaItem(new Item("Coca-cola 2litros", 5.5));
        pedido.adicionaItem(new Item("Pudim de leite", 8));
        pedido.removeItem(2);

        int opcaoPagamento = Integer.parseInt(JOptionPane.showInputDialog(null, "1 - Credito / 2 - Boleto / 3 - Debito"));

        if (opcaoPagamento == 1) {
            CartaoCredito cartaoCredito = new CartaoCredito();
            cartaoCredito.leitura();
            cartaoCredito.processamento();
            cartaoCredito.emissao(pedido);
            pedido.realizarEntrega();
            pedido.imprimeEntrega();

        } else if (opcaoPagamento == 2) {
            Boleto boleto = new Boleto();

            boleto.leitura();
            boleto.processamento();
            boleto.processamento();
            boleto.emissao(pedido);
            pedido.realizarEntrega();
            pedido.imprimeEntrega();
        } else if (opcaoPagamento == 3) {
            CartaoDebito cartaoDebito = new CartaoDebito();

            cartaoDebito.leitura();
            cartaoDebito.processamento();
            cartaoDebito.emissao(pedido);
            pedido.realizarEntrega();
            pedido.imprimeEntrega();
        }
    }
}
