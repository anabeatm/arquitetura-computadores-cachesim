import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_graficos_simulacao(csv_path="Dados_e_Graficos/resultados_simulacao.csv"):
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"ERRO: Arquivo CSV não encontrado em {csv_path}. Execute 'extrai_dados.py' primeiro.")
        return


    buffer_points_kb = [8, 16, 32, 64, 128]

    df['Associatividade'] = df['Associatividade'].astype(str)
    
    plt.figure(figsize=(12, 7))
    sns.lineplot(
        data=df, 
        x='Buffer_Size_KB', 
        y='Miss_Ratio', 
        hue='Associatividade', 
        style='Tipo_Acesso',
        markers=True,
        dashes=False
    )
    plt.title('Miss Ratio vs. Buffer Size')
    plt.xlabel('Buffer Size (KB)')
    plt.ylabel('Miss Ratio')
    

    plt.xticks(buffer_points_kb)
    
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(title='Assoc. / Tipo Acesso')
    plt.savefig('Dados_e_Graficos/miss_ratio_vs_buffer_size.png')
    plt.close()
    print("Gráfico 'miss_ratio_vs_buffer_size.png' salvo com sucesso!")

    # --- Gráfico 2: Total Cycles vs. Buffer Size (Tempo Total) ---
    plt.figure(figsize=(12, 7))
    sns.lineplot(
        data=df, 
        x='Buffer_Size_KB', 
        y='Total_Cycles', 
        hue='Associatividade', 
        style='Tipo_Acesso',
        markers=True,
        dashes=False
    )
    plt.title('Tempo Total (Ciclos) vs. Buffer Size')
    plt.xlabel('Buffer Size (KB)')
    plt.ylabel('Tempo Total (Ciclos)')
    
    plt.xticks(buffer_points_kb)

    if df['Total_Cycles'].max() > 1000000:
        plt.yscale('log')
        plt.ylabel('Tempo Total (Ciclos, Escala Log)')
    
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(title='Assoc. / Tipo Acesso')
    plt.savefig('Dados_e_Graficos/total_cycles_vs_buffer_size.png')
    plt.close()
    print("Gráfico 'total_cycles_vs_buffer_size.png' salvo com sucesso!")


gerar_graficos_simulacao()