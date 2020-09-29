public class Colaborador  implements IColaboradorIpml {
    private String nome;
    private int HorasTrabalhadas;

    public Colaborador (String nome, int HorasTrabalhadas) {
        this.nome = nome;
        this.HorasTrabalhadas = HorasTrabalhadas;
    }

	public String getNome() {
		return this.nome;
    }
    
	public void setNome(String nome) {
		this.nome = nome;
    }
    
	public int getHorasTrabalhadas() {
		return this.HorasTrabalhadas;
    }
    
	public void setHorasTrabalhadas(int horasTrabalhadas) {
		HorasTrabalhadas = horasTrabalhadas;
	}

	@Override
	public double calculaSalario() {
        
		return 0;
	}
    
}
