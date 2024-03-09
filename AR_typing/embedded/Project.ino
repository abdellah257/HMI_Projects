#define RTHUMB 2
#define RINDEX 3
#define RMID   4
#define RDDD   5
#define RPTT   6
#define LTHUMB 7
#define LINDEX 8
#define LMID   9
#define LDDD   10
#define LPTT   11

int last_button = 0;
int last_time = 0;
int current_time = 0;
int loop_indx = 0;
char message[50];
bool checkLast = false;
int lastClickState[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
const int TYPE_SPEED = 700;


void setup()
{
  Serial.begin(9600);
  memset(message, '\0', sizeof(message));
  pinMode(RTHUMB, INPUT_PULLUP);
  pinMode(RINDEX, INPUT_PULLUP);
  pinMode(RMID, INPUT_PULLUP);
  pinMode(RDDD, INPUT_PULLUP);
  pinMode(RPTT, INPUT_PULLUP);
  pinMode(LTHUMB, INPUT_PULLUP);
  pinMode(LINDEX, INPUT_PULLUP);
  pinMode(LMID, INPUT_PULLUP);
  pinMode(LDDD, INPUT_PULLUP);
  pinMode(LPTT, INPUT_PULLUP);
  last_button = 0;
}

void checkFinger(int i){
    // A Switch over the finger's associated numbers as in the definition above
    switch (i)
    {
    case 2:
           
        if( last_button == 2 && current_time - last_time < TYPE_SPEED){
            loop_indx += 1;
            strcpy(message, "Right THUMB MULTI ");
            Serial.print(message);
            Serial.println(loop_indx);
                     
        }else {
            if(checkLast) {
              Serial.print(message);
              Serial.println(loop_indx);
              checkLast = false;
              loop_indx = 0;
            }
            strcpy(message, "Right THUMB ");
            Serial.println(message);
            current_time = 0;
            loop_indx = 0;
        }
        last_time = current_time;
        last_button = 2;
        break;
    case 3:
        if( last_button == 3 && current_time - last_time < TYPE_SPEED){
            loop_indx += 1;
            strcpy(message, "Right INDEX MULTI ");
            Serial.print(message);
            Serial.println(loop_indx);
        }else{
            if(checkLast) {
              Serial.print(message);
              Serial.println(loop_indx);
              checkLast = false;
              loop_indx = 0;
            }
            strcpy(message, "Right INDEX  ");
            Serial.println(message);
            current_time = 0;
            loop_indx = 0;
        }
        last_time = current_time;
        last_button = 3;
        break;
    case 4:
        if( last_button == 4 && current_time - last_time < TYPE_SPEED){
            loop_indx += 1;
            strcpy(message, "Right MIDDLE MULTI ");
            Serial.print(message);
            Serial.println(loop_indx);
        }else{
            if(checkLast) {
              Serial.print(message);
              Serial.println(loop_indx);
              checkLast = false;
              loop_indx = 0;
            }
            strcpy(message, "Right MIDDLE ");
            Serial.println(message);
            current_time = 0;
            loop_indx = 0;
        }
        last_time = current_time;
        last_button = 4;
        break;
    case 5:
        if( last_button == 5 && current_time - last_time < TYPE_SPEED){
            loop_indx += 1;
            strcpy(message, "Right DDD MULTI ");
            Serial.print(message);
            Serial.println(loop_indx);
        }else{
            if(checkLast) {
              Serial.print(message);
              Serial.println(loop_indx);
              checkLast = false;
              loop_indx = 0;
            }
            strcpy(message, "Right DDD ");
            Serial.println(message);
            current_time = 0;
            loop_indx = 0;
        }
        last_time = current_time;
        last_button = 5;
        break;
    case 6:
        if( last_button == 6 && current_time - last_time < TYPE_SPEED){
            loop_indx += 1;
            strcpy(message, "Right PETIT MULTI ");
            Serial.print(message);
            Serial.println(loop_indx);
        }else{
            if(checkLast) {
              Serial.print(message);
              Serial.println(loop_indx);
              checkLast = false;
              loop_indx = 0;
            }
            strcpy(message, "Right PETIT ");
            Serial.println(message);
            current_time = 0;
            loop_indx = 0;
        }
        last_time = current_time;
        last_button = 6;
        break;
    case 7:
        if( last_button == 7 && current_time - last_time < TYPE_SPEED){
            loop_indx += 1;
            strcpy(message, "Left THUMB MULTI ");
            Serial.print(message);
            Serial.println(loop_indx);
        }else{
            if(checkLast) {
              Serial.print(message);
              Serial.println(loop_indx);
              checkLast = false;
              loop_indx = 0;
            }
            strcpy(message, "Left THUMB ");
            Serial.println(message);
            current_time = 0;
            loop_indx = 0;
        }
        last_time = current_time;
        last_button = 7;
        break;
    case 8:
        if( last_button == 8 && current_time - last_time < TYPE_SPEED){
            loop_indx += 1;
            strcpy(message, "Left INDEX MULTI ");
            Serial.print(message);
            Serial.println(loop_indx);
        }else{
            if(checkLast) {
              Serial.print(message);
              Serial.println(loop_indx);
              checkLast = false;
              loop_indx = 0;
            }
            strcpy(message, "Left INDEX ");
            Serial.println(message);
            current_time = 0;
            loop_indx = 0;
        }
        last_time = current_time;
        last_button = 8;
        break;
    case 9:
        if( last_button == 9 && current_time - last_time < TYPE_SPEED){
            loop_indx += 1;
            strcpy(message, "Left MIDDLE MULTI ");
            Serial.print(message);
            Serial.println(loop_indx);
            
        }else{
            if(checkLast) {
              Serial.print(message);
              Serial.println(loop_indx);
              checkLast = false;
              loop_indx = 0;
            }
            strcpy(message, "Left MIDDLE ");
            Serial.println(message);
            current_time = 0;
            loop_indx = 0;
        }
        last_time = current_time;
        last_button = 9;
        break;
    case 10:
        if( last_button == 10 && current_time - last_time < TYPE_SPEED){
            loop_indx += 1;
            strcpy(message, "Left DDD MULTI ");
            Serial.print(message);
            Serial.println(loop_indx);
        }else{
            if(checkLast) {
              Serial.print(message);
              Serial.println(loop_indx);
              checkLast = false;
              loop_indx = 0;
            }
            strcpy(message, "Left DDD ");
            Serial.println(message);
            current_time = 0;
            loop_indx = 0;
        }
        last_time = current_time;
        last_button = 10;
        break;
    case 11:
        if( last_button == 11 && current_time - last_time < TYPE_SPEED){
            loop_indx += 1;
            strcpy(message, "Left PETIT MULTI ");
            Serial.print(message);
            Serial.println(loop_indx);
        }else{
            if(checkLast) {
              Serial.print(message);
              Serial.println(loop_indx);
              checkLast = false;
              loop_indx = 0;
            }
            strcpy(message, "Left PETIT");
            Serial.println(message);
            current_time = 0;
            loop_indx = 0;
        }
        last_time = current_time;
        last_button = 11;
        break;
    default:
        break;
    }
}

void do_Press(int i){

}


void loop()
{
    if(current_time - last_time >= TYPE_SPEED && checkLast == true){
      Serial.print(message);
      Serial.println(loop_indx);
      loop_indx = 0;
      checkLast = false;      
    }
    for(int i = 2; i < 12; i++){
      if(digitalRead(i) == LOW && lastClickState[i-2] == 0){
        lastClickState[i-2] = 1;
        checkFinger(i);
        break;
      }
      else if(digitalRead(i) == HIGH) lastClickState[i-2] = 0;
    }
    current_time += 50;
    delay(50);
}