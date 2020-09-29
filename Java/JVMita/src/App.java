public class App {
    public static void main(String[] args) {
        Departamento departamento = new Departamento();

        departamento.adicionaColaborador(new Assalariado("Jose", 160, 1045));
        departamento.adicionaColaborador(new Comissionado("Raules", 160, 0.15, 134000));
        departamento.adicionaColaborador(new Horista("Craules", 160, 21));

        /*for (Colaborador colaborador : departamento.getColaboradores()) {
            System.out.println(colaborador.getNome() + 
                            " tem o salario de R$" + 
                            colaborador.calculaSalario());
        } */

        departamento.calculaSalarioColaboradores();
    }
}
