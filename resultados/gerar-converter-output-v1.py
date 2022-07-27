# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 17:33:32 2022
@author: flavio.vasconcelos
"""
import os


xml2csv = "D:\\Codigos\\simulacao-22\\xml2csv.py"
directory = "D:\\Codigos\\simulacao-22\\"
qtdSeed = 30
qtdScenery = 4
qtdTypeOutput = 3

scenery = ["completo",                  
           "sem-semaforo-manual",
           "sem-faixa-azul",
           "sem-faixa-azul-sem-semaforo-manual"]

typeOutput = ["summary",                  
              "vehroute",
              "tripinfo"]

sceneryMapFile = ["fernandes-lima-v118.v13.sim1.net.xml",                  
                  "fernandes-lima-v118.v13.sim1.sem-semaforo-manual.sim1.net.xml",
                  "fernandes-lima-v118.v13.sim1.sem-faixa-azul.sim1.net.xml",
                  "fernandes-lima-v118.v13.sim1.sem-faixa-azul.sem-semaforo-manual.sim1.net.xml"]
        

# Loop Cenário
for j in range (qtdScenery):                  
    # Loop Seed
    for i in range (qtdSeed):                     
        # Loop Seed
        for y in range (qtdTypeOutput):                                 
            file = ("D:\\Codigos\\simulacao-22\\output." + scenery[j] + ".seed" + str(i+1) + "." + typeOutput[y] + ".out.xml --output D:\\Codigos\\simulacao-22\\output." + scenery[j] + ".seed"+ str(i+1) + "." + typeOutput[y] + ".csv")
            #os.system("cmd /c python D:\\Codigos\\simulacao-22\\xml2csv.py D:\\Codigos\\simulacao-22\\estatistica-volumetrica-" + scenery[j] + "-seed-" + str(i+1) + ".out --output D:\\Codigos\\simulacao-22\\estatistica-volumetrica-" + scenery[j] + "-seed-" + str(i+1) + ".csv")                
            os.system("cmd /c python "+ xml2csv + " " + file)               
            
            print("Output: ", scenery[j] ," Seed: ", str(i+1), " Tipo: ", typeOutput[y])