
//Program for controlling Saber_tooth
//Four wheel Drive

int mapper[2]={ };
void setup() {
 Serial.begin(9600);
 Serial1.begin(9600);
 Serial3.begin(9600);                  //Serial pins attachment
}

void loop() {
int a,b;
int ch1=pulseIn(A15,HIGH);   
int ch2=pulseIn(A13,HIGH);            //for pwm

a=map(ch1,1852,1023,50,-50);         //mapping the values in required range
b=map(ch2,1020,1855,-50,50);

control(a,b);
 
left(mapper[0]);                     //for controlling left motors
right(mapper[1]);                    //for controlling right motors

}

void control (int a,int b)           //combining two channels of RC
{mapper[0]=a+b;
 mapper[0]=safe(mapper[0]);

 mapper[1]=a-b;
 mapper[1]=safe(mapper[1]);
}


int safe(int f)                     //for stop condition
{ f= (f>-10 && f<10) ? 0:f;
 return f;}  



void left(int e)
{int g,x;
  x=map(e,-100,100,128,255);
  g=map(e,-100,100,1,127);

  Serial1.write(x);
  Serial3.write(g); 
}


void right(int f)
{int g,x;
  g=map(f,-100,100,128,256);
  x=map(f,-100,100,1,127);
  Serial1.write(x);
  Serial3.write(g);
}
