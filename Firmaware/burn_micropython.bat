::
:: %1 - connection to connect
:: %2 - bin to burn
::
"C:\\Users\\Orel\\AppData\\Local\\Arduino15\\packages\\esp32\\tools\\esptool_py\\4.2.1/esptool.exe" --port %1 erase_flash
"C:\\Users\\Orel\\AppData\\Local\\Arduino15\\packages\\esp32\\tools\\esptool_py\\4.2.1/esptool.exe" --port %1 write_flash 0x1000 %2
echo.
echo --- MicroPython BURNING WAS COMPLETED! ---
