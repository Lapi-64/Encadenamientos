def forward_chaining():
    # 1. Base de Hechos Iniciales (Simulación de entrada del usuario)
    # Cambia estos valores para probar diferentes resultados
    hechos = {
        "morgana_en_equipo_rival": False,
        "muchos_ataques_basicos": False,
        "enemigo_feed_es_adc": False,
        "hay_mucho_cc": False, # Se actualizará por reglas
        "daño_predominante_ap": False
    }

    # 2. Base de Reglas (7 reglas definidas)
    # Cada regla es una función que añade un hecho si se cumple la condición
    conclusiones_extraidas = True
    
    while conclusiones_extraidas:
        conclusiones_extraidas = False
        
        # Regla 1: El requisito específico de Morgana
        if hechos.get("morgana_en_equipo_rival") and "cc_alto" not in hechos:
            hechos["cc_alto"] = True
            print("[Regla 1] Morgana detectada -> CC Alto.")
            conclusiones_extraidas = True

        # Regla 2: CC Alto implica necesidad de Tenacidad
        if hechos.get("cc_alto") and "necesita_tenacidad" not in hechos:
            hechos["necesita_tenacidad"] = True
            print("[Regla 2] CC Alto -> Se necesita Tenacidad.")
            conclusiones_extraidas = True

        # Regla 3: Muchos ataques básicos implican reducción de daño físico
        if hechos.get("muchos_ataques_basicos") and "necesita_reduccion_fisica" not in hechos:
            hechos["necesita_reduccion_fisica"] = True
            print("[Regla 3] Muchos ataques básicos -> Se necesita reducción física.")
            conclusiones_extraidas = True

        # Regla 4: Enemigo Fed es ADC implica daño físico crítico
        if hechos.get("enemigo_feed_es_adc") and "amenaza_fisica_alta" not in hechos:
            hechos["amenaza_fisica_alta"] = True
            print("[Regla 4] ADC enemigo Fed -> Amenaza física alta.")
            conclusiones_extraidas = True

        # Regla 5: Daño AP predominante implica resistencia mágica
        if hechos.get("daño_predominante_ap") and "necesita_mr" not in hechos:
            hechos["necesita_mr"] = True
            print("[Regla 5] Daño AP predominante -> Se necesita Resistencia Mágica (MR).")
            conclusiones_extraidas = True

        # Regla 6: Lógica para Botas de Acero (Plated Steelcaps)
        if (hechos.get("necesita_reduccion_fisica") or hechos.get("amenaza_fisica_alta")) \
           and "comprar_botas_acero" not in hechos:
            hechos["comprar_botas_acero"] = True
            conclusiones_extraidas = True

        # Regla 7: Lógica para Botas Mercuriales (Mercury's Treads)
        if (hechos.get("necesita_tenacidad") or hechos.get("necesita_mr")) \
           and "comprar_mercuriales" not in hechos:
            hechos["comprar_mercuriales"] = True
            conclusiones_extraidas = True

    # 3. Resultado Final
    print("\n--- Resultado de la Inferencia ---")
    if hechos.get("comprar_mercuriales") and hechos.get("comprar_botas_acero"):
        print("Recomendación: Situación mixta, pero prioriza Mercuriales si el CC te impide jugar.")
    elif hechos.get("comprar_mercuriales"):
        print("Recomendación: Comprar Botas Mercuriales.")
    elif hechos.get("comprar_botas_acero"):
        print("Recomendación: Comprar Botas de Acero.")
    else:
        print("Recomendación: Botas de Hechicero o Jonias (no hay amenaza clara de CC o AD).")

if __name__ == "__main__":
    forward_chaining()