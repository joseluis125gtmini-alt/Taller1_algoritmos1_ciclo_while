def modulo_telemetria():

    total_km = 0.0
    total_galones = 0.0
    mejor_rendimiento = 0.0
    tanqueos_validos = 0
    tanqueos_extra = 0
    

    while True:
        entrada_galones = input ()

        if not entrada_galones: break
        galones = float(entrada_galones)
        
        if galones == 0:
            break
            
        kilometros = float(input())
        while True:
            octanaje = int(input())
                           
            if 81 <= octanaje <= 98:
                break
            else:
                print("OCTANAJE INVALIDO")
        
        rendimiento_actual = kilometros / galones
        
        total_km += kilometros
        total_galones += galones
        tanqueos_validos += 1
        

        if rendimiento_actual > mejor_rendimiento:
            mejor_rendimiento = rendimiento_actual
    
        if octanaje >= 90:
            tanqueos_extra += 1

    if tanqueos_validos > 0:
        promedio_total = total_km / total_galones
        porcentaje_extra = (tanqueos_extra / tanqueos_validos) * 100
        
        print(f"AVG: {promedio_total:.2f}")
        print(f"BEST: {mejor_rendimiento:.2f}")
        print(f"EXTRA: {porcentaje_extra:.2f}%")

if __name__ == "__main__":
  modulo_telemetria()


