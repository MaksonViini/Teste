public class Horista extends Colaborador{
    private double valorHora;

    public Horista (String nome, int horasTrabalhadas, double valorHora) {
        super(nome, horasTrabalhadas);
        this.valorHora = valorHora;
    }

    public double getValorHora() {
        return this.valorHora;
    }

    public void setValorHora(double valorHora) {
        this.valorHora = valorHora;
    }

    @Override
    public double calculaSalario () {
        return this.valorHora * this.getHorasTrabalhadas();
    }
}
