package test;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

import main.Calculator;

public class CalculatorTest {
    @Test
    public void addTest() {
        final Calculator calculator = new Calculator();

        calculator.setOperand1(3);
        calculator.setOperand2(9);
        final double d = calculator.add();

        assertEquals(12, d, 0.0001);
    }

    @Test
    public void divideTest() {
        final Calculator calculator = new Calculator();

        calculator.setOperand1(1);
        calculator.setOperand2(0);
        final double d = calculator.divide();

        assertEquals(0.0, d, 0.0001);
    }

    @Test
    public void potencia() {
        final Calculator calculator = new Calculator();

        calculator.setOperand1(2);
        calculator.setOperand1(2);
        final double d = calculator.potencia();

        assertEquals(4, d, 0.0001);
    }

    @Test
    public void quadrado() {
        final Calculator calculator = new Calculator();

        calculator.setOperand1(2);
        final double d = calculator.quadrado();

        assertEquals(4, d, 0.0001);
    }

    @Test
    public void raiz() {
        final Calculator calculator = new Calculator();

        calculator.setOperand1(9);
        final double d = calculator.raiz();

        assertEquals(3, d, 0.0001);
    }
}
