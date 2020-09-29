package main;

import javax.swing.*;

public class App {
    public static void main(String[] args) {
        Calculator calculator = new Calculator();

        String s = JOptionPane.showInputDialog("Operando 1");
        calculator.setOperand1(Double.parseDouble(s));

        //s = JOptionPane.showInputDialog("Operando 2");
       // calculator.setOperand2(Double.parseDouble(s));

        JOptionPane.showMessageDialog(null, "Resultado: " + calculator.raiz());
    }
}
