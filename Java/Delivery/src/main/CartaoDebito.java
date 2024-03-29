package main;

import javax.swing.JOptionPane;

/**
 * Classe para tipo de pagamento Cartão de Debito
 * @hidden https://www.4devs.com.br/gerador_de_numero_cartao_credito
 */
public class CartaoDebito implements IPagamentoImpl {

    private String numeroCartao;
    private int mesValido;
    private int anoValido;
    private int codigoSeguranca;

    /**
     * Método construtor para a classe Cartão de Debito
     */
    public CartaoDebito() {
        this.numeroCartao = "";
        this.mesValido = this.anoValido = this.codigoSeguranca = 0;
    }


    /**
     * Método para leitura do Cartão de Debito
     */
    @Override
    public void leitura() {
        this.numeroCartao = JOptionPane.showInputDialog(null, "Digite o número do cartao");
        do {
            this.mesValido = Integer.parseInt(JOptionPane.showInputDialog(null, "Mês de validade do cartão"));
        } while (this.mesValido < 1 || this.mesValido > 12);

        do {
            this.anoValido = Integer.parseInt(JOptionPane.showInputDialog(null, "Ano de validade do cartão"));
        } while (this.anoValido < 1990);

        do {
            this.codigoSeguranca = Integer.parseInt(JOptionPane.showInputDialog(null, "Código de segurança"));
        } while (this.codigoSeguranca <= 99 || this.codigoSeguranca > 999);

    }

    /**
     * Método para processamento do Cartão de Debito
     */
    @Override
    public void processamento() {
        System.out.println ("Processando o pagamento...");
        System.out.println ("Número do cartão..: " + this.numeroCartao);
        System.out.println ("Validade do cartão: " + this.mesValido + "/" + this.anoValido);
        System.out.println ("Número do cartão..: " + this.codigoSeguranca);
    }

    /**
     * Método para emissao do Cartão de Debito
     * @param pedido
     */
    @Override
    public void emissao(Pedido pedido) {
        double totalPedido = 0;

        System.out.println ("Pedido No.: " + pedido.getNumero());
        for (Item item : pedido.getItens()) 
            totalPedido += item.getPreco();

        System.out.println ("Total.....: R$ " + totalPedido);

        System.out.println ("Cartão de debito APROVADO!");
    }
    
}
