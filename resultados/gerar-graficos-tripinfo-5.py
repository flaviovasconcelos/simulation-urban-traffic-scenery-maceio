# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 21:17:48 2022
@author: Flavio Vasconcelos
"""

import pandas as pl
import matplotlib.pyplot as plt
import numpy as np


#Exemplo
#dados.pd.read_csv('arquivo.csv', sheet_name = 'seed-1')

# id
# arrival (chegada) - depart (partida) = tempo de viagem
# duration
# vType = passanger,taxi,truck,bus
# CO2_abs = mg
# fuel_abs = ml
# tripinfo_depart > 899.00
# tripinfo_arrival < 4500

qtdSeed = 30
scenery = ["completo",                  
           "sem-semaforo-manual",
           "sem-faixa-azul",
           "sem-faixa-azul-sem-semaforo-manual"]

typeVehicle = ["car","truck","bus"]
typeOutput = ["car","truck","bus"]

car_1 = "0.1." #Fernandes Lima x Centro
car_2 = "0.21." #Rua Camaragibe x Centro
truck_1 = "4.25." #Fernandes Lima x Centro
bus_1 = ["2.50.","2.500.","2.650.","2.750.","2.850.","2.950.","2.1050.","2.1550.","3.2150.","2.2250.","2.2500.","2.2600.","2.3650.","2.3750.","2.3900.","2.4000.","2.4100.","2.4400.","2.4700.","2.4800.","2.4900.","2.5000.","2.5250."] #Fernandes Lima x Centro
bus_2 = ["2.3050.","2.3500.","2.4650."] #Rua Camaragibe x Centro
# taxi_1 = "6.1000." #Fernandes Lima x Centro
# taxi_1 = "6.1041."  #Rua Camaragibe x Centro

    
# ARRAY CAR
array_completo_car_mean_duration = []
array_completo_car_mean_waiting_time = []
array_completo_car_mean_emissions_co2 = []
array_completo_car_mean_emissions_fuel = []
array_sem_semaforo_manual_car_mean_duration = []
array_sem_semaforo_manual_car_mean_waiting_time = []
array_sem_semaforo_manual_car_mean_emissions_co2 = []
array_sem_semaforo_manual_car_mean_emissions_fuel = []
array_sem_faixa_azul_car_mean_duration = []
array_sem_faixa_azul_car_mean_waiting_time = []
array_sem_faixa_azul_car_mean_emissions_co2 = []
array_sem_faixa_azul_car_mean_emissions_fuel = []
array_sem_faixa_azul_sem_semaforo_manual_car_mean_duration = []
array_sem_faixa_azul_sem_semaforo_manual_car_mean_waiting_time = []
array_sem_faixa_azul_sem_semaforo_manual_car_mean_emissions_co2 = []
array_sem_faixa_azul_sem_semaforo_manual_car_mean_emissions_fuel = []

# ARRAY TRUCK
array_completo_truck_mean_duration = []
array_completo_truck_mean_waiting_time = []
array_completo_truck_mean_emissions_co2 = []
array_completo_truck_mean_emissions_fuel = []
array_sem_semaforo_manual_truck_mean_duration = []
array_sem_semaforo_manual_truck_mean_waiting_time = []
array_sem_semaforo_manual_truck_mean_emissions_co2 = []
array_sem_semaforo_manual_truck_mean_emissions_fuel = []
array_sem_faixa_azul_truck_mean_duration = []
array_sem_faixa_azul_truck_mean_waiting_time = []
array_sem_faixa_azul_truck_mean_emissions_co2 = []
array_sem_faixa_azul_truck_mean_emissions_fuel = []
array_sem_faixa_azul_sem_semaforo_manual_truck_mean_duration = []
array_sem_faixa_azul_sem_semaforo_manual_truck_mean_waiting_time = []
array_sem_faixa_azul_sem_semaforo_manual_truck_mean_emissions_co2 = []
array_sem_faixa_azul_sem_semaforo_manual_truck_mean_emissions_fuel = []

# ARRAY BUS
array_completo_bus_mean_duration = []
array_completo_bus_mean_waiting_time = []
array_completo_bus_mean_emissions_co2 = []
array_completo_bus_mean_emissions_fuel = []
array_sem_semaforo_manual_bus_mean_duration = []
array_sem_semaforo_manual_bus_mean_waiting_time = []
array_sem_semaforo_manual_bus_mean_emissions_co2 = []
array_sem_semaforo_manual_bus_mean_emissions_fuel = []
array_sem_faixa_azul_bus_mean_duration = []
array_sem_faixa_azul_bus_mean_waiting_time = []
array_sem_faixa_azul_bus_mean_emissions_co2 = []
array_sem_faixa_azul_bus_mean_emissions_fuel = []
array_sem_faixa_azul_sem_semaforo_manual_bus_mean_duration = []
array_sem_faixa_azul_sem_semaforo_manual_bus_mean_waiting_time = []
array_sem_faixa_azul_sem_semaforo_manual_bus_mean_emissions_co2 = []
array_sem_faixa_azul_sem_semaforo_manual_bus_mean_emissions_fuel = []


for j in range (len(scenery)):               
    for i in range (qtdSeed):        
        fileOutput = "output." + scenery[j] + ".seed" + str(i+1) + ".tripinfo.csv"
        dataframe1 = pl.read_csv(fileOutput, delimiter=";", usecols= ['tripinfo_id','tripinfo_depart','tripinfo_arrival','tripinfo_duration','tripinfo_waitingTime','tripinfo_vType','emissions_CO2_abs','emissions_fuel_abs'], header=0)
        '''   
        print("\n-------------------------------------------------------")
        print("CENÁRIO: ", scenery[j], " Seed: ", str(i+1))
        print("-------------------------------------------------------")
        '''
        
        # ---------- CAR- ------------ CAR ---------------- CAR ----------------- CAR ---------------- CAR ------------------------
        # Selecao de carros que completam todo o percuso da Fernandes Lima
        result_car = dataframe1[(dataframe1.tripinfo_depart>899) & \
                                (dataframe1.tripinfo_arrival<4500) & \
                                (dataframe1.tripinfo_vType == "passenger") & \
                                ((dataframe1.tripinfo_id.str.startswith(car_1)) | (dataframe1.tripinfo_id.str.startswith(car_2)))]               
        # Loop para criar os array com as medias das 30 sementes
        if scenery[j] == "completo":
            array_completo_car_mean_duration.append(result_car["tripinfo_duration"].mean())
            array_completo_car_mean_waiting_time.append(result_car["tripinfo_waitingTime"].mean())   
            array_completo_car_mean_emissions_co2.append(result_car["emissions_CO2_abs"].mean())   
            array_completo_car_mean_emissions_fuel.append(result_car["emissions_fuel_abs"].mean())   
        elif scenery[j] == "sem-semaforo-manual": 
            array_sem_semaforo_manual_car_mean_duration.append(result_car["tripinfo_duration"].mean())
            array_sem_semaforo_manual_car_mean_waiting_time.append(result_car["tripinfo_waitingTime"].mean())   
            array_sem_semaforo_manual_car_mean_emissions_co2.append(result_car["emissions_CO2_abs"].mean())   
            array_sem_semaforo_manual_car_mean_emissions_fuel.append(result_car["emissions_fuel_abs"].mean())   
        elif scenery[j] == "sem-faixa-azul": 
            array_sem_faixa_azul_car_mean_duration.append(result_car["tripinfo_duration"].mean())
            array_sem_faixa_azul_car_mean_waiting_time.append(result_car["tripinfo_waitingTime"].mean())   
            array_sem_faixa_azul_car_mean_emissions_co2.append(result_car["emissions_CO2_abs"].mean())   
            array_sem_faixa_azul_car_mean_emissions_fuel.append(result_car["emissions_fuel_abs"].mean())   
        elif scenery[j] == "sem-faixa-azul-sem-semaforo-manual": 
            array_sem_faixa_azul_sem_semaforo_manual_car_mean_duration.append(result_car["tripinfo_duration"].mean())
            array_sem_faixa_azul_sem_semaforo_manual_car_mean_waiting_time.append(result_car["tripinfo_waitingTime"].mean())   
            array_sem_faixa_azul_sem_semaforo_manual_car_mean_emissions_co2.append(result_car["emissions_CO2_abs"].mean())   
            array_sem_faixa_azul_sem_semaforo_manual_car_mean_emissions_fuel.append(result_car["emissions_fuel_abs"].mean())   
            
                            
        
        # ---------- TRUCK ------------ TRUCK -------------- TRUCK --------------- TRUCK -------------- TRUCK ------------------
        # Selecao de caminhões que completam todo o percuso da Fernandes Lima
        result_truck = dataframe1[(dataframe1.tripinfo_depart>899) & \
                                  (dataframe1.tripinfo_arrival<4500) & \
                                  (dataframe1.tripinfo_vType == "truck") & \
                                  (dataframe1.tripinfo_id.str.startswith(truck_1))]        
        if scenery[j] == "completo":
            array_completo_truck_mean_duration.append(result_truck["tripinfo_duration"].mean())
            array_completo_truck_mean_waiting_time.append(result_truck["tripinfo_waitingTime"].mean())   
            array_completo_truck_mean_emissions_co2.append(result_truck["emissions_CO2_abs"].mean())   
            array_completo_truck_mean_emissions_fuel.append(result_truck["emissions_fuel_abs"].mean())   
        elif scenery[j] == "sem-semaforo-manual": 
            array_sem_semaforo_manual_truck_mean_duration.append(result_truck["tripinfo_duration"].mean())
            array_sem_semaforo_manual_truck_mean_waiting_time.append(result_truck["tripinfo_waitingTime"].mean())   
            array_sem_semaforo_manual_truck_mean_emissions_co2.append(result_truck["emissions_CO2_abs"].mean())   
            array_sem_semaforo_manual_truck_mean_emissions_fuel.append(result_truck["emissions_fuel_abs"].mean())   
        elif scenery[j] == "sem-faixa-azul": 
            array_sem_faixa_azul_truck_mean_duration.append(result_truck["tripinfo_duration"].mean())
            array_sem_faixa_azul_truck_mean_waiting_time.append(result_truck["tripinfo_waitingTime"].mean())   
            array_sem_faixa_azul_truck_mean_emissions_co2.append(result_truck["emissions_CO2_abs"].mean())   
            array_sem_faixa_azul_truck_mean_emissions_fuel.append(result_truck["emissions_fuel_abs"].mean())   
        elif scenery[j] == "sem-faixa-azul-sem-semaforo-manual": 
            array_sem_faixa_azul_sem_semaforo_manual_truck_mean_duration.append(result_truck["tripinfo_duration"].mean())
            array_sem_faixa_azul_sem_semaforo_manual_truck_mean_waiting_time.append(result_truck["tripinfo_waitingTime"].mean())   
            array_sem_faixa_azul_sem_semaforo_manual_truck_mean_emissions_co2.append(result_truck["emissions_CO2_abs"].mean())   
            array_sem_faixa_azul_sem_semaforo_manual_truck_mean_emissions_fuel.append(result_truck["emissions_fuel_abs"].mean())   
        
               
        # ---------- BUS ------------ BUS -------------- BUS --------------- BUS -------------- BUS ------------------
        # Selecao de ônibus que completam todo o percuso da Fernandes Lima
        result_bus = dataframe1[(dataframe1.tripinfo_depart>899) & \
                                (dataframe1.tripinfo_arrival<4500) & \
                                (dataframe1.tripinfo_vType == "bus") & \
                                ((dataframe1.tripinfo_id.str.startswith(tuple(bus_1))) | (dataframe1.tripinfo_id.str.startswith(tuple(bus_2))))]        
        
        if scenery[j] == "completo":
            array_completo_bus_mean_duration.append(result_bus["tripinfo_duration"].mean())
            array_completo_bus_mean_waiting_time.append(result_bus["tripinfo_waitingTime"].mean())   
            array_completo_bus_mean_emissions_co2.append(result_bus["emissions_CO2_abs"].mean())   
            array_completo_bus_mean_emissions_fuel.append(result_bus["emissions_fuel_abs"].mean())   
        elif scenery[j] == "sem-semaforo-manual": 
            array_sem_semaforo_manual_bus_mean_duration.append(result_bus["tripinfo_duration"].mean())
            array_sem_semaforo_manual_bus_mean_waiting_time.append(result_bus["tripinfo_waitingTime"].mean())   
            array_sem_semaforo_manual_bus_mean_emissions_co2.append(result_bus["emissions_CO2_abs"].mean())   
            array_sem_semaforo_manual_bus_mean_emissions_fuel.append(result_bus["emissions_fuel_abs"].mean())   
        elif scenery[j] == "sem-faixa-azul": 
            array_sem_faixa_azul_bus_mean_duration.append(result_bus["tripinfo_duration"].mean())
            array_sem_faixa_azul_bus_mean_waiting_time.append(result_bus["tripinfo_waitingTime"].mean())   
            array_sem_faixa_azul_bus_mean_emissions_co2.append(result_bus["emissions_CO2_abs"].mean())   
            array_sem_faixa_azul_bus_mean_emissions_fuel.append(result_bus["emissions_fuel_abs"].mean())   
        elif scenery[j] == "sem-faixa-azul-sem-semaforo-manual": 
            array_sem_faixa_azul_sem_semaforo_manual_bus_mean_duration.append(result_bus["tripinfo_duration"].mean())
            array_sem_faixa_azul_sem_semaforo_manual_bus_mean_waiting_time.append(result_bus["tripinfo_waitingTime"].mean())   
            array_sem_faixa_azul_sem_semaforo_manual_bus_mean_emissions_co2.append(result_bus["emissions_CO2_abs"].mean())   
            array_sem_faixa_azul_sem_semaforo_manual_bus_mean_emissions_fuel.append(result_bus["emissions_fuel_abs"].mean())   
        
       
        
# Resultados Consolidados    
print("\n-------------------------------------------------------")
print("RESULTADOS CONSOLIDADOS")
print("-------------------------------------------------------\n")

print("CENÁRIO ATUAL")
print("-------------")
print ("CAR")
print ("mean_duration: ", round(np.mean(array_completo_car_mean_duration)/60, 2), "minutos")  
print ("mean_waiting_time: ", round(np.mean(array_completo_car_mean_waiting_time)/60, 2), "minutos")  
print ("mean_emissions_co2: ", round(np.mean(array_completo_car_mean_emissions_co2)*0.001, 2), "gramas")  
print ("mean_emissions_fuel: ", round(np.mean(array_completo_car_mean_emissions_fuel)*0.001, 2), "litros")  
print ("\n")
print ("TRUCK")    
print ("mean_duration: ", round(np.mean(array_completo_truck_mean_duration)/60, 2), "minutos")  
print ("mean_waiting_time: ", round(np.mean(array_completo_truck_mean_waiting_time)/60, 2), "minutos")  
print ("mean_emissions_co2: ", round(np.mean(array_completo_truck_mean_emissions_co2)*0.001, 2), "gramas")  
print ("mean_emissions_fuel: ", round(np.mean(array_completo_truck_mean_emissions_fuel)*0.001, 2), "litros")
print ("\n")    
print ("BUS")
print ("mean_duration: ", round(np.mean(array_completo_bus_mean_duration)/60, 2), "minutos")  
print ("mean_waiting_time: ", round(np.mean(array_completo_bus_mean_waiting_time)/60, 2), "minutos")  
print ("mean_emissions_co2: ", round(np.mean(array_completo_bus_mean_emissions_co2)*0.001, 2), "gramas")  
print ("mean_emissions_fuel: ", round(np.mean(array_completo_bus_mean_emissions_fuel)*0.001, 2), "litros")
print ("\n")

print("CENÁRIO SEM SEMÁFORO MANUAL")  
print("---------------------------")  
print ("CAR")    
print ("mean_duration: ", round(np.mean(array_sem_semaforo_manual_car_mean_duration)/60, 2), "minutos")  
print ("mean_waiting_time: ", round(np.mean(array_sem_semaforo_manual_car_mean_waiting_time)/60, 2), "minutos")  
print ("mean_emissions_co2: ", round(np.mean(array_sem_semaforo_manual_car_mean_emissions_co2)*0.001, 2), "gramas")  
print ("mean_emissions_fuel: ", round(np.mean(array_sem_semaforo_manual_car_mean_emissions_fuel)*0.001, 2), "litros")  
print ("\n")    
print ("TRUCK")    
print ("mean_duration: ", round(np.mean(array_sem_semaforo_manual_truck_mean_duration)/60, 2), "minutos")  
print ("mean_waiting_time: ", round(np.mean(array_sem_semaforo_manual_truck_mean_waiting_time)/60, 2), "minutos")  
print ("mean_emissions_co2: ", round(np.mean(array_sem_semaforo_manual_truck_mean_emissions_co2)*0.001, 2), "gramas")  
print ("mean_emissions_fuel: ", round(np.mean(array_sem_semaforo_manual_truck_mean_emissions_fuel)*0.001, 2), "litros")
print ("\n")    
print ("BUS")
print ("mean_duration: ", round(np.mean(array_sem_semaforo_manual_bus_mean_duration)/60, 2), "minutos")  
print ("mean_waiting_time: ", round(np.mean(array_sem_semaforo_manual_bus_mean_waiting_time)/60, 2), "minutos")  
print ("mean_emissions_co2: ", round(np.mean(array_sem_semaforo_manual_bus_mean_emissions_co2)*0.001, 2), "gramas")  
print ("mean_emissions_fuel: ", round(np.mean(array_sem_semaforo_manual_bus_mean_emissions_fuel)*0.001, 2), "litros")
print ("\n")

print("CENÁRIO SEM FAIXA AZUL")
print("----------------------")
print ("CAR")    
print ("mean_duration: ", round(np.mean(array_sem_faixa_azul_car_mean_duration)/60, 2), "minutos")  
print ("mean_waiting_time: ", round(np.mean(array_sem_faixa_azul_car_mean_waiting_time)/60, 2), "minutos")  
print ("mean_emissions_co2: ", round(np.mean(array_sem_faixa_azul_car_mean_emissions_co2)*0.001, 2), "gramas")  
print ("mean_emissions_fuel: ", round(np.mean(array_sem_faixa_azul_car_mean_emissions_fuel)*0.001, 2), "litros")  
print ("\n")    
print ("TRUCK")
print ("mean_duration: ", round(np.mean(array_sem_faixa_azul_truck_mean_duration)/60, 2), "minutos")  
print ("mean_waiting_time: ", round(np.mean(array_sem_faixa_azul_truck_mean_waiting_time)/60, 2), "minutos")  
print ("mean_emissions_co2: ", round(np.mean(array_sem_faixa_azul_truck_mean_emissions_co2)*0.001, 2), "gramas")  
print ("mean_emissions_fuel: ", round(np.mean(array_sem_faixa_azul_truck_mean_emissions_fuel)*0.001, 2), "litros")
print ("\n")    
print ("BUS")
print ("mean_duration: ", round(np.mean(array_sem_faixa_azul_bus_mean_duration)/60, 2), "minutos")  
print ("mean_waiting_time: ", round(np.mean(array_sem_faixa_azul_bus_mean_waiting_time)/60, 2), "minutos")  
print ("mean_emissions_co2: ", round(np.mean(array_sem_faixa_azul_bus_mean_emissions_co2)*0.001, 2), "gramas")  
print ("mean_emissions_fuel: ", round(np.mean(array_sem_faixa_azul_bus_mean_emissions_fuel)*0.001, 2), "litros")
print ("\n")

print("CENÁRIO SEM FAIXA AZUL E SEMÁFORO MANUAL")
print("----------------------------------------")
print ("CAR")    
print ("mean_duration: ", round(np.mean(array_sem_faixa_azul_sem_semaforo_manual_car_mean_duration)/60, 2), "minutos")  
print ("mean_waiting_time: ", round(np.mean(array_sem_faixa_azul_sem_semaforo_manual_car_mean_waiting_time)/60, 2), "minutos")  
print ("mean_emissions_co2: ", round(np.mean(array_sem_faixa_azul_sem_semaforo_manual_car_mean_emissions_co2)*0.001, 2), "gramas")  
print ("mean_emissions_fuel: ", round(np.mean(array_sem_faixa_azul_sem_semaforo_manual_car_mean_emissions_fuel)*0.001, 2), "litros")  
print ("\n")    
print ("TRUCK")    
print ("mean_duration: ", round(np.mean(array_sem_faixa_azul_sem_semaforo_manual_truck_mean_duration)/60, 2), "minutos")  
print ("mean_waiting_time: ", round(np.mean(array_sem_faixa_azul_sem_semaforo_manual_truck_mean_waiting_time)/60, 2), "minutos")  
print ("mean_emissions_co2: ", round(np.mean(array_sem_faixa_azul_sem_semaforo_manual_truck_mean_emissions_co2)*0.001, 2), "gramas")  
print ("mean_emissions_fuel: ", round(np.mean(array_sem_faixa_azul_sem_semaforo_manual_truck_mean_emissions_fuel)*0.001, 2), "litros")
print ("\n")    
print ("BUS")
print ("mean_duration: ", round(np.mean(array_sem_faixa_azul_sem_semaforo_manual_bus_mean_duration)/60, 2), "minutos")  
print ("mean_waiting_time: ", round(np.mean(array_sem_faixa_azul_sem_semaforo_manual_bus_mean_waiting_time)/60, 2), "minutos")  
print ("mean_emissions_co2: ", round(np.mean(array_sem_faixa_azul_sem_semaforo_manual_bus_mean_emissions_co2)*0.001, 2), "gramas")  
print ("mean_emissions_fuel: ", round(np.mean(array_sem_faixa_azul_sem_semaforo_manual_bus_mean_emissions_fuel)*0.001, 2), "litros")
print ("\n")


#headers = ['tripinfo_arrival', 'tripinfo_arrivalLane', 'tripinfo_arrivalPos', 'tripinfo_arrivalSpeed', 'tripinfo_depart', 
#           'tripinfo_departDelay', 'tripinfo_departLane', 'tripinfo_departPos', 'tripinfo_departSpeed', 'tripinfo_devices', 
#           'tripinfo_duration', 'tripinfo_id', 'tripinfo_rerouteNo', 'tripinfo_routeLength', 'tripinfo_speedFactor', 'tripinfo_stopTime', 
#           'tripinfo_timeLoss', 'tripinfo_vType', 'tripinfo_vaporized', 'tripinfo_waitingCount', 'tripinfo_waitingTime', 'emissions_CO2_abs', 
#           'emissions_CO_abs', 'emissions_HC_abs', 'emissions_NOx_abs', 'emissions_PMx_abs', 'emissions_electricity_abs', 'emissions_fuel_abs' ]

# id = O nome do veículo que é descrito por esta entrada.
# depart = A hora real de partida (a hora em que o veículo foi inserido na rede).
# departLane = O id da pista em que o veículo iniciou sua jornada.
# departPos = A posição na pista em que o veículo iniciou sua jornada.
# departSpeed =  A velocidade com que o veículo iniciou a sua viagem.
# departDelay = O tempo que o veículo teve que esperar antes de iniciar sua jornada.
# arrival = A hora em que o veículo chegou ao seu destino.
# arrivalLane = A identificação da pista em que o veículo estava ao chegar ao seu destino.
# arrivalPos = A posição na pista em que o veículo estava ao chegar ao destino.
# arrivalSpeed = A velocidade que o veículo tinha ao chegar ao destino.
# duration = O tempo que o veículo precisou para realizar a rota.
# routeLength =  A extensão do percurso do veículo.
# waitingTime = O tempo em que a velocidade do veículo foi inferior ou igual a 0,1 m/s ( paradas programadas não contam).
# waitingCount = número de episódios em espera.
# stopTime = A hora em que o veículo estava fazendo uma parada planejada.
# timeLoss = O tempo perdido por dirigir abaixo da velocidade ideal. (velocidade ideal inclui o speedFactor individual ; lentidão devido a interseções etc. resultarão em perda de tempo, as paradas programadas não contam).
# rerouteNo = O número em que o veículo foi redirecionado.
# devices = Lista de dispositivos que o veículo tinha. Cada dispositivo é separado dos outros por um ';'.
# vType = O tipo do veículo.
# speedFactor = O fator de velocidade individual do veículo (possivelmente extraído de uma distribuição de velocidade no início da simulação).
# vaporized = Se o veículo foi removido da simulação antes de chegar ao seu destino.
# CO_abs = A quantidade total de CO emitida pelo veículo durante a viagem.
# CO2_abs = A quantidade total de CO 2 emitida pelo veículo durante a viagem.
# HC_abs = A quantidade total de HC emitida pelo veículo durante a viagem.
# PMx_abs = A quantidade total de PM x emitida pelo veículo durante a viagem.
# NOx_abs = A quantidade total de NO x emitida pelo veículo durante a viagem.
# fuel_abs = A quantidade total de combustível que o veículo usou durante a viagem.
