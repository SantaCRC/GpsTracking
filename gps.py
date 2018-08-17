import time
alot=-83.909700

def escribir():
    x = 0
    alat = 9.856070
    altitud=str(1)
    while altitud!="0":
        """lat=str(input("lat: "))
        log=str(input("log: "))
        altitud=str(input("altitud: "))"""
        arch = open("test.kml", "w")
        lat=str(alat+0.000001)
        alat=alat+0.000001
        log=str(alot)
        arch.write("""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
   <Style id="randomColorIcon">
      <IconStyle>
         <color>ff00ff00</color>
         <colorMode>normal</colorMode>
         <scale>1.1</scale>
         <Icon>
            <href>globo.png</href>
         </Icon>
      </IconStyle>
   </Style>
   <Placemark>
      <name></name>
      <description>Altitud:"""+altitud+"""</description>
      <styleUrl>#randomColorIcon</styleUrl>
      <Point>
         <coordinates>"""+log+","+lat+","+altitud+"""</coordinates>
      </Point>
   </Placemark>
</Document>
</kml>""")
        arch.close()
        time.sleep(0.8)
        print("hecho")
        altitud=str(x+1)
        x=x+1


escribir()