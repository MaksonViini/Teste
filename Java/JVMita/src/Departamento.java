import java.util.ArrayList;
import java.util.List;

public class Departamento {
    private List <Colaborador> colaboradores;
    private double[] salarios;

    public Departamento () {
        this.colaboradores = new ArrayList<>();
    }

    public void adicionaColaborador (Colaborador colaborador) {
        this.colaboradores.add(colaborador);
    }

    public List<Colaborador> getColaboradores() {
        return this.colaboradores;
    }

    public void calculaSalarioColaboradores () {
        salarios = new double [colaboradores.size()];
        int contaSalarios = 0;
        for (Colaborador colaborador : colaboradores) {
            salarios[contaSalarios++] = colaboradores.calculaSalario();
        }
    }

    public double[] getSalarios() {
        return this.salarios;
    }
}
