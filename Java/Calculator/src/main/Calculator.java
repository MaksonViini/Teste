package main;
import java.lang.Math;

public class Calculator implements IOperationsImpl {
    private double operand1;
    private double operand2;
    private double result;

    public Calculator() {
        this.operand1 = this.operand2 = this.result = Double.MIN_VALUE;
    }

    @Override
    public double add() {
        this.result = this.operand1 + this.operand2;
        return this.result;
    }

    @Override
    public double subt() {
        this.result = this.operand1 - this.operand2;
        return this.result;
    }

    @Override
    public double times() {
        this.result = this.operand1 * this.operand2;
        return this.result;
    }

    @Override
    public double divide() {
        this.result = this.operand1 / this.operand2;
        return this.result;
    }

    public double getOperand1() {
        return operand1;
    }

    public void setOperand1(final double operand1) {
        this.operand1 = operand1;
    }

    public double getOperand2() {
        return operand2;
    }

    public void setOperand2(final double operand2) {
        this.operand2 = operand2;
    }

    @Override
    public void reset() {
        this.result = 0;
    }

    @Override
    public double potencia() {
        this.result = Math.pow(this.operand1, this.operand2);
        return this.result;
    }

    @Override
    public double quadrado() {
        this.result = Math.pow(this.operand1, 2);
        return this.result;
    }

    @Override
    public double raiz() {
        this.result = Math.sqrt(operand1);
        return this.result;
    }
}
