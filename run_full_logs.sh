#!/bin/bash

ACCESS_COUNT=10000000
STRIDE=8192
WRITE_RATIO=50
OUTPUT_DIR="Logs_Completos"


XML_FILES=("assoc_1.xml" "assoc_2.xml" "assoc_4.xml" "assoc_8.xml")
#              8KB     16KB    32KB    64KB    128KB 
BUFFER_SIZES=("8192" "16384" "32768" "65536" "131072")
ACCESS_TYPES=("sequential" "random")

echo "Iniciando 40 simulações. Logs completos serão salvos em $OUTPUT_DIR/..."
echo "Pode demorar um pouco. Aguarde..."
echo "--------------------------------------------------------"


for XML in "${XML_FILES[@]}"; do
    ASSOC=$(echo "$XML" | cut -d'_' -f2 | cut -d'.' -f1)
    
    for BUF_SIZE in "${BUFFER_SIZES[@]}"; do
        

        OUTPUT_NAME="${OUTPUT_DIR}/log_assoc${ASSOC}_buf${BUF_SIZE}_sequential.txt"
        COMMAND_SEQ="./cache-sim.exe XML_Configs/$XML sequential $ACCESS_COUNT $BUF_SIZE $STRIDE $WRITE_RATIO"
        echo "Executando SEQ: $OUTPUT_NAME"
        $COMMAND_SEQ > "$OUTPUT_NAME"
        

        OUTPUT_NAME="${OUTPUT_DIR}/log_assoc${ASSOC}_buf${BUF_SIZE}_random.txt"
        COMMAND_RAND="./cache-sim.exe XML_Configs/$XML random $ACCESS_COUNT $BUF_SIZE $WRITE_RATIO"
        echo "Executando RAND: $OUTPUT_NAME"
        $COMMAND_RAND > "$OUTPUT_NAME"
            
    done
done

echo "--------------------------------------------------------"
echo "Todos os logs foram salvos na pasta $OUTPUT_DIR."