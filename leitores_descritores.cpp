#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

#define TRUE 1

sem_t mutex;                    /* controla o acesso a 'rc' */
sem_t db;                       /* controla o acesso a base de dados */
int rc = 0;                     /* número de processos lendo ou querendo ler */

void* reader(void *arg);
void* writer(void *arg);
void read_data_base();
void use_data_read();
void think_up_data();
void write_data_base();

int main() {
sem_init(&mutex, 0, 1);
sem_init(&db, 0, 1);

pthread_t r[3], w[2];

int i;

    /* criando leitores */
    for (i = 0; i < 3 ; i++) {
 pthread_create(&r[i], NULL, reader, (void*) &i);
}

    /* criando escritores */
    for (i = 0; i< 2; i++) {
 pthread_create(&w[i], NULL, writer, (void*) &i);
}

while(TRUE);
return 0;
}

void* reader(void *arg) {
int i = *((int *) arg);

while(TRUE) {               /* repere para sempre */
 sem_wait(&mutex);       /* obtém acesso exclusivo à 'rc' */
 rc = rc + 1;            /* um leitor a mais agora */

 if (rc == 1) {          /* se este for o primeiro leitor... */
     sem_wait(&db);   
 }

 sem_post(&mutex);       /* libera o acesso exclusivo a 'rc' */
 read_data_base(i);       /* acesso aos dados */
 sem_wait(&mutex);       /* obtém acesso exclusivo a 'rc' */
 rc = rc - 1;            /* um leitor a menos agora */

 if (rc == 0) {          /* se este for o último leitor */   
     sem_post(&db);
 }

 sem_post(&mutex);       /* libera o acesso exclusivo a 'rc' */
 use_data_read(i);        /* região não crítica */
}
}

void* writer(void *arg) {
int i = *((int *) arg);

while(TRUE) {               /* repete para sempre */
 think_up_data(i);        /* região não crítica */
 sem_wait(&db);          /* obtém acesso exclusivo */
 write_data_base(i);      /* atualiza os dados */
 sem_post(&db);          /* libera o acesso exclusivo */
}
}

void read_data_base(int i) {
printf("Reader %d estah lendo os dados!\n", i);
sleep( rand() % 5);
}

void use_data_read(int i) {
printf("Reader %d estah usando os dados lidos!\n", i);
sleep(rand() % 5);
}

void think_up_data(int i) {
printf("Writer %d estah pensando no que escrever!\n", i);
sleep(rand() % 5);
}

void write_data_base(int i) {
printf("Writer %d estah escrevendo os dados!\n", i);
sleep( rand() % 5);
}
