#Quantos segundos há em 42 minutos e 42 segundos?
# resultado
print(42 * 60 + 42)
# %%
# Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.
print(10 / 1.61)

# Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?

print(f"Passo médio: {int((42*60+42) / (10 / 1.61) // 60)} minutos e {int((42*60+42) / (10 / 1.61) % 60)} segundos por milha.")
print(f"Velocidade média: {10 / 1.61 / ((42*60+42) / 3600):.2f} milhas por hora.")

