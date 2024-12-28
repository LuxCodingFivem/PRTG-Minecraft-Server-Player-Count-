# PRTG-Minecraft-Server-Player-Count
PRTG Custom Sensor to Monitor the Current Player

# Installtion 

1. Download Ping over Port.py
2. Open Python file and edit the Translation in line 17
3. Copy file in following path on your PRTG Server C:\Program Files (x86)\PRTG Network Monitor\Custom Sensors\python\
4. Open CMD and Change Directory to C:\Program Files (x86)\PRTG Network Monitor\python
5. Type "python.exe -m pip install mcstatus" to install the needed Lib
6. Add a new Sensor on your PRTG web interface (Python Script Advanced)
7. Chose a name for the sensor
8. Chose Ping over Port.py as Script
9. You need the following additional parameters: %host, [Port of the Minecraft Server], [max Player until warning], [Minecraft Server Name]
10. Save the Sensor

# License 

MIT License  

Copyright (c) 2024 LuxCoding

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


Thanks for using my Custom PRTG Sensor 
