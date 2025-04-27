# 🌬️ Wind-Optimizer: Plataforma de Otimização de Parques Eólicos Offshore

**Tecnologia:** Simulação de turbulência fractal + algoritmo genético  
**Clientes-Alvo:** EDP Renováveis, Ørsted, Iberdrola  
**Precisão:** Aumento de 25% na eficiência energética  

![Demo](https://via.placeholder.com/800x400.png?text=Simulação+de+Turbulência+WindOptimizer)

## 📦 Instalação Completa

### Pré-requisitos
- Python 3.10+
- NVIDIA GPU (recomendado para simulações grandes)
- CUDA 12.0+ (opcional para aceleração GPU)

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/wind-optimizer.git
cd wind-optimizer

# Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale dependências
pip install -r requirements.txt

# Para suporte a GPU (opcional)
pip install cupy-cuda12x
