public class teste {
    public static void main(final String[] args) {
        final int n1 = 6;
        final int n2 = 8;
        if (n1 < n2) {
            System.out.println("n2 maior");
            System.out.println(n2);
        } else {
            System.out.println("n1 maior");
            System.out.println(n1);
        }
        
        for (int i=0; i<5; i++) {
            if (i == 2) {
                continue;
            }
            
            if (i == 4) {
                break;
            }
            System.out.println(i);
    }

}
}