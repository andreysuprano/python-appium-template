start java -jar selenium-server-standalone-3.141.59.jar -role hub -port 8080
start appium -a 127.0.0.1 -p 4725 --nodeconfig ../device_capabilities/Nexus_S_7.json
start appium -a 127.0.0.1 -p 4730 --nodeconfig ../device_capabilities/Pixel_2_8.json
start appium -a 127.0.0.1 -p 4735 --nodeconfig ../device_capabilities/Pixel_3_10.json