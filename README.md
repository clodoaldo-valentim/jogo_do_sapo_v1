# Jogo do Sapo - Pygame Basics

Um projeto educacional desenvolvido em **Python** utilizando a biblioteca **Pygame**. O objetivo deste jogo é servir como material de estudo para conceitos fundamentais de desenvolvimento de jogos, como o Game Loop, detecção de colisões, animação de sprites e manipulação de sons.

---

## Objetivo do Jogo

O jogador controla um sapo que deve caçar mosquitos para ganhar pontos.

* **Ganhe pontos:** Capture o mosquito no momento exato do ataque.
* **Perca pontos:** Evite comer as frutas (maçãs).
* **Vitória:** Alcance **10 pontos** antes que o tempo de **60 segundos** se esgote.

---

## Conceitos de Programação Aplicados

Este projeto demonstra a implementação de:

* **Game Loop:** O ciclo principal que processa eventos, atualiza a lógica e renderiza as imagens a 60 FPS.
* **POO (Sprites):** Uso de classes e herança (`pygame.sprite.Sprite`) para organizar objetos como o Sapo, Frutas e Mosquitos.
* **Sistema de Colisão:** Verificação de contato entre retângulos (`colliderect`) condicionada a frames específicos de animação.
* **Gerenciamento de Assets:** Carregamento e manipulação de imagens (PNG/JPG) e sons (MP3/WAV/OGG).
* **Interface Básica (UI):** Renderização de texto dinâmico para exibir pontuação e cronômetro em tempo real.

---

## Como Executar

### Pré-requisitos
* Python 3.x instalado.
* Biblioteca Pygame instalada.

pip install pygame
## Instalação
### Clone este repositório:
git clone [https://github.com/clodoaldo-valentim/jogo_do_sapo_v1.git](https://github.com/clodoaldo-valentim/jogo_do_sapo_v1.git)

Certifique-se de que as pastas de assets (sons/, sprites/, fundos/) estão no mesmo diretório que o arquivo .py.

## Execute o jogo:
python nome_do_arquivo.py
ControlesTeclaAçãoSetas DirecionaisMovimentam o sapo pela telaEspaçoRealiza o ataque (Lança a língua
## Estrutura de Arquivos Sugerida
Para que o código funcione corretamente, organize seus arquivos da seguinte forma:
.
### ├── jogo.py          # Seu código principal
### ├── sons/            # Música de fundo, coleta, vitória, derrota
### ├── sprites/         # Imagens do sapo, mosquito e maçã
### └── fundos/          # Imagens de fundo, tela de vitória e derrota
## Licença
Este projeto é para fins educacionais. Sinta-se à vontade para clonar, modificar e melhorar!
