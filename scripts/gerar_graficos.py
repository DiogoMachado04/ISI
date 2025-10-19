import json
import matplotlib.pyplot as plt
import os

# --- Diretoria base (onde o script está localizado) ---
base_dir = os.path.dirname(os.path.abspath(__file__))

# --- Caminhos fixos para os ficheiros JSON ---
input_dir = os.path.join(base_dir, '..', 'data', 'output')
json_files = [
    ("grafico_hoteis.json", "grafico_hoteis"),
    ("grafico_clientes.json", "grafico_clientes")
]

print("Script iniciado")


# --- Diretoria de saída ---
output_dir = os.path.join(base_dir, '..','graficos')
os.makedirs(output_dir, exist_ok=True)

# --- Função para gerar gráfico ---
def gerar_grafico(json_path, chart_name):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # O formato esperado é lista com 1 objeto
    if isinstance(data, list) and len(data) > 0:
        data = data[0]

    labels = data.get("labels", [])
    values = data.get("data", [[]])[0] if data.get("data") else []

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color="skyblue")
    plt.title(f"{data.get('series', [chart_name])[0]}")
    plt.xlabel("Clientes / Hotéis")
    plt.ylabel("Total (€)")
    plt.xticks(rotation=45, ha="right")

    output_path = os.path.join(output_dir, f"{chart_name}.png")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Gráfico criado: {output_path}")

# --- Gerar gráficos para ambos os ficheiros ---
for filename, chart_name in json_files:
    json_path = os.path.join(input_dir, filename)
    if os.path.exists(json_path):
        gerar_grafico(json_path, chart_name)
    else:
        print(f"Ficheiro não encontrado: {json_path}")

print(f"\nTodos os gráficos foram gerados em: {output_dir}")

