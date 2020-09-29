public class Comissionado extends Colaborador {
    private double percentualComissao;
    private double totalVendasDoMes;

    public Comissionado(String nome, int horasTrabalhadas, double percentualComissao, double totalVendasDoMes) {
        super(nome, horasTrabalhadas);
        this.percentualComissao = percentualComissao;
        this.totalVendasDoMes = totalVendasDoMes;

    }

    public double getPercentualComissao() {
        return this.percentualComissao;
    }

    public void setPercentualComissao(double percentualComissao) {
        this.percentualComissao = percentualComissao;
    }

    public double getTotalVendasDoMes() {
        return this.totalVendasDoMes;
    }

    public void setTotalVendasDoMes(double totalVendasDoMes) {
        this.totalVendasDoMes = totalVendasDoMes;
    }

    @Override
    public double calculaSalario () {
        return this.totalVendasDoMes * this.percentualComissao;
    }

}
