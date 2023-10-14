{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
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
        "<a href=\"https://colab.research.google.com/github/GisstHubana/FHIR_Reporting_Tool/blob/GisstHubana-patch-2/flaskblog.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Flask Einleitungscode"
      ],
      "metadata": {
        "id": "Cb5Fc9S9eJBl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from flask import Flask\n",
        "\n",
        "app = Flask(__name__)\n",
        "\n",
        "@app.route(\"/\")\n",
        "def hello_world():\n",
        "    return \"<p>Hello, World!</p>\""
      ],
      "metadata": {
        "id": "Tr0nCipFePCE"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}