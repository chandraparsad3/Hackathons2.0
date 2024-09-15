#include <DHT.h>

#define DHTPIN 2      
#define DHTTYPE DHT11  
#define LDRPIN A2      
#define MQ135PIN A0   
#define MQ7PIN A1     

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  Serial.println("Sensors initialized.");
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor");
  } else {
    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.println(" °C");

    Serial.print("Humidity: ");
    Serial.print(humidity);
    Serial.println(" %");
  }

  int ldrValue = analogRead(LDRPIN);
  float lightIntensity = ldrValue * (5.0 / 1023.0) * 100;
  int mq135Value = analogRead(MQ135PIN);
  float co2 = convertMQ135Reading(mq135Value, "CO2");
  float nh3 = convertMQ135Reading(mq135Value, "NH3");
  float c4h10 = convertMQ135Reading(mq135Value, "C4H10");
  float ch4 = convertMQ135Reading(mq135Value, "CH4");

  int mq7Value = analogRead(MQ7PIN);
  float co = convertMQ7Reading(mq7Value);

  Serial.print("Light Intensity: ");
  Serial.print(lightIntensity);
  Serial.println(" lux");

  Serial.print("CO2: ");
  Serial.print(co2);
  Serial.println(" ppm");

  Serial.print("NH3: ");
  Serial.print(nh3);
  Serial.println(" ppm");

  Serial.print("C4H10: ");
  Serial.print(c4h10);
  Serial.println(" ppm");

  Serial.print("CH4: ");
  Serial.print(ch4);
  Serial.println(" ppm");

  Serial.print("CO: ");
  Serial.print(co);
  Serial.println(" ppm");

  delay(60000);  
}

float convertMQ135Reading(int rawValue, String gasType) {
  float concentration = 0.0;
  if (gasType == "CO2") {
    concentration = rawValue * 0.15; 
  } else if (gasType == "NH3") {
    concentration = rawValue * 0.26;  
  } else if (gasType == "C4H10") {
    concentration = rawValue * 0.37;  
  } else if (gasType == "CH4") {
    concentration = rawValue * 0.45;  
  }
  return concentration;
}

float convertMQ7Reading(int rawValue) {
  float concentration = rawValue * 0.5; 
  return concentration;
}
