public class Assalariado extends Colaborador {
    private double valorSalarioFixo;

    public Assalariado (String nome, int HorasTrabalhadas, double valorSalarioFixo) {
        super(nome, HorasTrabalhadas);
        this.valorSalarioFixo = valorSalarioFixo;
    }

    public double getValorSalarioFixo() {
        return this.valorSalarioFixo;
    }

    public void setValorSalarioFixo(double valorSalarioFixo) {
        this.valorSalarioFixo = valorSalarioFixo;
    }

    @Override
    public double calculaSalario () {
        return this.valorSalarioFixo;
    }
}
