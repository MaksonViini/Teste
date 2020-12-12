package main;

import java.util.ArrayList;
import java.util.List;

import javax.swing.JOptionPane;

/**
 * Classe Pedido
 */
public class Pedido {
    // ID numérico para identificação de um pedido
    private int numero;
    // Lista de itens de um pedido
    private List<Item> itens;

    private String cidade;
    private String rua;
    private String bairro;
    private int numeroCasa;

    /**
     * Método construtor da classe
     * 
     * @param numero Número do pedido
     */
    public Pedido(int numero) {
        this.numero = numero;
        this.itens = new ArrayList<>();
    }

    
    /** 
     * @return String
     */
    public String getCidade() {
        return cidade;
    }

    
    /** 
     * @param cidade
     */
    public void setCidade(String cidade) {
        this.cidade = cidade;
    }

    /**
     * Método para retornar o número do pedido
     * 
     * @return Número de identificação do pedido
     */
    public int getNumero() {
        return this.numero;
    }

    /**
     * Método para adicionar um item em um pedido
     * 
     * @param item Item de um pedido
     */
    public void adicionaItem(Item item) {
        this.itens.add(item);
    }

    /**
     * Método para remover um item do pedido
     * 
     * @param posicao Posição do item no pedido
     */
    public void removeItem(int posicao) {
        this.itens.remove(posicao);
    }

    /**
     * Método para coletar dados de endereco para efetuar entrega
     */
    public void realizarEntrega () {
        System.out.println();
        this.setCidade(JOptionPane.showInputDialog(null, "Informe a sua cidade"));
        this.rua = JOptionPane.showInputDialog(null, "Informe a rua");
        this.bairro = JOptionPane.showInputDialog(null, "Informe o bairro");
        this.numeroCasa = Integer.parseInt(JOptionPane.showInputDialog(null, "Número da casa"));

    }

    /**
     * Método para imprimir a local de entrega
     */
    public void imprimeEntrega () {
        System.out.println("Local entrega...");
        System.out.println("Rua..: " + this.rua);
        System.out.println ("Bairro..: " + this.bairro);
        System.out.println ("Número da casa..: " + this.numeroCasa);

    }

    /**
     * Método para imprimir a lista de itens do pedido
     */
    public void imprime() {
        int numItem = 1;
        System.out.println ("Pedido Número: " + this.numero);
        for (Item item : itens) {
            System.out.print("Item #" + numItem + ":");
            System.out.println (item.getDescricao() + "\t R$ " + item.getPreco());
        }
        System.out.println();
    }

    /**
     * Método para retornar a lista de itens do pedido
     * @return Lista de itens
     */
    public List<Item> getItens() {
        return this.itens;
    }

    
    /** 
     * @return String
     */
    public String getRua() {
        return rua;
    }

    
    /** 
     * @param rua
     */
    public void setRua(String rua) {
        this.rua = rua;
    }

    
    /** 
     * @return String
     */
    public String getBairro() {
        return bairro;
    }

    
    /** 
     * @param bairro
     */
    public void setBairro(String bairro) {
        this.bairro = bairro;
    }

    
    /** 
     * @return int
     */
    public int getNumeroCasa() {
        return numeroCasa;
    }

    
    /** 
     * @param numeroCasa
     */
    public void setNumeroCasa(int numeroCasa) {
        this.numeroCasa = numeroCasa;
    }
}
