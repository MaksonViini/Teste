#include <cekeikon.h>
void inicializa(Mat_<float>& A, Mat_<float>& B, int n, int seed)
{ A.create(n,n);
 B.create(n,n);
 srand(seed);
 for (int l=0; l<n; l++)
 for (int c=0; c<n; c++)
 A(l,c)=rand()%n;
 for (int l=0; l<n; l++)
 for (int c=0; c<n; c++)
 B(l,c)=rand()%n;
}
void multMatConvencional(const Mat_<float>& A, const Mat_<float>& B,
Mat_<float>& D)
{ D.create(A.rows,B.cols);
 for (int l=0; l<A.rows; l++)
 for (int c=0; c<B.cols; c++) {
 float d=0.0;
 for (int i=0; i<A.cols; i++)
 d=d+A(l,i)*B(i,c);
 D(l,c)=d;
 }
}
int main(int argc, char** argv) {
 if (argc!=3) {
 printf("Convencional: Multiplica duas matrizes nxn\n");
 printf("Convencional n seed\n");
 printf(" As matrizes sao preenchidas com numeros de 0 a n-1\n");
 erro("Erro: Numero de argumentos invalido");
 }
 int n;
 convArg(n,argv[1]);
 int seed;
 convArg(seed,argv[2]);
 Mat_<float> A,B;
 inicializa(A,B,n,seed);
 int t1=centseg();
 Mat_<float> D;
 multMatConvencional(A,B,D);
 int t2=centseg()-t1;
 printf("Tempo gasto convencional: %d.%02ds\n",t2/100,t2%100);
}