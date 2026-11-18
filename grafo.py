import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

datos_vias = [
    ("CA_Fusagasuga", "PBA_Fusagasuga", 12, 15, 25),
    ("CA_Fusagasuga", "UPA_ASPROAGRO", 28, 35, 14),
    ("CA_Fusagasuga", "UPA_ASOTRASIL", 18, 22, 20),
    ("UPA_ASPROAGRO", "UPA_SANBERPAS", 34, 45, 10),
    ("UPA_ASOTRASIL", "UPA_ASOGRANADINOS", 20, 25, 18),
    ("UPA_ASOGRANADINOS", "UPA_AGROSOACHA", 32, 40, 22),
    ("UPA_AGROSOACHA", "CA_Mosquera", 26, 35, 28),
    ("CA_Fusagasuga", "CA_Girardot", 68, 75, 28),
    ("CA_Girardot", "PBA_Girardot", 10, 12, 25),
    ("CA_Girardot", "CA_LaMesa", 58, 70, 18),
    ("CA_LaMesa", "CA_Mosquera", 45, 55, 20),
    ("CA_LaMesa", "UPA_ASOPROFRUT", 30, 40, 12),
    ("UPA_ASOPROFRUT", "CA_Facatativa", 28, 38, 14),
    ("CA_Mosquera", "PBA_Mosquera", 8, 10, 30),
    ("CA_Mosquera", "CA_Facatativa", 24, 30, 28),
    ("CA_Mosquera", "PBA_Chia", 38, 50, 25),
    ("PBA_Chia", "CA_Zipaquira", 22, 28, 26),
    ("CA_Zipaquira", "PBA_Zipaquira", 9, 12, 25),
    ("CA_Zipaquira", "CA_Ubate", 48, 55, 22),
    ("CA_Ubate", "PBA_Ubate", 10, 12, 24),
    ("CA_Zipaquira", "UPA_ASOPAPA_CHOCONTA", 42, 50, 20),
    ("UPA_ASOPAPA_CHOCONTA", "CA_Ubate", 46, 58, 16),
    ("UPA_AGROSOACHA", "UPA_ASOPROCHIPA", 44, 60, 15),
    ("UPA_ASOPROCHIPA", "CA_Caqueza", 22, 30, 18),
]

for u, v, flete, tiempo, ton in datos_vias:
    G.add_edge(u, v, weight=round(0.6 * flete + 0.4 * tiempo, 2), max_ton=ton)

def buscar_ruta(origen, destino, carga):
    sub = G.edge_subgraph([(u, v) for u, v, d in G.edges(data=True) if d["max_ton"] >= carga])
    if origen in sub and destino in sub and nx.has_path(sub, origen, destino):
        return nx.dijkstra_path(sub, origen, destino, weight="weight"), round(nx.dijkstra_path_length(sub, origen, destino, weight="weight"), 2)
    return None, "Sin ruta disponible"

print(f"Nodos: {G.number_of_nodes()} | Aristas: {G.number_of_edges()} | Conexo: {nx.is_connected(G)}")
ruta1, costo1 = buscar_ruta("CA_Ubate", "UPA_SANBERPAS", 10)
print("Caso 1 (Ubaté -> San Bernardo, 10t):", ruta1, costo1)
ruta2, costo2 = buscar_ruta("CA_Girardot", "CA_Facatativa", 22)
print("Caso 2 (Girardot -> Facatativá, 22t):", ruta2, costo2)
print("Caso 3 (Fusagasugá -> San Bernardo, 16t):", buscar_ruta("CA_Fusagasuga", "UPA_SANBERPAS", 16))
print("Nodos críticos:", list(nx.articulation_points(G)))
print("Puentes:", list(nx.bridges(G)))

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
colores = ["royalblue" if n.startswith("CA_") else "tomato" if n.startswith("PBA_") else "mediumseagreen" for n in G.nodes()]

nx.draw(G, pos, with_labels=True, node_color=colores, node_size=1100, font_size=8, edge_color="lightgray")
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, "weight"), font_size=7)

if ruta1 is not None:
    aristas_ruta1 = list(zip(ruta1[:-1], ruta1[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=aristas_ruta1, edge_color="orange", width=3)
    plt.title("Circuito de Maquinaria y Centros de Acopio (Ruta Caso 1 en naranja)")
else:
    plt.title("Circuito de Maquinaria y Centros de Acopio")

plt.show()