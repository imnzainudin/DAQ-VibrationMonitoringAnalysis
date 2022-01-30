/*
 *    Muhammad Iman Bin Zainudin
 *  Online Data Acquisiton with GUI
 *          using Free Rtos
 */
//Include Library
#include <Arduino.h>
//#include "semphr.h" //vanilla needs
#include "DHTesp.h"

//Define pin
#define DHTPIN 3
#define x 25
#define y 26
#define z 27

//DHT22-Temperature & Humidity Sensor
DHTesp dht;

TempAndHumidity sensorData;
float humid, tempC;
float initialx, initialy, initialz, ax, ay, az;

//FreeRTOS
TaskHandle_t Task1;
TaskHandle_t Task2;

//Period
static const int Period_Task1 = 2000;
//Printing
float uhumid, utempC;

//Globals
static SemaphoreHandle_t mutex;

void setup()
{
  Serial.begin(115200);
  dht.setup(DHTPIN, DHTesp::DHT22);

  initialx=(analogRead(x)*3.3)/4095;
  initialy=(analogRead(y)*3.3)/4095;
  initialz=(analogRead(z)*3.3)/4095; 
  
  //Creating mutex
  mutex = xSemaphoreCreateMutex();

  //Creating tasks
  xTaskCreatePinnedToCore(
    TaskTemperature,  //Task function
    "Task1",          //Name
    4000,            //Stack size
    NULL,             //Parameter
    1,                //Priority
    &Task1,           //Handle
    0);               //Core
  delay(500);

  xTaskCreatePinnedToCore(
    TaskVibration,  //Task function
    "Task2",          //Name
    4000,            //Stack size
    NULL,             //Parameter
    1,                //Priority
    &Task2,           //Handle
    1);               //Core
  delay(500);
}

void loop()
{
}

/*
 *            Function CALL
 *---------------------------------------
 */
void TaskTemperature(void * pvParameters)
{
  TickType_t xLastWakeTime;
  const TickType_t xFrequency = Period_Task1/portTICK_PERIOD_MS;

  xLastWakeTime = xTaskGetTickCount();
  /*
   * DHT22 Temperature Sensor
   */
  for(;;)
  {
      do
      {
        tempC = dht.getTemperature();
        humid = dht.getHumidity();
      }
      while(isnan(humid) || isnan(tempC));
    if(xSemaphoreTake(mutex, 1) == pdTRUE) 
    {
      //Print if changes in value
      if(uhumid!=humid||utempC!=tempC)
      {
        Serial.print(tempC);
        Serial.print(",");
        Serial.print(humid);
      }
      else
      {
        Serial.print(",");
      }

      vTaskDelay(100/portTICK_PERIOD_MS);
      xSemaphoreGive(mutex);
      uhumid=humid;
      utempC=tempC;
      
      vTaskDelayUntil(&xLastWakeTime, xFrequency);
      /*Serial.print("tempC: ");
      Serial.println(utempC);
      Serial.print("humid: ");
      Serial.println(uhumid);*/
    }  
  }
}

void TaskVibration(void * pvParameters)
{
  /*
   * Gy-61 3-axis Accelerometer
   */
  for(;;)
  {
      ax = (((analogRead(x)*3.3)/4095) - initialx)/0.330; //get X
      ay = (((analogRead(y)*3.3)/4095) - initialy)/0.330; //get Y
      az = (((analogRead(z)*3.3)/4095) - initialz)/0.330; //get Z
      
    if(xSemaphoreTake(mutex, 0) == pdTRUE) 
    {
      Serial.print(",");
      Serial.print(",");
      Serial.print(ax);Serial.print(",");
      Serial.print(ay);Serial.print(",");
      Serial.println(az);

      xSemaphoreGive(mutex);
      vTaskDelay(100/portTICK_PERIOD_MS);
    }

    else
    {
      Serial.print(",");
      Serial.print(ax);Serial.print(",");
      Serial.print(ay);Serial.print(",");
      Serial.println(az);

      vTaskDelay(100/portTICK_PERIOD_MS);
    }
    //Serial.println(initialx);
    //Serial.println(initialy);
    //Serial.println(initialz);
  }
}
