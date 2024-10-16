#include <U8g2lib.h>
#include <Wire.h>

U8G2_SSD1306_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0);

const int sensorPin = 36;
const int numReadings = 100;
int readings[numReadings];
int currentIndex = 0;
int total = 0;

void setup() {
  Serial.begin(115200);
  u8g2.begin();
  u8g2.setFont(u8g2_font_profont12_tf);

  for (int i = 0; i < numReadings; i++) {
    readings[i] = 0;
  }
}

void loop() {
  int sensorValue = analogRead(sensorPin);

  total = total - readings[currentIndex];
  readings[currentIndex] = sensorValue;
  total = total + readings[currentIndex];
  currentIndex = (currentIndex + 1) % numReadings;

  float average = total / numReadings;

  u8g2.firstPage();
  do {
    u8g2.clearBuffer();

    u8g2.setFont(u8g2_font_profont12_tf);
    u8g2.setCursor(2, 15);
    u8g2.print("Sensor Reading: ");
    u8g2.setCursor(110, 15);
    u8g2.print(sensorValue);

    u8g2.setFont(u8g2_font_profont10_mr);
    u8g2.setCursor(2, 60);
    u8g2.print("Average Reading: ");
    u8g2.setCursor(110, 60);
    u8g2.print(average);
   

    u8g2.drawLine(0, 45, 127, 45); // Draw a horizontal line

    // Plot the sensor readings as a graph
    int xPos = 0;
    int yPos = 63 - map(sensorValue, 2000, 4095, 0, 63);
    for (int i = 0; i < numReadings - 1; i++) {
      int x = map(i, 0, numReadings - 2, 0, 127);
      int y = 63 - map(readings[(currentIndex + i + 1) % numReadings], 0, 4095, 0, 63);
      u8g2.drawLine(xPos, yPos, x, y);
      xPos = x;
      yPos = y;
    }

  } while (u8g2.nextPage());

  delay(100);
}

