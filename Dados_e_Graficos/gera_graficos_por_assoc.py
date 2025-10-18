import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def gerar_graficos_por_associatividade(csv_path="Dados_e_Graficos/resultados_simulacao.csv"):
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"ERRO: Arquivo CSV não encontrado em {csv_path}. Verifique o caminho.")
        return

    df['Buffer_Size_KB'] = (df['Buffer_Size'] / 1024).astype(int)
    
    associatividades = sorted(df['Associatividade'].unique())
    
    print("Iniciando geração dos 8 gráficos, um par para cada Associatividade...")

    
    for assoc in associatividades:
        
        df_filtered = df[df['Associatividade'] == assoc]
        title_prefix = f'Associatividade {assoc}-way:'
        
        # --- Gráfico 1: Miss Ratio ---
        plt.figure(figsize=(10, 6))
        # Hue é o Tipo de Acesso (Sequential vs Random)
        sns.lineplot(data=df_filtered, x='Buffer_Size_KB', y='Miss_Ratio', hue='Tipo_Acesso', markers=True, dashes=False)
        plt.title(f'{title_prefix} Miss Ratio vs. Buffer Size')
        plt.xlabel('Buffer Size (KB)')
        plt.ylabel('Miss Ratio')

        buffer_points_kb = [8, 16, 32, 64, 128]
        plt.xticks(buffer_points_kb)

        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend(title='Padrão de Acesso')
        plt.savefig(f'Dados_e_Graficos/miss_ratio_assoc{assoc}.png')
        plt.close()
        print(f"Gráfico 'miss_ratio_assoc{assoc}.png' salvo.")

        # --- Gráfico 2: Tempo Total (Cycles) ---
        plt.figure(figsize=(10, 6))

        sns.lineplot(data=df_filtered, x='Buffer_Size_KB', y='Total_Cycles', hue='Tipo_Acesso', markers=True, dashes=False)
        plt.title(f'{title_prefix} Tempo Total (Ciclos) vs. Buffer Size')
        plt.xlabel('Buffer Size (KB)')
        plt.ylabel('Tempo Total (Ciclos)')

        buffer_points_kb = [8, 16, 32, 64, 128]
        plt.xticks(buffer_points_kb)

        plt.yscale('log')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend(title='Padrão de Acesso')
        plt.savefig(f'Dados_e_Graficos/cycles_assoc{assoc}.png')
        plt.close()
        print(f"Gráfico 'cycles_assoc{assoc}.png' salvo.")

    print("\nTodos os 8 gráficos por Associatividade foram gerados com sucesso na pasta Dados_e_Graficos!")

gerar_graficos_por_associatividade()