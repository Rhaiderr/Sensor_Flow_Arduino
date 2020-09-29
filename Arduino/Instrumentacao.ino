#include <Thermistor.h>
Thermistor temp(1);
float vazao; //Variável para armazenar o valor em L/min
float media=0; //Variável para tirar a média a cada 1 minuto
int contaPulso; //Variável para a quantidade de pulsos
int i=0; //Variável para contagem
int temperature; //Variável para armazenar o valor de temperatura


void setup() {

  Serial.begin(9600);
  pinMode(2, INPUT);
  attachInterrupt(0, incpulso, RISING); //Configura o pino 2(Interrupção 0) para trabalhar como interrupção
  delay(1000);
}

void loop() {
  
  contaPulso = 0;   //Zera a variável para contar os giros por segundos
  sei();      //Habilita interrupção
  delay(1000);
  cli();      //Desabilita interrupção
  temperature = temp.getTemp(); //Realiza leitura da temperatura
  Serial.println(temperature);// Imprime na serial o valor da temperatura
  vazao = contaPulso / 5.5; //Converte para L/min
  Serial.println(vazao); //Imprime na serial o valor da vazão
}

void incpulso ()
{ 
  contaPulso++; //Incrementa a variável de contagem dos pulsos
}
