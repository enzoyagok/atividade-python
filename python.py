{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPlrrOwC3FaphbVs4l1BQUg",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/enzoyagok/atividade-python/blob/main/atividade_python.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Sistema de Acesso ao Laboratório:** *Basico 1*🟢"
      ],
      "metadata": {
        "id": "2xq75AqiUwHs"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fjjtbDupUruX",
        "outputId": "5bcc3999-c0a7-465a-b055-a0f38d691372"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite sua idade: 15\n",
            "Você pode entrar S/N: s\n",
            "Entrada Negada\n"
          ]
        }
      ],
      "source": [
        "\n",
        "idade = int(input(\"Digite sua idade: \"))\n",
        "pode = (input(\"Você pode entrar S/N: \"))\n",
        "\n",
        "if (idade >= 16) and (pode == \"S\"):\n",
        "  print(\"Entrada permitida\")\n",
        "elif (idade >= 15) and (pode == \"S\") and (pode == \"N\"):\n",
        "  print(\"Entrada Negada\")\n",
        "else:\n",
        "  print(\"Entrada Negada\")"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Sistema de Acesso ao Laboratório:** *Médio 2*🟡"
      ],
      "metadata": {
        "id": "uQfHk2qGZJcT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "idade = int(input(\"Digite sua idade: \"))\n",
        "pode = (input(\"Você pode entrar S/N: \"))\n",
        "\n",
        "if idade >= 18:\n",
        "  print(\"Entrada Permitida\")\n",
        "elif idade >= 16 and pode == \"S\":\n",
        "  print(\"Entrada Permitida com Autorização\")\n",
        "else:\n",
        "  print(\"Entrada Negada\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lTXyRqXQY8a0",
        "outputId": "de7e8007-1fb0-4fb5-83bb-8b33ff01de6d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite sua idade: 18\n",
            "Você pode entrar S/N: S\n",
            "Entrada Permitida\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Sistema de Acesso ao Laboratório:** *Alto 3*🔴"
      ],
      "metadata": {
        "id": "qCJZDmORhId0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "hora = int(input(\"Digite o horário (0-22): \"))\n",
        "idade = int(input(\"Digite sua idade: \"))\n",
        "pode = (input(\"Você pode entrar S/N: \"))\n",
        "\n",
        "\n",
        "if hora >= 22 or hora < 6:\n",
        "  print(\"Entrada Negada: laboratório esta fechado 22 e as 6\")\n",
        "\n",
        "\n",
        "if (idade >= 18) and (pode == \"S\"):\n",
        "  print(\"Entrada Direta\")\n",
        "elif idade >= 19:\n",
        "  print(\"Entrada Direta\")\n",
        "else:\n",
        "  print(\"Entrada Permitida\")\n",
        "\n",
        "\n",
        "if  (idade >=  16) and (idade >= 18) and (pode == \"S\"):\n",
        "  print(\"\")\n",
        "elif (idade >= 17) and (pode == \"S\") and (pode == \"N\"):\n",
        "  print(\"com autorização\")\n",
        "else:\n",
        "  print(\"com autorização\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qUlsEYPphICU",
        "outputId": "3279802b-567a-4d58-bb5e-f67345e423d8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o horário (0-22): 5\n",
            "Digite sua idade: 19\n",
            "Você pode entrar S/N: S\n",
            "Entrada Negada: laboratório fecha as 22\n",
            "Entrada Direta\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        " **Sistema de Pontuação de Jogo:** *Basico 1*🟢"
      ],
      "metadata": {
        "id": "YuHXblvkjJN_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "pontos = int(input(\"Digite sua pontuação: \"))\n",
        "\n",
        "if pontos >= 100:\n",
        "  print(f\"Nivel avançado {pontos} pts\")\n",
        "else:\n",
        "  print(f\"Nivel iniciante {pontos} pts\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vn30fPAsji4I",
        "outputId": "43d59c7a-7dc0-477c-cb6d-08af6500bba1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite sua pontuação100\n",
            "Nivel avançado\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Sistema de Pontuação de Jogo:** *Médio 2*  🟡"
      ],
      "metadata": {
        "id": "OwyCg7UmkbKG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "pontos = int(input(\"Digite sua pontuação: \"))\n",
        "\n",
        "if pontos >= 200:\n",
        "  print(f\"Elite {pontos} pts\")\n",
        "elif pontos >= 100:\n",
        "    print(f\"Intermediário {pontos} pts\")\n",
        "else:\n",
        " print(f\"Iniciante {pontos} pts\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UyucsOyOkkRN",
        "outputId": "a8ac1781-8a8b-4546-9479-acffcb8fa15d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite sua pontuação: 100\n",
            "Inetermediario 100 pts\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Sistema de Pontuação de Jogo:** *Alto 3*  🔴"
      ],
      "metadata": {
        "id": "vObfGVVVljcj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "pontos = int(input(\"Digite sua pontuação: \"))\n",
        "\n",
        "if pontos < 0:\n",
        "  print(\"Error: inválido\")\n",
        "elif pontos == 150:\n",
        "  print(f\"Bônus especial {pontos} pts\")\n",
        "elif pontos >= 200:\n",
        "  print(f\"Elite {pontos} pts\")\n",
        "elif pontos >= 100:\n",
        "  print(f\"Intermediário {pontos} pts\")\n",
        "else:\n",
        " print(f\"Iniciante {pontos} pts\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wt1RKN7wlvCk",
        "outputId": "b73fbc8a-86bf-4dd1-bdb2-58779168f769"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite sua pontuação: -10\n",
            "Error: inválido\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Sistema de Pontuação de Jogo:** *Avançado⚫*"
      ],
      "metadata": {
        "id": "KZCndocxSdAZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print('='*50)\n",
        "\n",
        "pontos = int(input(\"Digite a sua pontuação: \"))\n",
        "\n",
        "\n",
        "if pontos < 0:\n",
        "    print(\"Erro: pontuação inválida\")\n",
        "elif pontos >= 300:\n",
        "  print(f\"Nível: Monstro, Você fez {pontos} pts! Impossivel!\")\n",
        "elif pontos >= 150:\n",
        "    print(f\"Nível: Mestre, Você fez {pontos} pts! Absurdo!\")\n",
        "elif pontos >= 200:\n",
        "    print(f\"Nível: Elite, Você fez {pontos} pts! Incrivel!\")\n",
        "elif pontos >= 100:\n",
        "    print(f\"Nível: Intermediário, Você fez {pontos} pts Uau!\")\n",
        "else:\n",
        "    print(f\"Nível: Iniciante Você fez {pontos} pts. Melhore!\")\n",
        "\n",
        "print('='*50)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "H_HOh203SjiZ",
        "outputId": "22ad7cca-187d-4026-8ca6-6ca75b4c764d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "==================================================\n",
            "Digite a sua pontuação: 100\n",
            "Nível: Intermediário, Você fez 100 pts Uau!\n",
            "==================================================\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Sistema de Compra com Desconto:** *Básico 1*  🟢"
      ],
      "metadata": {
        "id": "etPA1-xin9sf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "preco = (float(input(\"1 Preço: \")) * int(input(\"Quantia 1: \"))) +\\\n",
        "        (float(input(\"2 Preço: \")) * int(input(\"Quantia 2: \"))) +\\\n",
        "        (float(input(\"3 Preço: \")) * int(input(\"Quantia 3: \"))) +\\\n",
        "        (float(input(\"4 Preço: \")) * int(input(\"Quantia 4: \"))) +\\\n",
        "        (float(input(\"5 Preço: \")) * int(input(\"Quantia 5: 1\")))\n",
        "\n",
        "\n",
        "if preco >= 100:\n",
        "   valor1 = preco * 0.90\n",
        "else:\n",
        "  valor1 = preco\n",
        "\n",
        "print(f\"Total: R$ {valor1:.2f}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ttcURGXSoTg2",
        "outputId": "1ef08d1e-32fb-409d-cd53-e7c45b51695b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 Preço: 10\n",
            "Quantia 1: 2\n",
            "2 Preço: 122\n",
            "Quantia 2: 122\n",
            "3 Preço: 212\n",
            "Quantia 3: 122\n",
            "4 Preço: 212\n",
            "Quantia 4: 12\n",
            "5 Preço: 12\n",
            "Quantia 5: 22\n",
            "Total: R$ 39218.40\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Sistema de Compra com Desconto:** *Médio*  🟡"
      ],
      "metadata": {
        "id": "maPm6sVjrb2m"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "preco = (float(input(\"1 Preço: \")) * int(input(\"Quantia 1: \"))) +\\\n",
        "        (float(input(\"2 Preço: \")) * int(input(\"Quantia 2: \"))) +\\\n",
        "        (float(input(\"3 Preço: \")) * int(input(\"Quantia 3: \"))) +\\\n",
        "        (float(input(\"4 Preço: \")) * int(input(\"Quantia 4: \"))) +\\\n",
        "        (float(input(\"5 Preço: \")) * int(input(\"Quantia 5: 1\")))\n",
        "\n",
        "\n",
        "if preco >= 200:\n",
        "   desconto = 0.20\n",
        "   tipo = \"Médio\"\n",
        "elif preco >= 100:\n",
        "   desconto = 0.10\n",
        "   tipo = \"Básico\"\n",
        "else:\n",
        "  desconto = 0\n",
        "  tipo = \"Nada (Sem desconto)\"\n",
        "\n",
        "valor1 = preco - (preco * desconto)\n",
        "print(f\"Cliente {tipo} - Total final: R$ {valor1:.2f}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VJtFsR1urbPf",
        "outputId": "07ef57d8-6129-446d-a04c-0aa69f2d0efe"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 Preço: 12\n",
            "Quantia 1: 2\n",
            "2 Preço: 1\n",
            "Quantia 2: 2\n",
            "3 Preço: 22\n",
            "Quantia 3: 2\n",
            "4 Preço: 111\n",
            "Quantia 4: 12\n",
            "5 Preço: 12\n",
            "Quantia 5: 12\n",
            "Cliente Médio - Total final: R$ 1140.80\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Sistema de Compra com Desconto:** *Alto*  🔴  "
      ],
      "metadata": {
        "id": "GFo0jTl-uO0y"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "preco1 = float(input(\"P1: \")) * int(input(\"Quantia: \"))\n",
        "preco2 = float(input(\"P2: \")) * int(input(\"Quantia: \"))\n",
        "preco3 = float(input(\"P3: \")) * int(input(\"Quantia: \"))\n",
        "preco4 = float(input(\"P4: \")) * int(input(\"Quantia: \"))\n",
        "preco5 = float(input(\"P5: \")) * int(input(\"Quantia: \"))\n",
        "\n",
        "valores = preco1 + preco2 + preco3 + preco4 + preco5\n",
        "vip = input(\"Tem VIP? (S/N): \")\n",
        "\n",
        "desconto = 0\n",
        "if valores >= 200: desconto = 0.20\n",
        "elif valores >= 100: desconto = 0.10\n",
        "\n",
        "if vip == \"S\" or vip == \"s\":\n",
        "  desconto += 0.05\n",
        "\n",
        "print(f\"Preço final: R$ {valores * (1 - desconto):.2f}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mI9P-3HNugfZ",
        "outputId": "48174eee-40ab-49c1-b2d0-c747f03036a9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "P1: 11\n",
            "Quantia: 2\n",
            "P2: 12\n",
            "Quantia: 1\n",
            "P3: 18\n",
            "Quantia: 2\n",
            "P4: 23\n",
            "Quantia: 2\n",
            "P5: 100\n",
            "Quantia: 2\n",
            "Tem VIP? (S/N): S\n",
            "Preço final: R$ 237.00\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Sistema de Compra com Desconto:** *Avançado⚫*"
      ],
      "metadata": {
        "id": "K_A0tQ9tSPdx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "total = (float(input(\"1 Preço: \")) * int(input(\"1 Qtd: \"))) + \\\n",
        "        (float(input(\"2 Preço: \")) * int(input(\"2 Qtd: \"))) + \\\n",
        "        (float(input(\"3 Preço: \")) * int(input(\"3 Qtd: \"))) + \\\n",
        "        (float(input(\"4 Preço: \")) * int(input(\"4 Qtd: \"))) + \\\n",
        "        (float(input(\"5 Preço: \")) * int(input(\"5 Qtd: \")))\n",
        "\n",
        "if total >= 200:\n",
        "    desconto, tipo = 0.20, \"Alto\"\n",
        "elif total >= 100:\n",
        "    desconto, tipo = 0.10, \"Médio\"\n",
        "else:\n",
        "    desconto, tipo = 0.00, \"Básico\"\n",
        "\n",
        "vip = input(\"\\nCliente VIP? (S/N): \")\n",
        "if vip == \"S\" or vip == \"s\":\n",
        "    desconto += 0.05\n",
        "    status = \"Ativado\"\n",
        "else:\n",
        "    status = \"Desativado\"\n",
        "\n",
        "valor = total* (1 - desconto)\n",
        "\n",
        "print(f\"\\n{'>'*30}\")\n",
        "print(f\"Total: R$ {total:.2f} | Tipo: {tipo}\")\n",
        "print(f\"VIP: {status} | Desconto: {desconto * 100:.0f}%\")\n",
        "print(f\"Valor final: R$ {valor:.2f}\")\n",
        "print('<'*30)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2-WGrEqNVJfs",
        "outputId": "28c5f428-d192-4f15-8c8f-f6c237cf2e7f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 Preço: 1\n",
            "1 Qtd: 1\n",
            "2 Preço: 1\n",
            "2 Qtd: 1\n",
            "3 Preço: 1\n",
            "3 Qtd: 1\n",
            "4 Preço: 1\n",
            "4 Qtd: 1\n",
            "5 Preço: 1\n",
            "5 Qtd: 1\n",
            "\n",
            "Cliente VIP? (S/N): S\n",
            "\n",
            ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n",
            "Total: R$ 5.00 | Tipo: Básico\n",
            "VIP: Ativado | Desconto: 5%\n",
            "Valor final: R$ 4.75\n",
            "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Monitoramento de Temperetura:**  *Básico 1*  🟢"
      ],
      "metadata": {
        "id": "-buGW663uOHD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "temperatura = float(input(\"Temperatura do servidor: \"))\n",
        "\n",
        "if temperatura >= 70:\n",
        "  print(\"Situação: Alerta\")\n",
        "else:\n",
        "  print(\"Situação: Normal\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xxRT8vUbu6RE",
        "outputId": "c438748c-b778-4a89-fde3-45224e07b2a0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Temperatura do servidor: 100\n",
            "Situação: Alerta\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Monitoramento de Temperetura:** *Médio*  🟡"
      ],
      "metadata": {
        "id": "UAAlLKjOwQc2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "temperatura = float(input(\"Temperatura do servidor: \"))\n",
        "\n",
        "if temperatura >= 90:\n",
        "    print(\"Situação: Crítico\")\n",
        "elif temperatura >= 70:\n",
        "    print(\"Situação: Alerta\")\n",
        "else:\n",
        "    print(\"Situação: Normal\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "InFOzqh-wI1f",
        "outputId": "710d7ede-d99e-48de-d750-2b5518cbe98f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Temperatura do servidor: 190\n",
            "Situação: Crítico\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Monitoramento de Temperetura:** *Alto*  🔴"
      ],
      "metadata": {
        "id": "as5Luog_w4oV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "temperatura = float(input(\"Temperatura do servidor: \"))\n",
        "\n",
        "if temperatura < 0:\n",
        "  print(\"Situação: Erro no sensor\")\n",
        "elif temperatura >= 90:\n",
        "  print(\"Situação: Crítico\")\n",
        "elif temperatura >= 70:\n",
        "  print(\"Situação: Alerta\")\n",
        "else:\n",
        "  print(\"Situação: Normal\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bLPU6ooBxLeo",
        "outputId": "a24b6929-6051-4d56-bafd-69c71d413209"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Temperatura do servidor: -1\n",
            "Situação: Erro no sensor\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Monitoramento de Temperetura:** *Avançado⚫*"
      ],
      "metadata": {
        "id": "HHCFevN3Q7F0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "temperatura = float(input(\"Digite a temperatura (°C): \"))\n",
        "\n",
        "if temperatura < 0:\n",
        "    status = \"Sensor com erro\"\n",
        "    ideia = \"Verifique-o novamente\"\n",
        "elif temperatura >= 90:\n",
        "    status = \"CRÍTICO\"\n",
        "    ideia = \"Desligue imediatamente!\"\n",
        "elif temperatura >= 70:\n",
        "    status = \"Alerta\"\n",
        "    ideia = \"Aumentar rotação dos coolers\"\n",
        "else:\n",
        "    status = \"Normal\"\n",
        "    ideia = \"Manter monitoramento padrão\"\n",
        "\n",
        "\n",
        "print(\"\\n\" + \"_\"*30)\n",
        "print(f\"RELATÓRIO DE MONITORAMENTO\")\n",
        "print(f\"Temperatura: {temperatura}°C\")\n",
        "print(f\"Status: {status}\")\n",
        "print(f\"Ideia sugerida: {ideia}\")\n",
        "print(\"_\"*30)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LUM8VwQVSRhR",
        "outputId": "17dd809d-4813-4fa6-d922-54fe4d6ce490"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a temperatura (°C): 100\n",
            "\n",
            "______________________________\n",
            "RELATÓRIO DE MONITORAMENTO\n",
            "Temperatura: 100.0°C\n",
            "Status: CRÍTICO\n",
            "Ideia sugerida: Desligue imediatamente!\n",
            "______________________________\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Avaliação de Projeto:**  *Básico 1*  🟢"
      ],
      "metadata": {
        "id": "Tr0oXaXhyYDq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "nota = float(input(\"Digite a sua nota: \"))\n",
        "\n",
        "\n",
        "if nota >= 7:\n",
        "    print(\"Aprovado\")\n",
        "else:\n",
        "    print(\"Reprovado\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yUH_SHN2ym_S",
        "outputId": "a3457353-ee99-4ce2-8502-c10635408848"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a sua nota: 4\n",
            "Reprovado\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Avaliação de Projeto:** *Médio*  🟡"
      ],
      "metadata": {
        "id": "GsR4gmzFNM9c"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "nota = float(input(\"Digite a sua nota: \"))\n",
        "\n",
        "\n",
        "if nota >= 9:\n",
        "    print(\"Aprovado com excelência\")\n",
        "elif nota >= 7:\n",
        "    print(\"Aprovado\")\n",
        "else:\n",
        "    print(\"Reprovado\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SbrD87RgNglE",
        "outputId": "d69fac21-eb80-4713-f45a-a2a43dd44ee0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a sua nota: 10\n",
            "Aprovado com excelência\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Avaliação de Projeto:** *Alto*  🔴"
      ],
      "metadata": {
        "id": "ubh-jkmXNyAa"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "nota = float(input(\"Digite a sua nota (0-10): \"))\n",
        "\n",
        "\n",
        "if nota > 10 or nota < 0:\n",
        "    print(\"Nota inválida\")\n",
        "elif nota == 10:\n",
        "    print(\"Projeto destaque da turma\")\n",
        "elif nota >= 9:\n",
        "    print(\"Aprovado com excelência\")\n",
        "elif nota >= 7:\n",
        "    print(\"Aprovado\")\n",
        "else:\n",
        "    print(\"Reprovado\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "59FQqyuHN41a",
        "outputId": "662a5977-a491-44e3-cacb-00b42b0b2dc7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a sua nota (0-10): 11\n",
            "Nota inválida\n"
          ]
        }
      ]
    }
  ]
}
