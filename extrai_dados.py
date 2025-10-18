import pandas as pd
import re
import glob
import os

def extrair_dados_logs(diretorio_logs="Logs_Completos"):
 
    resultados = []
    

    miss_ratio_regex = re.compile(r"L1Cache\.miss_ratio\s+([\d\.]+)")
    cycles_regex = re.compile(r"total time required \(cycles\):\s+(\d+)")
    
    filename_regex = re.compile(r"log_assoc(\d+)_buf(\d+)_(\w+)\.txt")

    caminhos_logs = glob.glob(os.path.join(diretorio_logs, "*.txt"))
    
    if not caminhos_logs:
        print(f"ERRO: Nenhum arquivo .txt encontrado em '{diretorio_logs}'.")
        return None

    print(f"Encontrados {len(caminhos_logs)} arquivos de log. Processando...")

    for caminho_arquivo in caminhos_logs:
        
        nome_arquivo = os.path.basename(caminho_arquivo)
        match_name = filename_regex.search(nome_arquivo)
        
        if not match_name:
            print(f"Aviso: Nome de arquivo ignorado (padrão incorreto): {nome_arquivo}")
            continue

        assoc = int(match_name.group(1))
        buffer_size = int(match_name.group(2))
        access_type = match_name.group(3)
        
        miss_ratio = None
        cycles = None

        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Erro ao ler o arquivo {nome_arquivo}: {e}")
            continue

        match_miss = miss_ratio_regex.search(content)
        if match_miss:
            miss_ratio = float(match_miss.group(1))

        match_cycles = cycles_regex.search(content)
        if match_cycles:
            cycles = int(match_cycles.group(1))

        resultados.append({
            'Associatividade': assoc,
            'Buffer_Size': buffer_size,
            'Tipo_Acesso': access_type,
            'Miss_Ratio': miss_ratio,
            'Total_Cycles': cycles
        })

    df = pd.DataFrame(resultados)
    df['Buffer_Size_KB'] = (df['Buffer_Size'] / 1024).astype(int)
    
    output_csv = "Dados_e_Graficos/resultados_simulacao.csv"
    
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    
    df.to_csv(output_csv, index=False)
    print(f"\nSucesso! Dados extraídos e salvos em: {output_csv}")
    
    return df

extrair_dados_logs()