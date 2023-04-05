// C++ code
//
void setup()
{
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
}

void s()
{
  int i = 0;
  
  while(i<3){
    digitalWrite(LED_BUILTIN, HIGH);
    delay(250); 
    digitalWrite(LED_BUILTIN, LOW);
    delay(250); 
    i = i + 1;
   }
  
  delay(700);
}

void o()
{
  int i = 0;
  
  while(i<3){
    digitalWrite(13, HIGH);
    delay(500); 
    digitalWrite(13, LOW);
    delay(500); 
    i = i + 1;
   }
  
  delay(700);
}

void piscaAlternado()
{
  int i = 0;
  
  while(i<3){
    digitalWrite(13, HIGH);
    delay(500); 
    digitalWrite(13, LOW);
    delay(500); 
    digitalWrite(12, HIGH);
    delay(500); 
    digitalWrite(12, LOW);
    delay(500); 
    i = i + 1;
  }
	
}

void piscaJunto()
{
  int i = 0;
  
  while(i<3){
    digitalWrite(13, HIGH);
    digitalWrite(12, HIGH);
    delay(500); 
    digitalWrite(13, LOW);
    digitalWrite(12, LOW);
    delay(500); 
    i = i + 1;
  }
	
}

void loop()
{
  
  s();
  o();
  s();
  delay(1000);
  
  piscaAlternado();
  delay(1000);
  
  piscaJunto();
  delay(1000);
  
}