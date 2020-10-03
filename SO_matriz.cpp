#include <iostream>
#include <time.h>
#include <thread> 
#include <vector>
using namespace std;

void ler_matriz (int A[][2]);
void print_matriz (int matriz[2][2]);
void sum_row (int matriz[2][2]);

int nthreads = 5;
int main () {
    int matriz[2][2];
    ler_matriz(matriz);
    print_matriz(matriz);
    sum_row(matriz);

    
}

void ler_matriz (int matriz[2][2]) {
    srand(time(NULL));
    for (int i=0; i<nthreads; i++) 
        for (int j=0; j<nthreads; j++)
            matriz[i][j] = rand() % 10;
}

void print_matriz (int matriz[2][2]) {
    for (int i=0; i<nthreads; i++) {
        for (int j=0; j<nthreads; j++) {
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }
}

void sum_row (int matriz[2][2]) {

    vector <thread> threads(nthreads);

    int sum=0, row[nthreads];
    for (int i=0; i<nthreads; i++) {
        sum = 0;
        for (int j=0; j<nthreads; j++) {
            sum += matriz[i][j];
            row[i] = sum; 
        }
    }
    cout << endl;
    for (int i=0; i<nthreads;i++) {
        cout << row[i] << " ";
    }
}

