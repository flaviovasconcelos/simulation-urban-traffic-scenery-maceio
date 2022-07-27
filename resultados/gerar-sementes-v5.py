# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 03:03:39 2022
@author: Flavio Vasconcelos
"""

import os, sys
import subprocess
import traci

#import xml.etree.ElementTree as ET

from xml.dom import minidom
import xml.etree.cElementTree as ET



try:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', "tools"))  # tutorial in tests
    sys.path.append(os.path.join(os.environ.get("SUMO_HOME", os.path.join(os.path.dirname(__file__), "..", "..", "..")), "tools"))  # tutorial in docs
    from sumolib import checkBinary
except ImportError:
    sys.exit("please declare environment variable 'SUMO_HOME' as the root directory of \
        your sumo installation (it should contain folders 'bin', 'tools' and 'docs')")
        

# print(os.environ['OS'])        
'''
os.environ["SUMO-SCENARY"] = "completo"
os.environ["SUMO-SEED"] = "50"

os.system('SET SUMO-SCENARY=completo')
os.system('SET SUMO-SEED=50')

print ("SUMO SEED: ",os.environ['SUMO-SEED'])
print ("SUMO SCENARY: ", os.environ['SUMO-SCENARY'])
'''

        
# --------------- VARIAVEIS -------------------------------------------------        

directory = "D:/Codigos/simulacao-22/"
rangeScenery = 4
scenery = ["completo",                  
           "sem-semaforo-manual",
           "sem-faixa-azul",
           "sem-faixa-azul-sem-semaforo-manual"]

sceneryMapFile = ["fernandes-lima-v118.v13.sim1.net.xml",                  
                  "fernandes-lima-v118.v13.sim1.sem-semaforo-manual.sim1.net.xml",
                  "fernandes-lima-v118.v13.sim1.sem-faixa-azul.sim1.net.xml",
                  "fernandes-lima-v118.v13.sim1.sem-faixa-azul.sem-semaforo-manual.sim1.net.xml"]

#mapFile = "fernandes-lima-v118.v13.sim1.net.xml"
routeFile = directory + "fernandes-lima-v118.car.flow.sim9.rou.xml," + \
            directory + "fernandes-lima-v118.taxi.sim9.rou.xml," + \
            directory + "fernandes-lima-v118.bus.flow.sim9.rou.xml," + \
            directory + "fernandes-lima-v118.truck.sim9.rou.xml"
            
additionalFiles = "fernandes-lima-v118.v2.variavel.add.xml"
#tree = ET.parse("fernandes-lima-v118.v2.variavel.add.xml")
#root = tree.getroot()
#print("Imprimindo XML",root)

#mydoc = minidom.parse(additionalFiles)
#items = mydoc.getElementsByTagName('e1Detector')
#print('Nome do arquivo:', items[1].attributes['file'].value)


# VARIAVEIS
qtdSeed = 30
PORT = "8833"
beginTime = 0
endTime = 5400
emissionsProbability = 1


def run():
    traci.init(int(PORT))
    step = 0
    #while traci.simulation.getMinExpectedNumber() > 0:
    while step < endTime:
        traci.simulationStep()
        step += 1
    traci.close()

# --------------- EXECUCAO -------------------------------------------------
if __name__ == "__main__":

    sumoBinary = checkBinary('sumo')
    
    # Codigo para reescrever o xml adicional
    tree = ET.parse(additionalFiles)
    root = tree.getroot()
    data = ET.Element('additional')


    # Loop Cenário
    for j in range (rangeScenery):        
        mapFile = directory + sceneryMapFile[j]            
        
        # Loop Seed
        for i in range (qtdSeed):
            tripInfoFile = (directory + "output." + scenery[j] + ".seed" + str(i+1) + ".tripinfo.out.xml")
            summaryFile = (directory + "output." + scenery[j] + ".seed" + str(i+1) + ".summary.out.xml")
            vehrouteFile = (directory + "output." + scenery[j] + ".seed" + str(i+1) + ".vehroute.out.xml")
            fcdFile = (directory + "output." + scenery[j] + ".seed" + str(i+1) + ".fcd.out.xml")
            emissionFile = (directory + "output." + scenery[j] + ".seed" + str(i+1) + ".emission.out.xml")
            
            # Loop xml adicional busStop e e1Detector
            for x in root:   
                if x.tag != 'busStop':
                    x.attrib['file'] = 'estatistica-volumetrica-' + scenery[j] + '-seed-' + str(i+1) + '.out'                                            
            xml_file_name = 'xml-estatistica-volumetrica-' + scenery[j] + '-seed-' + str(i+1) +'.add.xml'
            xml_file_out = tree.write(xml_file_name, encoding="utf-8")
            
            
            sumoProcess = subprocess.Popen([sumoBinary, 
        				'-n', mapFile ,
        				'-r', routeFile, 
                        '--additional-files', directory + xml_file_name, 
        				'--remote-port', PORT,
                        '--seed', str(i+1),
                        '--device.emissions.probability', str(emissionsProbability),
                        '--tripinfo-output', tripInfoFile,
                        '--summary-output', summaryFile,
                        '--vehroute-output', vehrouteFile,
                        #'--fcd-output', fcdFile,
                        #'--emission-output', emissionFile,
                        '-b', str(beginTime), 
                        '-e', str(endTime)])
            print(" Seed:", i+1, "Cenário:",scenery[j])
            run()
            sumoProcess.wait()
