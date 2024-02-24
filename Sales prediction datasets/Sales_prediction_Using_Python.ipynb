{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "BHK4db86O0ml"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "import warnings\n",
        "warnings.filterwarnings(\"ignore\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "q5BAMyjyPM9g",
        "outputId": "333b2ce1-7a04-4392-bd80-a4b515b4fbe3"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Unnamed: 0     TV  radio  newspaper  sales\n",
              "0           1  230.1   37.8       69.2   22.1\n",
              "1           2   44.5   39.3       45.1   10.4\n",
              "2           3   17.2   45.9       69.3    9.3\n",
              "3           4  151.5   41.3       58.5   18.5\n",
              "4           5  180.8   10.8       58.4   12.9"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-ce083f5e-909d-410b-bf66-476a628d8b97\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Unnamed: 0</th>\n",
              "      <th>TV</th>\n",
              "      <th>radio</th>\n",
              "      <th>newspaper</th>\n",
              "      <th>sales</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>230.1</td>\n",
              "      <td>37.8</td>\n",
              "      <td>69.2</td>\n",
              "      <td>22.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>44.5</td>\n",
              "      <td>39.3</td>\n",
              "      <td>45.1</td>\n",
              "      <td>10.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>17.2</td>\n",
              "      <td>45.9</td>\n",
              "      <td>69.3</td>\n",
              "      <td>9.3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>151.5</td>\n",
              "      <td>41.3</td>\n",
              "      <td>58.5</td>\n",
              "      <td>18.5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>180.8</td>\n",
              "      <td>10.8</td>\n",
              "      <td>58.4</td>\n",
              "      <td>12.9</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-ce083f5e-909d-410b-bf66-476a628d8b97')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-ce083f5e-909d-410b-bf66-476a628d8b97 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-ce083f5e-909d-410b-bf66-476a628d8b97');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-7f93c618-da97-4174-8135-b2edad3f6eb7\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-7f93c618-da97-4174-8135-b2edad3f6eb7')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-7f93c618-da97-4174-8135-b2edad3f6eb7 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 200,\n  \"fields\": [\n    {\n      \"column\": \"Unnamed: 0\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 57,\n        \"min\": 1,\n        \"max\": 200,\n        \"num_unique_values\": 200,\n        \"samples\": [\n          96,\n          16,\n          31\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"TV\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 85.85423631490808,\n        \"min\": 0.7,\n        \"max\": 296.4,\n        \"num_unique_values\": 190,\n        \"samples\": [\n          287.6,\n          286.0,\n          78.2\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"radio\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 14.846809176168724,\n        \"min\": 0.0,\n        \"max\": 49.6,\n        \"num_unique_values\": 167,\n        \"samples\": [\n          8.2,\n          36.9,\n          44.5\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"newspaper\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 21.778620838522826,\n        \"min\": 0.3,\n        \"max\": 114.0,\n        \"num_unique_values\": 172,\n        \"samples\": [\n          22.3,\n          5.7,\n          17.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"sales\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 5.217456565710478,\n        \"min\": 1.6,\n        \"max\": 27.0,\n        \"num_unique_values\": 121,\n        \"samples\": [\n          11.4,\n          21.2,\n          12.9\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 2
        }
      ],
      "source": [
        "df=pd.read_csv(\"/content/Advertising.csv\")\n",
        "df.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kPQ6iLiHPZTT",
        "outputId": "5899bbf9-e4d3-44bf-dc7b-50e606e2b6dc"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(200, 5)"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ],
      "source": [
        "df.shape"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "zFhNOwjoPi42",
        "outputId": "795354d6-4b37-47f1-b061-cda23d4e3c3f"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "       Unnamed: 0          TV       radio   newspaper       sales\n",
              "count  200.000000  200.000000  200.000000  200.000000  200.000000\n",
              "mean   100.500000  147.042500   23.264000   30.554000   14.022500\n",
              "std     57.879185   85.854236   14.846809   21.778621    5.217457\n",
              "min      1.000000    0.700000    0.000000    0.300000    1.600000\n",
              "25%     50.750000   74.375000    9.975000   12.750000   10.375000\n",
              "50%    100.500000  149.750000   22.900000   25.750000   12.900000\n",
              "75%    150.250000  218.825000   36.525000   45.100000   17.400000\n",
              "max    200.000000  296.400000   49.600000  114.000000   27.000000"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-10c960cd-0543-4e10-a814-3345daefdea8\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Unnamed: 0</th>\n",
              "      <th>TV</th>\n",
              "      <th>radio</th>\n",
              "      <th>newspaper</th>\n",
              "      <th>sales</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>200.000000</td>\n",
              "      <td>200.000000</td>\n",
              "      <td>200.000000</td>\n",
              "      <td>200.000000</td>\n",
              "      <td>200.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>100.500000</td>\n",
              "      <td>147.042500</td>\n",
              "      <td>23.264000</td>\n",
              "      <td>30.554000</td>\n",
              "      <td>14.022500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>57.879185</td>\n",
              "      <td>85.854236</td>\n",
              "      <td>14.846809</td>\n",
              "      <td>21.778621</td>\n",
              "      <td>5.217457</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.700000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.300000</td>\n",
              "      <td>1.600000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>50.750000</td>\n",
              "      <td>74.375000</td>\n",
              "      <td>9.975000</td>\n",
              "      <td>12.750000</td>\n",
              "      <td>10.375000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>100.500000</td>\n",
              "      <td>149.750000</td>\n",
              "      <td>22.900000</td>\n",
              "      <td>25.750000</td>\n",
              "      <td>12.900000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>150.250000</td>\n",
              "      <td>218.825000</td>\n",
              "      <td>36.525000</td>\n",
              "      <td>45.100000</td>\n",
              "      <td>17.400000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>200.000000</td>\n",
              "      <td>296.400000</td>\n",
              "      <td>49.600000</td>\n",
              "      <td>114.000000</td>\n",
              "      <td>27.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-10c960cd-0543-4e10-a814-3345daefdea8')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-10c960cd-0543-4e10-a814-3345daefdea8 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-10c960cd-0543-4e10-a814-3345daefdea8');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-0bbbea95-085a-40bf-9f54-a13037576015\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-0bbbea95-085a-40bf-9f54-a13037576015')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-0bbbea95-085a-40bf-9f54-a13037576015 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 8,\n  \"fields\": [\n    {\n      \"column\": \"Unnamed: 0\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 71.77644232399086,\n        \"min\": 1.0,\n        \"max\": 200.0,\n        \"num_unique_values\": 6,\n        \"samples\": [\n          200.0,\n          100.5,\n          150.25\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"TV\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 93.12930693433862,\n        \"min\": 0.7,\n        \"max\": 296.4,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          147.0425,\n          149.75,\n          200.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"radio\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 64.62946191825954,\n        \"min\": 0.0,\n        \"max\": 200.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          23.264000000000006,\n          22.9,\n          200.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"newspaper\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 67.53295876114069,\n        \"min\": 0.3,\n        \"max\": 200.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          30.553999999999995,\n          25.75,\n          200.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"sales\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 66.68380930502316,\n        \"min\": 1.6,\n        \"max\": 200.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          14.0225,\n          12.9,\n          200.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 4
        }
      ],
      "source": [
        "df.describe()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uLGSCrFSPncv",
        "outputId": "e4f118c4-a064-4b20-f61d-6ccdd03fc68f"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Unnamed: 0', 'TV', 'radio', 'newspaper', 'sales']"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ],
      "source": [
        "df.columns.values.tolist()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "huchbN2nXV_m",
        "outputId": "21a8c5c2-2f0c-4a14-e31a-19552e57232a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 200 entries, 0 to 199\n",
            "Data columns (total 5 columns):\n",
            " #   Column      Non-Null Count  Dtype  \n",
            "---  ------      --------------  -----  \n",
            " 0   Unnamed: 0  200 non-null    int64  \n",
            " 1   TV          200 non-null    float64\n",
            " 2   radio       200 non-null    float64\n",
            " 3   newspaper   200 non-null    float64\n",
            " 4   sales       200 non-null    float64\n",
            "dtypes: float64(4), int64(1)\n",
            "memory usage: 7.9 KB\n"
          ]
        }
      ],
      "source": [
        "df.info()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "odNOEgpwXbTP",
        "outputId": "444e4d17-8892-407f-e0cb-dd4a2f170c2a"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Unnamed: 0    0\n",
              "TV            0\n",
              "radio         0\n",
              "newspaper     0\n",
              "sales         0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ],
      "source": [
        "df.isnull().sum()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 506
        },
        "id": "FU72TXx2XpcV",
        "outputId": "f094f25c-0403-4aaa-db1a-3098491fad36"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 500x500 with 3 Axes>"
            ],
            "image/png": "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365JkybpL3/5i95//3298sorcjqdOuecc/Tzn/9c99xzj+677z7FxcVZ8dYAAAgLo75HffSrR0lJSZKkyspKtba2KjMzM3DMqFGj5HK5VFFRIUmqqKjQ2WefHbRgICsrSz6fT++99143pgcAIPyMWUzW3t6uO+64QxdeeKHGjh0rSXK73YqLi1NiYmLQsU6nU263O3DMV1f1HX189Jivam5uVnPz/33NyefzhettAAAQVsbMqHNzc7Vnzx5t2LAh4q9VVFQkh8MR2FJTUyP+mgAAhMKIop43b542bdqk1157TaeddlpgPDk5WS0tLWpoaAg63uPxKDk5OXDMV1eBH3189Jivys/Pl9frDWy1tbVhfDcAAISPpUXt9/s1b948Pffcc3r11Vc1bNiwoP0TJkxQv379VF5eHhjbt2+fampqlJGRIUnKyMjQu+++qwMHDgSO2bx5s+x2u8aMGdPh69psNtnt9qANAAATWXqOOjc3V6WlpXr++eeVkJAQOKfscDjUv39/ORwOzZ49W3l5eUpKSpLdbtf8+fOVkZGhSZMmSZIuvfRSjRkzRjfccIMeeughud1uLVq0SLm5ubLZbFa+PQAAuszSol61apUkaerUqUHjTz31lH784x9Lkh5++GHFxsYqOztbzc3NysrK0sqVKwPH9unTR5s2bdItt9yijIwMDRgwQDNnztTSpUu7620AABAxlhb1idwPJD4+XsXFxSouLj7uMWlpafrzn/8czmgAABjBiMVkAACgYxQ1AAAGo6gBADAYRQ0AgMEoagAADEZRAwBgMIoaAACDUdQAABjshIv6hz/8ocrKyk7oIiUAACA8Trio//nPf+rKK6+Uy+XSkiVLtH///kjmAgAA6kRRl5eXa//+/Zo9e7bWrVunESNGaNq0aSotLVVzc3MkMwIA0Gt16hx1Wlqa7rvvPu3fv1+bN29WSkqK5syZo6FDhyo3N1eVlZWRygkAQK8U8mKyadOmad26dXK73SoqKtKGDRuUnp4ezmwAAPR6Xbp7VlVVldasWaM1a9bI6/UqMzMzXLkAAIBCmFE3NTVp3bp1mjZtmkaMGKG1a9dq9uzZqqqqUllZWSQyAgDQa53wjHrnzp168skn9cwzz6ipqUk/+MEPVFZWposvvlgxMTGRzIh/EXu4weoIAGC0aPt38oSLetKkSRo/frx+/vOfKycn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\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "fig, axs=plt.subplots(3, figsize=(5,5))\n",
        "plt1= sns.boxplot(df['TV'], ax=axs[0])\n",
        "plt2= sns.boxplot(df['newspaper'], ax=axs[1])\n",
        "plt3= sns.boxplot(df['radio'], ax=axs[2])\n",
        "plt.tight_layout()\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 466
        },
        "id": "dE3aSXTpak2Q",
        "outputId": "ef042369-4f3d-4d18-d000-2c445c139d91"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: xlabel='newspaper', ylabel='Density'>"
            ]
          },
          "metadata": {},
          "execution_count": 9
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAlEAAAGwCAYAAACJjDBkAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABvw0lEQVR4nO3deVxU9f4/8NcszAzrsDOAoLjigoCoiJlacsWya6SVmqXXS3nrqlncFu3mUt2bqVlmejVb1L7p1exnXjO1CC0rcQNRcSFXUNllGRiWgZnz+wOZnESFETgzw+v5eMxDOecz57w/kzkvP+dzPkciCIIAIiIiImoWqdgFEBEREdkihigiIiIiCzBEEREREVmAIYqIiIjIAgxRRERERBZgiCIiIiKyAEMUERERkQXkYhdgz4xGI3JycuDq6gqJRCJ2OURERNQEgiCgvLwcAQEBkEpvPd7EENWKcnJyEBQUJHYZREREZIHLly+jQ4cOt9zPENWKXF1dAdT/R3BzcxO5GiIiImoKrVaLoKAg0/f4rTBEtaKGS3hubm4MUURERDbmTlNxOLGciIiIyAIMUUREREQWYIgiIiIisgBDFBEREZEFGKKIiIiILMAQRURERGQBhigiIiIiCzBEEREREVmAIYqIiIjIAgxRRERERBZgiCIiIiKyAEMUERERkQUYooiIiIgswBBFREREZAGGKCIiIiILyMUugMgSGw9mi3LeJ6KDRTkvERFZH45EEREREVmAIYqIiIjIAgxRRERERBZgiCIiIiKyAEMUERERkQUYooiIiIgswBBFREREZAGGKCIiIiILMEQRERERWcAqQtTKlSvRqVMnqFQqREdH49ChQ7dtv2XLFoSGhkKlUiEsLAw7d+407autrcWrr76KsLAwODs7IyAgAJMnT0ZOTo7ZMYqLizFp0iS4ubnB3d0dCQkJqKioMGtz/Phx3HvvvVCpVAgKCsLixYtbrtNERERk00QPUZs3b0ZiYiLmz5+PtLQ0hIeHIy4uDgUFBY22379/PyZOnIiEhAQcPXoU8fHxiI+PR0ZGBgCgsrISaWlpmDt3LtLS0rB161ZkZmZizJgxZseZNGkSTp48iaSkJOzYsQP79u3DtGnTTPu1Wi1GjhyJjh07IjU1FUuWLMGCBQuwZs2a1vswiIiIyGZIBEEQxCwgOjoaAwYMwIoVKwAARqMRQUFBmDlzJmbPnn1T+/Hjx0On02HHjh2mbYMGDUJERARWr17d6DkOHz6MgQMHIisrC8HBwTh9+jR69eqFw4cPo3///gCA3bt348EHH8SVK1cQEBCAVatW4Z///Cfy8vKgUCgAALNnz8a2bdtw5syZRs9TU1ODmpoa089arRZBQUEoKyuDm5ubZR8QNYrPziMiotai1WqhVqvv+P0t6kiUXq9HamoqYmNjTdukUiliY2ORkpLS6HtSUlLM2gNAXFzcLdsDQFlZGSQSCdzd3U3HcHd3NwUoAIiNjYVUKsXBgwdNbYYOHWoKUA3nyczMRElJSaPnWbhwIdRqtekVFBR0+w+AiIiIbJaoIaqoqAgGgwF+fn5m2/38/JCXl9foe/Ly8prVvrq6Gq+++iomTpxoSpN5eXnw9fU1ayeXy+Hp6Wk6zq3O07CvMXPmzEFZWZnpdfny5UbbERERke2Ti11Aa6qtrcXjjz8OQRCwatWqVj+fUqmEUqls9fMQERGR+EQNUd7e3pDJZMjPzzfbnp+fD41G0+h7NBpNk9o3BKisrCzs2bPH7JqmRqO5aeJ6XV0diouLTce51Xka9hEREVH7JurlPIVCgaioKCQnJ5u2GY1GJCcnIyYmptH3xMTEmLUHgKSkJLP2DQHq7Nmz+OGHH+Dl5XXTMUpLS5GammratmfPHhiNRkRHR5va7Nu3D7W1tWbn6dGjBzw8PCzvNBEREdkF0Zc4SExMxMcff4z169fj9OnTeO6556DT6TB16lQAwOTJkzFnzhxT+1mzZmH37t1YunQpzpw5gwULFuDIkSOYMWMGgPoA9eijj+LIkSPYsGEDDAYD8vLykJeXB71eDwDo2bMnRo0ahWeeeQaHDh3Cr7/+ihkzZmDChAkICAgAADzxxBNQKBRISEjAyZMnsXnzZnzwwQdITExs40+IiIiIrJHoc6LGjx+PwsJCzJs3D3l5eYiIiMDu3btNk7izs7Mhlf6e9QYPHoyNGzfi9ddfx2uvvYZu3bph27Zt6NOnDwDg6tWr2L59OwAgIiLC7Fx79+7F8OHDAQAbNmzAjBkzMGLECEilUowbNw7Lly83tVWr1fj+++8xffp0REVFwdvbG/PmzTNbS4qIiIjaL9HXibJnTV1ngpqP60QREVFrsYl1ooiIiIhsFUMUERERkQUYooiIiIgswBBFREREZAGGKCIiIiILMEQRERERWYAhioiIiMgCDFFEREREFmCIIiIiIrIAQxQRERGRBRiiiIiIiCzAEEVERERkAYYoIiIiIgswRBERERFZQC52AUT2zGgUoNPXQVdjgJujHE4K/i9HRGQv+Dc6UQu7WlqFbUevYt9vhUjLLkGtQTDt83NToqe/G+J6azCylx+8XJQiVkpERHeDIYqohRRV1GDl3nPYcCAbeoPRbJ9MKoHBKCBfW4N8bSF+zCzE3G0ZeCQyEDPu74qOXs4iVU1ERJZiiCJqAfvPF2H6hjSUVNYCAAaGeOKhvv4Y0tUbAe6OUMql0FbV4UJRBfafv4ZdGbnIuKrFltQr2Hr0Kp6MDsbLo0LhouT/kkREtoJ/YxPdpfX7L+HNHadgMAoI1bji9dG9cE9XL0gkErN2aicHRAZ7IDLYA9Pv64q07BJ8mHwWezMLsT4lCz+cLsCicX0xpJu3SD0hIqLm4N15RHfhk58vYP72kzAYBTwSGYht0+/BkG7eNwWoxvQL9sDaqQPxRUI0Ong44mppFZ767CBW7j0HQRDu+H4iIhIXQxSRhb49not/fXsaAPBibHe893g4VA6yZh9nSDdvfPfCUEwcGARBAJZ8l4npG9NQXWto6ZKJiKgFMUQRWSA1qwQvfpkOAJgS0xHPj+japNGnW3FWyrFwbF+8/UgYHGQS7DyRh6lrD6Oipq6FKiYiopbGEEXUTJX6Ory4OR36OiNG9vLDvD/3vqsAdaMnooPxfwnRcFHKkXLhGp769CDKqmpb5NhERNSyGKKImmnRrjPILq5EoLsjlj4eDpm0ZQJUg0GdvbDh6WioHR1wNLsUCesOo0rPS3tERNaGIYqoGfafL8L6lCwAwDvjwuCqcmiV84QHueO/zwyCm0qOI1klmL4xDbV/WHuKiIjExRBF1EQGo4DXt2UAACYODMa93Xxa9Xy9Atzw6V8GQCmXYs+ZArz+dQbv2iMisiIMUURNlJZdgguFOng6KzDnwdA2OeeATp74z6R+kEqAzUcuY/3+S21yXiIiujOGKKImqDUYkXw6HwAw/b6ucGuly3iNGdHTD6892BMA8Na3p/HruaI2OzcREd0aQxRRExy4cA3a6joEqFWYFB3c5udPGBKCsZGBMBgFzNiYhtyyqjavgYiIzDFEEd2Bvs6IHzMLAQAv/Km7RQtq3i2JRIK3x4ahT6AbSiprMWtTOgxGzo8iIhITQxTRHaRll6Cq1gBPZwXGRgaKVofKQYYPJ/aDs0KGQxeL8eGes6LVQkREVhCiVq5ciU6dOkGlUiE6OhqHDh26bfstW7YgNDQUKpUKYWFh2Llzp9n+rVu3YuTIkfDyqn8AbHp6utn+S5cuQSKRNPrasmWLqV1j+zdt2tRi/SbbYBQEpJy/BgAY3MULcpm4/8uEeDvj34+EAQCWJ5/FkUvFotZDRNSeifqNsHnzZiQmJmL+/PlIS0tDeHg44uLiUFBQ0Gj7/fv3Y+LEiUhISMDRo0cRHx+P+Ph4ZGRkmNrodDoMGTIEixYtavQYQUFByM3NNXu98cYbcHFxwQMPPGDWdu3atWbt4uPjW6zvZBvOF1SgsKIGSrkU/YI9xC4HABAfGYix/QJhFICXthzjQpxERCKRCCIuPBMdHY0BAwZgxYoVAACj0YigoCDMnDkTs2fPvqn9+PHjodPpsGPHDtO2QYMGISIiAqtXrzZre+nSJYSEhODo0aOIiIi4bR2RkZHo168fPv30U9M2iUSCr7/++q6Ck1arhVqtRllZGdzc3Cw+Dt1s48HsNjnP+v2XkJlfjpguXvhz3wA8IcKk8saUVdUi7v19yNNWY+o9nTD/z73FLomIyG409ftbtJEovV6P1NRUxMbG/l6MVIrY2FikpKQ0+p6UlBSz9gAQFxd3y/ZNkZqaivT0dCQkJNy0b/r06fD29sbAgQPx2Wef3XGhw5qaGmi1WrMX2a6iihpk5pdDAmBwZy+xyzGjdnTAokf7AgDW/noJBy5cE7kiIqL2R7QQVVRUBIPBAD8/P7Ptfn5+yMvLa/Q9eXl5zWrfFJ9++il69uyJwYMHm21/88038eWXXyIpKQnjxo3D3//+d3z44Ye3PdbChQuhVqtNr6CgIIvrIvGlZZUAALr7ucLLRSlyNTcb1t0HEwfW/xl7besJ1NTxsh4RUVuSi12AmKqqqrBx40bMnTv3pn03bouMjIROp8OSJUvw/PPP3/J4c+bMQWJioulnrVbLIGWjjIKA9CulAIDIYHfT9ra6jHij211CnPNgT/xwugAXinRY9eN5vBDbvQ0rIyJq30QbifL29oZMJkN+fr7Z9vz8fGg0mkbfo9FomtX+Tr766itUVlZi8uTJd2wbHR2NK1euoKam5pZtlEol3NzczF5km7KuVaK0shZKuRQ9/a33v6ObygELrs+H+s/e8zhfWCFyRURE7YdoIUqhUCAqKgrJycmmbUajEcnJyYiJiWn0PTExMWbtASApKemW7e/k008/xZgxY+Djc+cHyaanp8PDwwNKpfVd1qGWl365/lJen0A1HERe1uBOHgzT4L4ePtAbjJi7jQ8pJiJqK6JezktMTMSUKVPQv39/DBw4EMuWLYNOp8PUqVMBAJMnT0ZgYCAWLlwIAJg1axaGDRuGpUuXYvTo0di0aROOHDmCNWvWmI5ZXFyM7Oxs5OTkAAAyMzMB1I9i3Thide7cOezbt++mdaYA4JtvvkF+fj4GDRoElUqFpKQkvP3223jppZda7bMg61FrMOLE1TIAQESQu7jFNIFEIsGbD/fBiPd+wv7z1/D9qXzE9bZsdJaIiJpO1H9ijx8/Hu+++y7mzZuHiIgIpKenY/fu3abJ49nZ2cjNzTW1Hzx4MDZu3Ig1a9YgPDwcX331FbZt24Y+ffqY2mzfvh2RkZEYPXo0AGDChAmIjIy8aQmEzz77DB06dMDIkSNvqsvBwQErV65ETEwMIiIi8NFHH+G9997D/PnzW+NjICuTmVeO6loj1I4OCPF2FrucJgnydMK0ezsDAN7eeZqTzImI2oCo60TZO64T1Xpac4L3xkPZyLhahqHdvDGqj3+rnaepmro2la6mDve9+yMKymsw+4FQPDusSytXRkRkn6x+nSgia1RnMOK3/HIAQO8AtcjVNI+zUo5XRoUCAFbsOYfC8lvfBEFERHePIYroBheKdNDXGeGqkiPQw1HscpptbGQgwjuoUVFTh3e/yxS7HCIiu9au14ki+qNTufWrzPfUuEEqkYhcTb3mXroc1NkLx66U4csjl+HjqkSAe/PDoLU83oaIyJpxJIroOkEQcKYhRFnx2lB30tHLGX07qCEA2HE8l0seEBG1EoYoouuullZBW10HhVyKLj62cVferYzqrYGDTIJL13Sm0TUiImpZDFFE152+Hja6+bpAbuULbN6Ju5MC93T1BgB8fyofBiNHo4iIWpptf1MQtaAzefV35fWy4Ut5NxrazQeODjIUlteYVmAnIqKWwxBFBKC8uha5ZdWQAOju5yp2OS1C5SDD8B71jzT64XQBag1GkSsiIrIvDFFEgOnBvf7uKjgr7eem1UGdvaB2dEBZVS0OXiwWuxwiIrvCEEUE4FxBfYjq6uMiciUty0EmxYhQXwDAj5kFqK7l42CIiFoKQxS1e4Ig/B6ifO3jUt6NIoM94O2iRKXegF/OFYldDhGR3WCIonavsLwG2uo6yKUSdPRyErucFieTSjCyV/1DvX85W4SKmjqRKyIisg8MUdTunbs+H6qTlzMcbHxpg1vpHeCGQHdH6A1G7D1TIHY5RER2wT6/MYia4fdLefY1H+pGEokEcb01AIBDl4pRWqkXuSIiItvHEEXtmsEo4GKRDgDQxY5DFFAfEkO8nWEwCtibydEoIqK7xRBF7drV0irU1Bnh6CCDv1oldjmt7k896+dGpWaV4FpFjcjVEBHZNoYoateyrtWPQnXycoJUIhG5mtbXydsZ3f1cYBSAPZwbRUR0VxiiqF27dP1SXidv237gcHPEXh+NSr9cigJttcjVEBHZLoYoareMgoBL1yoB1N+Z11508HBCT383CACSORpFRGQxhihqtwrLa1BVa4CDTIIAd0exy2lTsT3rVzE/cbUMuWVVIldDRGSbGKKo3bp0fT5UkKcTZFL7nw91I3+1I8IC1QDqH05MRETNxxBF7ZZpPlQ7upR3oxE9fSEBcDpXiysllWKXQ0RkcxiiqN3KaofzoW7k66pCRJA7AOCH0/niFkNEZIMYoqhdKq3Uo7SqFlIJEOTZvuZD3ej+UF9IJcBv+RWmkTkiImoahihqlxruygtwd4RSLhO5GvF4uSgR1dETAJB0Oh+CIIhcERGR7WCIonbpcnF9iAr2dBK5EvHd18MHMqkEF4t0OF/I0SgioqZiiKJ26fL1idRBHgxR7k4KDOxUPxr1A0ejiIiajCGK2p06gxG5ZfUrdQdxJAoAMKyHDxxkEmQXV+K3/HKxyyEisgkMUdTu5JZVw2AU4KSQwcPJQexyrIKbygGDQrwAcG4UEVFTMURRu3PjpTxJO3jocFPd290HCrkUOaXV+O4klzwgIroThihqd66U1D/mpEM7XtqgMS5KOe7pUj8a9V5SJgxGjkYREd2O6CFq5cqV6NSpE1QqFaKjo3Ho0KHbtt+yZQtCQ0OhUqkQFhaGnTt3mu3funUrRo4cCS8vL0gkEqSnp990jOHDh0MikZi9nn32WbM22dnZGD16NJycnODr64uXX34ZdXV1d91fEl/DnXmcVH6zIV19oHKQ4rf8Cuw4niN2OUREVk3UELV582YkJiZi/vz5SEtLQ3h4OOLi4lBQ0PizvPbv34+JEyciISEBR48eRXx8POLj45GRkWFqo9PpMGTIECxatOi2537mmWeQm5trei1evNi0z2AwYPTo0dDr9di/fz/Wr1+PdevWYd68eS3TcRJNZU0drun0ABiiGuOokGFIVx8AwAc/nEWdwShyRURE1ksiiDiDNDo6GgMGDMCKFSsAAEajEUFBQZg5cyZmz559U/vx48dDp9Nhx44dpm2DBg1CREQEVq9ebdb20qVLCAkJwdGjRxEREWG2b/jw4YiIiMCyZcsarWvXrl146KGHkJOTAz8/PwDA6tWr8eqrr6KwsBAKhaJJ/dNqtVCr1SgrK4Obm1uT3kNNs/FgtkXv+y2/HOv2X4K3iwKJf+rRwlXZh5paA5bvOYuSylosebQvHusfJHZJRERtqqnf36KNROn1eqSmpiI2Nvb3YqRSxMbGIiUlpdH3pKSkmLUHgLi4uFu2v50NGzbA29sbffr0wZw5c1BZ+fsDWFNSUhAWFmYKUA3n0Wq1OHny5C2PWVNTA61Wa/Yi68JLeXemdJDhueFdAAAfJJ+Fvo6jUUREjREtRBUVFcFgMJgFFQDw8/NDXl5eo+/Jy8trVvtbeeKJJ/DFF19g7969mDNnDv7v//4PTz755B3P07DvVhYuXAi1Wm16BQXxX/DWpmFSeaAHJ5XfzlODOsHHVYkrJVX48shlscshIrJKok8sF8O0adMQFxeHsLAwTJo0CZ9//jm+/vprnD9//q6OO2fOHJSVlZlely/zy8fa5JRdvzPPnSHqdhwVMky/Phq1Ys85VNcaRK6IiMj6iBaivL29IZPJkJ9vvh5Nfn4+NBpNo+/RaDTNat9U0dHRAIBz587d9jwN+25FqVTCzc3N7EXWQ1tdi/LqOkgAaNQMUXcyMToYAWoV8rTVFs9BIyKyZ6KFKIVCgaioKCQnJ5u2GY1GJCcnIyYmptH3xMTEmLUHgKSkpFu2b6qGZRD8/f1N5zlx4oTZXYJJSUlwc3NDr1697upcJJ6c0vpRKB9XJRTydjkI2yxKuQwzR3QDAPznx3Oo1HOJDyKiG4n6TZKYmIiPP/4Y69evx+nTp/Hcc89Bp9Nh6tSpAIDJkydjzpw5pvazZs3C7t27sXTpUpw5cwYLFizAkSNHMGPGDFOb4uJipKen49SpUwCAzMxMpKenm+YynT9/Hm+99RZSU1Nx6dIlbN++HZMnT8bQoUPRt29fAMDIkSPRq1cvPPXUUzh27Bi+++47vP7665g+fTqUSmVbfTzUwhpCVCAv5TXZo1EdEOzphKIKPT5PyRK7HCIiqyJqiBo/fjzeffddzJs3DxEREUhPT8fu3btNk7izs7ORm5traj948GBs3LgRa9asQXh4OL766its27YNffr0MbXZvn07IiMjMXr0aADAhAkTEBkZaVoCQaFQ4IcffsDIkSMRGhqKf/zjHxg3bhy++eYb0zFkMhl27NgBmUyGmJgYPPnkk5g8eTLefPPNtvhYqJXklNY/dDiAIarJHGRSzLo+GrX6p/Mor64VuSIiIush6jpR9o7rRLUeS+boLN59BqVVtXjm3s4I8XZuharsxxPRwabfG4wCRr7/E84X6vBibHfMiu0mYmVERK3P6teJImpLupo6lFbVj6L4q1UiV2NbZFIJXvxTdwDAJz9fQGmlXuSKiIisA0MUtQsNSxt4OSugcpCJXI3tebCPP0I1riivqcPHP18QuxwiIqvAEEXtQs71RTY5H8oyUqkEiddHo9b+eglFFTUiV0REJD6GKGoXrpbVTyrnnXmW+1MvP/TtoEal3oDVP97dwrRERPaAIYrahYblDTgSZTmJ5PfRqP87kIV8bbXIFRERiYshiuxeda0Bxbr6ydCcVH53hnX3Qf+OHqipM2Ll3nNil0NEJCqGKLJ7DSMmbio5nJVykauxbRKJBP8Y2QMA8N9D2ci+VilyRURE4mGIIruXe30+lIajUC0iposX7u3mjVqDgMXfnRG7HCIi0TBEkd3Lux6i/PnQ4RYz54GekEiAHcdzkX65VOxyiIhEwWsbZPfyrl/O07hxJKqpmrIifGSQO9KyS/Hi5nQ8PSQEEonkrs9740rpRETWjiNRZNeMgmAaieLlvJYV29MPcqkEF4t0yMwrF7scIqI2xxBFdq1Ep4feYIRcKoG3i1LscuyKu5MCg7t4AwB2n8yDwcjHcBJR+8IQRXatYVK5r5sSMundX24ic8N7+MBJIUNBeQ3SskvELoeIqE0xRJFd+30+FCeVtwaVgwz39fAFAPxwOh/6OqPIFRERtR2GKLJrv9+Zx/lQrSW6syc8nRUor67Dz2cLxS6HiKjNMESRXcstq3/cCyeVtx65VIqRvfwAAPvOFqKsqlbkioiI2gZDFNmt6loDSirrv9D9ubxBqwoLVKOjlxNqDQK+P5kndjlERG2CIYrs1o2Pe3Hi415alUQiwUNhAZAAOHq5FJeL+TgYIrJ/DFFktwq0NQAAP45CtYlAD0dEBnsAAL49kQtB4JIHRGTfGKLIbuWXX1/ewJXrQ7WVkb38oJBJkV1cieNXysQuh4ioVTFEkd3iSFTbc3N0wLAePgDqF+DkkgdEZM8YoshumUaiGKLa1JCu3nB3dEBZVS1+OcclD4jIfjFEkV2q0htQXl0HgJfz2pqDTIpRfTQAgJ9+K0RppV7kioiIWgdDFNmlhjvz1I4OUDnIRK6m/blxyYNdGVzygIjsE0MU2aWGS3l+bhyFEoNEIsGf+9YveXDiahnOF1aIXRIRUYtjiCK71DCp3NeV86HEEuDuiOjOngCAb47lwGDkkgdEZF8YosguFXB5A6vwp54aOClkKCivQcr5IrHLISJqUQxRZJe4vIF1cFTIMKp3/STz5DMF0FbzuXpEZD8YosjuVOrrUF7DO/OsRb+OHujg4YiaOiO+4yRzIrIjDFFkd/Kvj0K5OzpAyTvzRCeVSDAm/Pfn6l0q0oldEhFRi2CIIrtjmg/FO/OsRgcPJ/TvVP9cvf8du8pJ5kRkFxiiyO40jET58c48qxLXq36Seb62Br+c5UrmRGT7RA9RK1euRKdOnaBSqRAdHY1Dhw7dtv2WLVsQGhoKlUqFsLAw7Ny502z/1q1bMXLkSHh5eUEikSA9Pd1sf3FxMWbOnIkePXrA0dERwcHBeP7551FWZv6wVIlEctNr06ZNLdJnal0FWj7uxRo5KeUYHeYPoH6SebGOK5kTkW0TNURt3rwZiYmJmD9/PtLS0hAeHo64uDgUFBQ02n7//v2YOHEiEhIScPToUcTHxyM+Ph4ZGRmmNjqdDkOGDMGiRYsaPUZOTg5ycnLw7rvvIiMjA+vWrcPu3buRkJBwU9u1a9ciNzfX9IqPj2+RflPryi9vuDOPl/OsTUSQOzr7OKPOKOB/6VchCLysR0S2SyKI+LdYdHQ0BgwYgBUrVgAAjEYjgoKCMHPmTMyePfum9uPHj4dOp8OOHTtM2wYNGoSIiAisXr3arO2lS5cQEhKCo0ePIiIi4rZ1bNmyBU8++SR0Oh3kcjmA+pGor7/+ulnBqaamBjU1NaaftVotgoKCUFZWBjc3tyYfh+5s48HsRrfraurw752nAQDz/9wLSjknllubovIaLN9zFnVGAeMHBCG8g7tp3xPRweIVRkR0nVarhVqtvuP3t2gjUXq9HqmpqYiNjf29GKkUsbGxSElJafQ9KSkpZu0BIC4u7pbtm6rhQ2oIUA2mT58Ob29vDBw4EJ999tkd/9W8cOFCqNVq0ysoKOiu6qLma3jci4eTAwOUlfJ2VWJ4Dx8AwLfHc1GlN4hcERGRZUQLUUVFRTAYDPDz8zPb7ufnh7y8xteSycvLa1b7ptbx1ltvYdq0aWbb33zzTXz55ZdISkrCuHHj8Pe//x0ffvjhbY81Z84clJWVmV6XL1+2uC6yDB/3YhuGdvOBj4sSFTV1+O4k144iItskv3MT+6XVajF69Gj06tULCxYsMNs3d+5c0+8jIyOh0+mwZMkSPP/887c8nlKphFLJeThiytfywcO2QC6TIj4yEB//fAGHLhUjMtgdHb2cxS6LiKhZRBuJ8vb2hkwmQ35+vtn2/Px8aDSaRt+j0Wia1f52ysvLMWrUKLi6uuLrr7+Gg4PDbdtHR0fjypUrZnOeyPoUXJ9UzjvzrF+ItzOiOtavHbUtnWtHEZHtsShEXbhw4a5PrFAoEBUVheTkZNM2o9GI5ORkxMTENPqemJgYs/YAkJSUdMv2t6LVajFy5EgoFAps374dKtWdv3DT09Ph4eHBkSYr17C8AdeIsg0P9ObaUURkuyy6nNe1a1cMGzYMCQkJePTRR5sUQhqTmJiIKVOmoH///hg4cCCWLVsGnU6HqVOnAgAmT56MwMBALFy4EAAwa9YsDBs2DEuXLsXo0aOxadMmHDlyBGvWrDEds7i4GNnZ2cjJyQEAZGZmAqgfxdJoNKYAVVlZiS+++AJarRZarRYA4OPjA5lMhm+++Qb5+fkYNGgQVCoVkpKS8Pbbb+Oll16yqJ/UNipq6qDTGyAB4MNn5tmEhrWjtqReQfKZAmRd0/GyHhHZDItGotLS0tC3b18kJiZCo9Hgb3/72x0XyWzM+PHj8e6772LevHmIiIhAeno6du/ebZo8np2djdzcXFP7wYMHY+PGjVizZg3Cw8Px1VdfYdu2bejTp4+pzfbt2xEZGYnRo0cDACZMmIDIyEjTEghpaWk4ePAgTpw4ga5du8Lf39/0apgI7uDggJUrVyImJgYRERH46KOP8N5772H+/PmWfFzURhpGoTycFVDIRV9HlproxrWjZv+/E1w7iohsxl2tE1VXV4ft27ebFqzs3r07/vrXv+Kpp56Cj49PS9Zpk5q6zgQ1X2PrRKVcuIZvjuUgVOOKyTGd2r4osti1ivq1o2oNAt5+JIzrRRGRqNpknSi5XI6xY8diy5YtWLRoEc6dO4eXXnoJQUFBmDx5stkoElFrM82H4qRym+PlosTIXvU3iLy98zRySqtEroiI6M7uKkQdOXIEf//73+Hv74/33nsPL730Es6fP4+kpCTk5OTg4Ycfbqk6ie7IdGce50PZpJguXugX7I6Kmjq89jUv6xGR9bMoRL333nsICwvD4MGDkZOTg88//xxZWVn417/+hZCQENx7771Yt24d0tLSWrpeolv6PURxJMoWSSUSLH40HAq5FD9mFmJr2lWxSyIiui2LQtSqVavwxBNPICsrC9u2bcNDDz0EqdT8UL6+vvj0009bpEiiO6nU10FXUwcA8HZViFwNWaqrrwteiO0GAHjjm5OmS7RERNbIohCVlJSEV199Ff7+/mbbBUFAdnb9hF+FQoEpU6bcfYVETVB0fRRK7chn5tm6afd2RligGtrqOry+LYOX9YjIalkUorp06YKioqKbthcXFyMkJOSuiyJqroZLeVwfyvbJZVIsfrQv5FIJvj+Vj29P8AYVIrJOFoWoW/3LsKKiwuKFN4nuRmHF9RDlwhBlD3r6u2H6fV0BAPP/dxLFOr3IFRER3axZK5YnJiYCACQSCebNmwcnJyfTPoPBgIMHDyIiIqJFCyRqikKORNmFG9f/8nJRwM9NiXxtDaauPYTxA1pn7SiuSUVElmpWiDp69CiA+pGoEydOQKH4fQKvQqFAeHg4H41ComCIsj9yqRTj+nXAqh/P49iVMvTtoEVPfy5aS0TWo1khau/evQCAqVOn4oMPPuAq3GQV6gxG0+Uehij70sHDCfd288G+s4XYln4Vnbyc4ajgjQNEZB0smhO1du1aBiiyGtd0eggAlHIpXJUWPVObrNiInr7wdlGivLoOOzM4yZyIrEeTv3HGjh2LdevWwc3NDWPHjr1t261bt951YURNdeNK5RKJRORqqKU5yKQY1y8Qa/ZdQGpWCcIC1eju5yp2WURETR+JUqvVpi8otVp92xdRW+J8KPvX0csZg7p4AQC2Hb2KmlqDyBURETVjJGrt2rWN/p5IbIXl9atac3kD+xbXS4MzuVqUVNZi98k8PBwRKHZJRNTOWTQnqqqqCpWVlaafs7KysGzZMnz//fctVhhRU5nWiOIz8+yaQi7FI5EdAAAHLxbjQlGFyBURUXtnUYh6+OGH8fnnnwMASktLMXDgQCxduhQPP/wwVq1a1aIFEt2OURB4Oa8d6errggGdPAEAW9OuQl9nFLkiImrPLApRaWlpuPfeewEAX331FTQaDbKysvD5559j+fLlLVog0e1oq2pRaxAgk0jg6cwHD7cHD/TRQO3ogGKdHj+czhe7HCJqxywKUZWVlXB1rb875vvvv8fYsWMhlUoxaNAgZGVltWiBRLfTMArl6aKATMo789oDlYMM8REBAIBfzxUhu7jyDu8gImodFoWorl27Ytu2bbh8+TK+++47jBw5EgBQUFDA9aOoTfGZee1TD40bIoPcIQD4f2lXUGfgZT0iansWhah58+bhpZdeQqdOnRAdHY2YmBgA9aNSkZGRLVog0e3cuEYUtS+j+/rDRSlHYXkN9mQWiF0OEbVDFoWoRx99FNnZ2Thy5Ah2795t2j5ixAi8//77LVYc0Z1wUnn75aSQY0x4/WW9fb8VIqe0SuSKiKi9sShEAYBGo0FkZCSk0t8PMXDgQISGhrZIYURNUcQQ1a71CVSjT6AaRqH+sp7BKIhdEhG1IxY9aEyn0+Gdd95BcnIyCgoKYDSaz0e4cOFCixRHdDtVegPKa+oAcE5Ue/bnvv64UFiB3LJq/HK2EMN6+IpdEhG1ExaFqKeffho//fQTnnrqKfj7+/N5ZSSKhknlbio5lA4ykashsbiqHPBgmD++Sr2C5DMF6BOohhdDNRG1AYtC1K5du/Dtt9/innvuael6iJrM9LgXXspr9yKD3HE0uwTnC3X4X3oOpt7Tif+4I6JWZ9GcKA8PD3h6erZ0LUTN8vukcj7upb2TSCR4OCIQcqkE5workH65VOySiKgdsChEvfXWW5g3b57Z8/OI2hrvzKMbebsocX9o/Xyob0/kovL6fDkiotZi0eW8pUuX4vz58/Dz80OnTp3g4OBgtj8tLa1FiiO6nYY1ojipnBoM6eaN9MulKCivwa6MPIyL6iB2SURkxywKUfHx8S1cBlHz1BmMKKnUA+BCm/Q7uVSKRyID8dG+C0jNLkFEsDu6+LiIXRYR2SmLQtT8+fNbug6iZrmm08MoAEq5FK4qi/4Yk53q6OWMgSGeOHSxGP9Lz8HzI7pCLrV4STwioluy+G+W0tJSfPLJJ5gzZw6Ki4sB1F/Gu3r1aosVR3QrN86H4l1Y9EdxvTRwVspRVFGDX89dE7scIrJTFoWo48ePo3v37li0aBHeffddlJaWAgC2bt2KOXPmNOtYK1euRKdOnaBSqRAdHY1Dhw7dtv2WLVsQGhoKlUqFsLAw7Ny502z/1q1bMXLkSHh5eUEikSA9Pf2mY1RXV2P69Onw8vKCi4sLxo0bh/z8fLM22dnZGD16NJycnODr64uXX34ZdXWcqGot+OBhuh1HhQwP9NYAAPaeKUBZVa3IFRGRPbIoRCUmJuIvf/kLzp49C5Xq99vLH3zwQezbt6/Jx9m8eTMSExMxf/58pKWlITw8HHFxcSgoaPxhovv378fEiRORkJCAo0ePIj4+HvHx8cjIyDC10el0GDJkCBYtWnTL87744ov45ptvsGXLFvz000/IycnB2LFjTfsNBgNGjx4NvV6P/fv3Y/369Vi3bh3mzZvX5L5R6+KdeXQnEcHu6OjpBL3BiJ0ncsUuh4jskEQQhGY/bEqtViMtLQ1dunSBq6srjh07hs6dOyMrKws9evRAdXV1k44THR2NAQMGYMWKFQAAo9GIoKAgzJw5E7Nnz76p/fjx46HT6bBjxw7TtkGDBiEiIgKrV682a3vp0iWEhITg6NGjiIiIMG0vKyuDj48PNm7ciEcffRQAcObMGfTs2RMpKSkYNGgQdu3ahYceegg5OTnw8/MDAKxevRqvvvoqCgsLoVAoGu1PTU0NampqTD9rtVoEBQWhrKwMbm5uTfpMqGnueWcPrpZWYVJ0MHoHqMUuh6xUblkVVuw5BwHAX+8JQVffmyeZPxEd3PaFEZFV02q1UKvVd/z+tmgkSqlUQqvV3rT9t99+g4+PT5OOodfrkZqaitjY2N+LkUoRGxuLlJSURt+TkpJi1h4A4uLibtm+MampqaitrTU7TmhoKIKDg03HSUlJQVhYmClANZxHq9Xi5MmTtzz2woULoVarTa+goKAm10VNJwgCL+dRk/irHRHd2QsA8M2xHNT94TmfRER3w6IQNWbMGLz55puora2fZyCRSJCdnY1XX30V48aNa9IxioqKYDAYzIIKAPj5+SEvL6/R9+Tl5TWr/a2OoVAo4O7ufsvj3Oo8DftuZc6cOSgrKzO9Ll++3OS6qOnytNXQ1xkhlYDPSKM7+lNPPzgrZCisqMF+TjInohZkUYhaunQpKioq4OPjg6qqKgwbNgxdu3aFq6sr/v3vf7d0jTZDqVTCzc3N7EUt73yBDgDg6ayETMo78+j2HBUyjOrjDwDYw0nmRNSCLFpgR61WIykpCb/++iuOHTuGiooK9OvX76ZLbbfj7e0NmUx2011x+fn50Gg0jb5Ho9E0q/2tjqHX61FaWmo2GnXjcTQazU13CTactznnotZxvrACACeVU9NFBrvj8KViZBdXIulUHh6N4qV2Irp7zR6JMhqN+Oyzz/DQQw/hb3/7G1atWoVffvkFOTk5aM4cdYVCgaioKCQnJ5sdOzk5GTExMY2+JyYmxqw9ACQlJd2yfWOioqLg4OBgdpzMzExkZ2ebjhMTE4MTJ06Y3SWYlJQENzc39OrVq8nnotZxruB6iOKlPGoiqUSCh/rWj0alZZfiakmVyBURkT1oVogSBAFjxozB008/jatXryIsLAy9e/dGVlYW/vKXv+CRRx5p1skTExPx8ccfY/369Th9+jSee+456HQ6TJ06FQAwefJks3WnZs2ahd27d2Pp0qU4c+YMFixYgCNHjmDGjBmmNsXFxUhPT8epU6cA1Aek9PR001wmtVqNhIQEJCYmYu/evUhNTcXUqVMRExODQYMGAQBGjhyJXr164amnnsKxY8fw3Xff4fXXX8f06dOhVPKLW2wNI1F83As1RwcPJ0QEuQMAvj3RvH/0ERE1plmX89atW4d9+/YhOTkZ9913n9m+PXv2ID4+Hp9//jkmT57cpOONHz8ehYWFmDdvHvLy8hAREYHdu3ebJnFnZ2dDesPjGgYPHoyNGzfi9ddfx2uvvYZu3bph27Zt6NOnj6nN9u3bTSEMACZMmACg/lE1CxYsAAC8//77kEqlGDduHGpqahAXF4f//Oc/pvfIZDLs2LEDzz33HGJiYuDs7IwpU6bgzTffbM7HRa2El/PIUiN7+eFkThkuXavEyRwt+gRyeQwislyz1okaOXIk7r///kbXcAKAt99+Gz/99BO+++67FivQljV1nQlqOm11Lfou+B4AMHd0LzgqZCJXRLYm6VQ+9mYWwNNZgRdGdMPkwZ3ELomIrEyrrBN1/PhxjBo16pb7H3jgARw7dqw5hyRqlguF9XfmuSrlDFBkkaHdveGqkqNYp0fKBS55QESWa1aIKi4uvmn9pBv5+fmhpKTkrosiupXzBbyUR3dHKZdhZK/6v8f2nCnAtYqaO7yDiKhxzQpRBoMBcvmtp1HJZDI+pJdaFedDUUuIDPZAgFqFmjojlv1wVuxyiMhGNWtiuSAI+Mtf/nLLO9RufG4cUWs4x5EoagFSiQQP9vXHJz9fxMZD2fjrkBCEeDuLXRYR2ZhmhagpU6bcsU1T78wjsoRpJIprRNFd6uztgh5+rsjML8e732di5RP9xC6JiGxMs0LU2rVrW6sOojuqNRiRda0SAEeiqGXE9dbgt4JyfHs8F38bWoq+HdzFLomIbIhFz84jEkN2cSXqjAKcFDK4OTqIXQ7ZAY1ahUciAgEAi3afEbkaIrI1DFFkMxrmQ3X2cYZUwgcPU8t48U/doZBJ8eu5a/j5bKHY5RCRDWGIIpvRMB+qi4+LyJWQPQnydMKTgzoCqB+NMhr5OBgiahqGKLIZ5wvqF9rsyhBFLWzG/V3hopQj46oWO07kil0OEdkIhiiyGaaRKF+GKGpZns4K/G1oZwDA0u8zoa8zilwREdkChiiyCYIgmFYr5+U8ag0J94bA20WJrGuV+PLIZbHLISIbwBBFNqGwvAblNXWQSoBO3k5il0N2yEkhx8z7uwIAVuw5h+pag8gVEZG1Y4gim3Du+qW8YE8nKOV88DC1jgkDgxCgViFPW43/HsoWuxwisnIMUWQTzhfWTyrnpTxqTUq5DDPu7wYAWLn3PKr0HI0ioltjiCKbYJoPxUnl1MoejeqADh6OKKqowf8duCR2OURkxRiiyCb8vkYUHxJLrUshl+L5EfWjUat/uoCKmjqRKyIia8UQRTahYSSqK0eiqA2MjQxEiLczinV6rN9/SexyiMhKMUSR1dPV1CGnrBoA0NmbIYpan1wmxazro1Fr9l2AtrpW5IqIyBoxRJHVu3B9UrmXswIezgqRq6H24s/hAejq64Kyqlp89stFscshIivEEEVWj8/MIzHIpBK8EFs/GvXpzxdRWqkXuSIisjYMUWT1+LgXEsuDffwRqnFFeU0dPv75gtjlEJGVYYgiq3eugHfmkTikUgle/FN3AMDaXy/hWkWNyBURkTVhiCKrx5EoEtPIXn7oE+iGSr0BH+3jaBQR/Y4hiqxancGIS0WVAICunBNFIpBIJEi8Phr1ecolFJRXi1wREVkLhiiyaldKqqA3GKGUSxHo7ih2OdRO3dfDFxFB7qiuNWL1jxyNIqJ6DFFk1RrmQ3X2cYFUKhG5GmqvbhyN+uJgFvK1HI0iIoYosnJ83AtZi3u7eSOqowf0dUas+vG82OUQkRVgiCKrxjWiyFpIJBK8GFs/GrXxUDZyy6pEroiIxMYQRVbt/PXVyvnMPLIG93T1wsBOntDXGfGfvRyNImrvGKLIagmCcMMaUQxRJD6JRIIX/lS/ivnmw5eRU8rRKKL2zCpC1MqVK9GpUyeoVCpER0fj0KFDt22/ZcsWhIaGQqVSISwsDDt37jTbLwgC5s2bB39/fzg6OiI2NhZnz5417f/xxx8hkUgafR0+fBgAcOnSpUb3HzhwoOU/AGpUUYUeZVW1kEiAEG/OiSLrMLiLNwZ19oTeYMTKvefELoeIRCR6iNq8eTMSExMxf/58pKWlITw8HHFxcSgoKGi0/f79+zFx4kQkJCTg6NGjiI+PR3x8PDIyMkxtFi9ejOXLl2P16tU4ePAgnJ2dERcXh+rq+jtqBg8ejNzcXLPX008/jZCQEPTv39/sfD/88INZu6ioqNb7MMjM2fxyAECwpxMcFTKRqyH6XcPcqC+PXMaVkkqRqyEisYgeot577z0888wzmDp1Knr16oXVq1fDyckJn332WaPtP/jgA4waNQovv/wyevbsibfeegv9+vXDihUrANSPQi1btgyvv/46Hn74YfTt2xeff/45cnJysG3bNgCAQqGARqMxvby8vPC///0PU6dOhURifhu9l5eXWVsHB4dW/Tzod79dD1HdfF1FroTIXHRnLwzu4oVag8DRKKJ2TNQQpdfrkZqaitjYWNM2qVSK2NhYpKSkNPqelJQUs/YAEBcXZ2p/8eJF5OXlmbVRq9WIjo6+5TG3b9+Oa9euYerUqTftGzNmDHx9fTFkyBBs3779tv2pqamBVqs1e5Hlfrs+H6q7H+dDkfVpeKbeliNXcLmYo1FE7ZGoIaqoqAgGgwF+fn5m2/38/JCXl9foe/Ly8m7bvuHX5hzz008/RVxcHDp06GDa5uLigqVLl2LLli349ttvMWTIEMTHx982SC1cuBBqtdr0CgoKumVburPf8upHorr7cSSKrM+ATp64t5s36owCPtxz9s5vICK7I/rlPLFduXIF3333HRISEsy2e3t7IzExEdHR0RgwYADeeecdPPnkk1iyZMktjzVnzhyUlZWZXpcvX27t8u2WIAimy3kMUWStXrg+N+r/pV1F1jWdyNUQUVsTNUR5e3tDJpMhPz/fbHt+fj40Gk2j79FoNLdt3/BrU4+5du1aeHl5YcyYMXesNzo6GufO3Xr+g1KphJubm9mLLFNQXgNtdR2kEqAzVysnKxXV0QPDuvvAYBSwPJlzo4jaG1FDlEKhQFRUFJKTk03bjEYjkpOTERMT0+h7YmJizNoDQFJSkql9SEgINBqNWRutVouDBw/edExBELB27VpMnjy5SRPG09PT4e/v3+T+keUaRqE6eTlD5cA788h6NcyN+vroFVws4mgUUXsiF7uAxMRETJkyBf3798fAgQOxbNky6HQ60yTvyZMnIzAwEAsXLgQAzJo1C8OGDcPSpUsxevRobNq0CUeOHMGaNWsAXF8M74UX8K9//QvdunVDSEgI5s6di4CAAMTHx5ude8+ePbh48SKefvrpm+pav349FAoFIiMjAQBbt27FZ599hk8++aQVPw1q8Ft+/aTybpxUTq1s48Hsuz5GDz9XZOaXI3FzOh7rf+e5kE9EB9/1OYlIfKKHqPHjx6OwsBDz5s1DXl4eIiIisHv3btPE8OzsbEilvw+YDR48GBs3bsTrr7+O1157Dd26dcO2bdvQp08fU5tXXnkFOp0O06ZNQ2lpKYYMGYLdu3dDpVKZnfvTTz/F4MGDERoa2mhtb731FrKysiCXyxEaGorNmzfj0UcfbYVPgf7oLOdDkQ0Z0dMXmfnlSL9ciuE9fOHjqhS7JCJqAxJBEASxi7BXWq0WarUaZWVlnB/VTGP/8yvSskuxfGIkxoQH3LS/JUYPiFrS/6Vcwum8coR3UGP8gNuPNHEkisi6NfX7u93fnUfWRxAEnL1+Oa8HR6LIRozoWT96fvxKGfK11SJXQ0RtgSGKrE5uWTXKa+ogl0r4zDyyGQHujugd4AYBQNKp/Du2JyLbxxBFVsd0Z563MxRy/hEl2xHb0w8SAKdytVzFnKgd4DcUWZ2GS3l83AvZGj83FSKD3QEA351q/AkJRGQ/GKLI6vDBw2TLRoT6QSaV4EKhDueuP/+RiOwTQxRZnYYHD/fQMESR7fFwVmBgiCcA4LuTeeAN0ET2iyGKrIrRKNywRhQv55Ftuq+HLxQyKa6WVuFkjlbscoiolTBEkVW5WlqFSr0BDjIJOnrxzjyyTS5KOe7p6g2g/k49g5GjUUT2iCGKrMrZgvpRqM7eLnCQ8Y8n2a57u3nD0UGGwooaHM0uEbscImoF/JYiq8Jn5pG9UDnIMLyHDwDgh9P50NcZRa6IiFoaQxRZlYY787hSOdmDQZ294O7kAG11HX45Vyh2OUTUwhiiyKqcNY1EMUSR7XOQSRHXWwMA2PdbEbTVtSJXREQtiSGKrIbRKJjmRPHOPLIXfQPVCPJwhN5gxA98HAyRXWGIIqtxuaQS1bVGKORS3plHdkMikeDBMH8AQGpWCXLLqkSuiIhaCkMUWY2GSeVdfFwgk0pEroao5XT0ckZYoBoCgF0nuAAnkb1giCKr8fukcl7KI/sT11sDmVSCc4UV+DGTk8yJ7AFDFFmNzLzrz8zjpHKyQ57OCgzu4gUA+PfO06gzcMkDIlvHEEVW40xe/eMxevm7iVwJUesY3t0XTgoZzhVU4POULLHLIaK7xBBFVqG61oDzhToAQKg/R6LIPjkqZBjZq37Jg/eSfkOBtlrkiojobjBEkVU4V1ABg1GAu5MDNG4qscshajX9O3kgPMgdFTV1+PfO02KXQ0R3gSGKrMKp3PpLeT01bpBIeGce2S+pRIJ/PdwHEgnwv/Qc7D9fJHZJRGQhhiiyCmdy6yeV9+R8KGoHwjqo8WR0RwDA3G0ZfK4ekY1iiCKrcPr6SBTnQ1F78dLIHvByVuB8oQ6f/nJR7HKIyAIMUSQ6QRBwmnfmUTujdnLAnAd7AgCWJ5/F1VKuZE5kaxiiSHR52mqUVtZCJpWgqy8X2qT2Y1y/QAzo5IGqWgMWbD/JlcyJbAxDFImuYT5UFx9nqBxkIldD1HYkEgneiu8DuVSCpFP52HE8V+ySiKgZGKJIdA135oVqeCmP2p9QjRv+fl9XAMD87SdxraJG5IqIqKkYokh0DZPKeWcetVcz7uuKUI0rinV6zNt+UuxyiKiJGKJIdLwzj9o7hVyKJY+GQyaV4Nvjudidwct6RLaAIYpEVamvw4Wi+se99AlQi1wNkXjCOqjx7LDOAIDXt2WgRKcXuSIiuhOGKBLV6VwtBAHwc1PCx1UpdjlEonp+RDd083VBUYUeb3zDy3pE1s4qQtTKlSvRqVMnqFQqREdH49ChQ7dtv2XLFoSGhkKlUiEsLAw7d+402y8IAubNmwd/f384OjoiNjYWZ8+eNWvTqVMnSCQSs9c777xj1ub48eO49957oVKpEBQUhMWLF7dMh8kk42r9pTyOQhEBSrkMSx4Lh1QCbEvPwe6MPLFLIqLbED1Ebd68GYmJiZg/fz7S0tIQHh6OuLg4FBQUNNp+//79mDhxIhISEnD06FHEx8cjPj4eGRkZpjaLFy/G8uXLsXr1ahw8eBDOzs6Ii4tDdbX5E9PffPNN5Obmml4zZ8407dNqtRg5ciQ6duyI1NRULFmyBAsWLMCaNWta54NopzKulgEAegcyRBEBQESQO6YN7QIAmL31OHLLuAgnkbUSPUS99957eOaZZzB16lT06tULq1evhpOTEz777LNG23/wwQcYNWoUXn75ZfTs2RNvvfUW+vXrhxUrVgCoH4VatmwZXn/9dTz88MPo27cvPv/8c+Tk5GDbtm1mx3J1dYVGozG9nJ2dTfs2bNgAvV6Pzz77DL1798aECRPw/PPP47333mu1z6I9yshpGIninXlEDRL/1B1hgWqUVtYicfMxGIxchJPIGokaovR6PVJTUxEbG2vaJpVKERsbi5SUlEbfk5KSYtYeAOLi4kztL168iLy8PLM2arUa0dHRNx3znXfegZeXFyIjI7FkyRLU1dWZnWfo0KFQKBRm58nMzERJSUmjtdXU1ECr1Zq96Naqaw04m1+/0GYfjkQRmSjkUnwwIQJOChlSLlzDR/vOi10SETVC1BBVVFQEg8EAPz8/s+1+fn7Iy2t8LkBeXt5t2zf8eqdjPv/889i0aRP27t2Lv/3tb3j77bfxyiuv3PE8N57jjxYuXAi1Wm16BQUF3bLvBPyWX446owBPZwX81SqxyyGyKp19XLBgTG8AwHvf/4b0y6XiFkRENxH9cp5YEhMTMXz4cPTt2xfPPvssli5dig8//BA1NZavFjxnzhyUlZWZXpcvX27Biu1Pw6Ty3gFukEgkIldDZH0ei+qA0X39UWcUMGvTUVTU1N35TUTUZkQNUd7e3pDJZMjPzzfbnp+fD41G0+h7NBrNbds3/NqcYwJAdHQ06urqcOnSpdue58Zz/JFSqYSbm5vZi24tI6d+Ujkv5RE1TiKR4O34MAS6OyLrWiXmbcvgQ4qJrIioIUqhUCAqKgrJycmmbUajEcnJyYiJiWn0PTExMWbtASApKcnUPiQkBBqNxqyNVqvFwYMHb3lMAEhPT4dUKoWvr6/pPPv27UNtba3ZeXr06AEPD4/md5ZucvL6nXlc3oDo1tRODlg2IQJSCbD16FVsOswRbiJrIfrlvMTERHz88cdYv349Tp8+jeeeew46nQ5Tp04FAEyePBlz5swxtZ81axZ2796NpUuX4syZM1iwYAGOHDmCGTNmAKj/l9sLL7yAf/3rX9i+fTtOnDiByZMnIyAgAPHx8QDqJ40vW7YMx44dw4ULF7Bhwwa8+OKLePLJJ00B6YknnoBCoUBCQgJOnjyJzZs344MPPkBiYmLbfkB2qtZgxOm8hknlHLEjup0BnTzxUlwPAPUPKW5YGoSIxCUXu4Dx48ejsLAQ8+bNQ15eHiIiIrB7927TJO7s7GxIpb9nvcGDB2Pjxo14/fXX8dprr6Fbt27Ytm0b+vTpY2rzyiuvQKfTYdq0aSgtLcWQIUOwe/duqFT1k5eVSiU2bdqEBQsWoKamBiEhIXjxxRfNApJarcb333+P6dOnIyoqCt7e3pg3bx6mTZvWRp+MfTubXwF9nRGuKjmCPJzELofI6j07tAvSskrww+kCPPtFKr6deS/UTg5il0XUrkkEXmBvNVqtFmq1GmVlZZwf9Qf/PZSNOVtPYEhXb3zxdHSz37/xYHYrVEXUNp6IDrbofWWVtXhoxc+4XFyFEaG++Hhyf0ilvCmDqKU19ftb9Mt51D6lZ5cCAMKDOB+KqKnUTg5YNSkKCrkUyWcKsOonrh9FJCaGKBLFsSulAIDwDu6i1kFka/oEqvHWw/XrRy39PhO/nC0SuSKi9oshitqcrqYOv11fqTwiyF3cYohs0PgBwXi8fwcYBWDGf9OQfa1S7JKI2iWGKGpzGVfLYBQAf7UKvm5cqZzIEm8+3AfhQe4orazFM58fgY4LcRK1OdHvzqP2h5fyqL1rqRsjRvXW4EJBBTLzy/H4RymYODAY0tus/m/phHYiahxHoqjNHbtcv8ZNRLC7uIUQ2Ti1owMmRQdDJpXgZI4WP2YWiF0SUbvCEEVtruFBqhyJIrp7wV7OeDg8AADww+kCnM7VilwRUfvBEEVtqrC8BldLqyCRAGEduLwBUUvo38kTgzp7AQC+PHIZ+dpqkSsiah8YoqhNHb8+H6qbrwtclJySR9RSRof5I8TbGTV1RnxxIAtVeoPYJRHZPYYoalOpWSUAuLQBUUuTSSWYODAY7k4OuKbTY9PhbBj5QAqiVsUQRW3qyKX6ENW/o6fIlRDZHxelHE9Gd4SDTIKzBRX4LiNP7JKI7BpDFLUZfZ3RtLxBVCcPcYshslMB7o4Y168DAODnc0U4ml0ickVE9oshitpMRk4ZauqM8HRWoLO3s9jlENmtvh3cMby7DwDg66NXcaWEK5oTtQaGKGozqdcv5UV19IDkNgsCEtHdi+3lh1CNK+qMAr44kAVtda3YJRHZHYYoajOHLxUDAPp35KU8otYmlUjweP8g+Lgqoa2uw4YDWaip4x17RC2JIYrahCAIpjvz+nM+FFGbUDnI8NSgjlA5SHG5pAqvf50BgXfsEbUYhihqE5euVeKaTg+FXIo+gVxkk6iteLsoMXFAMCQAtqRewdpfL4ldEpHdYIiiNnHk+qW88A5qKOUykashal+6+bnigTB/AMC/d57GL2eLRK6IyD4wRFGbOGKaVM71oYjEcE8XL4ztFwiDUcD0jWnIuqYTuyQim8cQRW0i5cI1AMDAEM6HIhKDRCLB24+EISLIHWVVtXjm8yOoqKkTuywim8YQRa3uSkklsosrIZNKMDDES+xyiNotlYMMHz0VBV9XJX7Lr8CLm9NhNHKiOZGlGKKo1aWcrx+F6ttBzYcOE4nMz02Fj56KgkIuRdKpfCz74TexSyKyWQxR1OoaLuUN7sJRKCJrEBnsgYWPhAEAlu85h2+P54pcEZFtYoiiViUIgmkkanAXb5GrIaIG46I6IGFICADgpS3HcCpHK3JFRLaHIYpa1aVrlcgtq4ZCJkUUVyonsipzHgjFvd28UVVrwDOfH8G1ihqxSyKyKQxR1KoaRqEig92hcuD6UETWRC6TYsXEfujk5YSrpVX4+4Y01BqMYpdFZDMYoqhV7T9fv6hfDOdDEVkltZMDPp7cHy5KOQ5eLMab35wSuyQim8EQRa3GaBRw4Pqk8pjODFFE1qqbnyuWjY+ARAL834EsbDyYLXZJRDaBIYpaTUZOGYoq9HBRytGP86GIrFpsLz+8NLIHAGDe/zJw6GKxyBURWT+GKGo1P2YWAgCGdPWGg4x/1Iis3d+Hd8Hovv6oMwp47otUXCmpFLskIqvGbzZqNXszCwAAw3v4iFwJETWFRCLBkkf7ope/G67p9Hh6/RHo+GgYoltiiKJWUazTI/1yKQBgeA9fcYshoiZzUsjx8ZT+8HZR4kxeOR8NQ3QbVhGiVq5ciU6dOkGlUiE6OhqHDh26bfstW7YgNDQUKpUKYWFh2Llzp9l+QRAwb948+Pv7w9HREbGxsTh79qxp/6VLl5CQkICQkBA4OjqiS5cumD9/PvR6vVkbiURy0+vAgQMt23k79fPZQggCEKpxhUatErscImqGQHfH+kfDyKT4/lQ+3kvio2GIGiN6iNq8eTMSExMxf/58pKWlITw8HHFxcSgoKGi0/f79+zFx4kQkJCTg6NGjiI+PR3x8PDIyMkxtFi9ejOXLl2P16tU4ePAgnJ2dERcXh+rqagDAmTNnYDQa8dFHH+HkyZN4//33sXr1arz22ms3ne+HH35Abm6u6RUVFdU6H4Sd2Xum4VIeR6GIbFFURw8sHFv/aJgVe8/hf+lXRa6IyPpIBEEQdZw2OjoaAwYMwIoVKwAARqMRQUFBmDlzJmbPnn1T+/Hjx0On02HHjh2mbYMGDUJERARWr14NQRAQEBCAf/zjH3jppZcAAGVlZfDz88O6deswYcKERutYsmQJVq1ahQsXLgCoH4kKCQnB0aNHERER0aS+1NTUoKbm9xV/tVotgoKCUFZWBjc3tyYdwx4YjAIG/PsHFOv02DxtEKJbYXkD3oJN1HxPRAc3+z0Ld53GRz9dgEIuxZd/i0FEkHvLF0ZkZbRaLdRq9R2/v0UdidLr9UhNTUVsbKxpm1QqRWxsLFJSUhp9T0pKill7AIiLizO1v3jxIvLy8szaqNVqREdH3/KYQH3Q8vT0vGn7mDFj4OvriyFDhmD79u237c/ChQuhVqtNr6CgoNu2t1fpl0tQrNPDlUsbENm8V+JCMSLUF/o6I575/Ahyy6rELonIaogaooqKimAwGODn52e23c/PD3l5eY2+Jy8v77btG35tzjHPnTuHDz/8EH/7299M21xcXLB06VJs2bIF3377LYYMGYL4+PjbBqk5c+agrKzM9Lp8+fIt29qzXSfqP+f7e/pyaQMiGyeTSrBsQgS6+7mgsLwG0z5PRZXeIHZZRFZBLnYBYrt69SpGjRqFxx57DM8884xpu7e3NxITE00/DxgwADk5OViyZAnGjBnT6LGUSiWUSmWr12zNBEHAroz6EPVAH43I1RDRje7mMviY8ED858dzOHG1DI99lIIJA4IglUju+D5LLiES2QpRhwm8vb0hk8mQn59vtj0/Px8aTeNfwBqN5rbtG35tyjFzcnJw3333YfDgwVizZs0d642Ojsa5c+fu2K49y7iqxdXSKjg6yDCsOyeVE9kLT2cFJkV3hEwiQcbVMnyX0fjIPlF7ImqIUigUiIqKQnJysmmb0WhEcnIyYmJiGn1PTEyMWXsASEpKMrUPCQmBRqMxa6PVanHw4EGzY169ehXDhw9HVFQU1q5dC6n0zh9Feno6/P39m9XH9mZXRi4A4L5QHzgqZCJXQ0QtKcTbGWP7BQIAfj5XZHrAOFF7JfrlvMTEREyZMgX9+/fHwIEDsWzZMuh0OkydOhUAMHnyZAQGBmLhwoUAgFmzZmHYsGFYunQpRo8ejU2bNuHIkSOmkSSJRIIXXngB//rXv9CtWzeEhIRg7ty5CAgIQHx8PIDfA1THjh3x7rvvorCw0FRPw2jV+vXroVAoEBkZCQDYunUrPvvsM3zyySdt9dHYnBsv5Y3qw7BJZI8igz1QVlWL70/l49vjuVA7OqB3gFrssohEIXqIGj9+PAoLCzFv3jzk5eUhIiICu3fvNk0Mz87ONhslGjx4MDZu3IjXX38dr732Grp164Zt27ahT58+pjavvPIKdDodpk2bhtLSUgwZMgS7d++GSlW/6GNSUhLOnTuHc+fOoUOHDmb13Ljiw1tvvYWsrCzI5XKEhoZi8+bNePTRR1vz47BpmfnluFikg0Iuxf2hvJRHZK+GdfdBaVUtDl0sxubDl5EwRI6OXs5il0XU5kRfJ8qeNXWdCXvx7neZWLH3HGJ7+uKTKQNa9VxcJ4pIXAajgA0Hs3AmrxxOChmmDe0MX9ebn07AieVki2xinSiyH0ajgK1pVwAAD0cEilwNEbU2mVSCCQOC0cHDEZV6Az775SKKdfo7v5HIjjBEUYtIuXANOWXVcFXJ8adefnd+AxHZPIVciikxneDrqoS2ug6f/nIBZVW1YpdF1GYYoqhF/L/U+lGoP4cHQOXAu/KI2gtnpRx/HRICL2cFSipr8ekvF1BezSBF7QNDFN21ipo60115j0Z1uENrIrI3bioHJAwJgbujA4oq9Pjs14uorKkTuyyiVscQRXdt54lcVNUa0NnbGZF8OClRu+TupEDCkBC4quTI19bgs18vooJBiuwcQxTdtc2H658ROC6qAyRNeAwEEdknLxcl/npPCJwVMuSUVePjfReQU8oHFpP9Yoiiu3LiShlSs0rgIJPgMV7KI2r3/NxUmDa0C9SODiisqMFjq1NwsUgndllErYIhiu7K2v0XAQCjw/zh63bzGjFE1P74uCrxt6Gd4e2iwNXSKjy2ej9O5WjFLouoxTFEkcUKy2uw41j9s/Km3hMicjVEZE3cnRSYNrQLevm7oahCj/FrUvisPbI7DFFksY0Hs6E3GBEZ7I5wTignoj9wUcqx6W+DMKCTB8qr6/DUp4ewfv8l8EEZZC8Yosgi1bUGfHEwCwDwl8GdxC2GiKyWm8oB/5cQjUciA2EwCpi//SRm/78TqKkziF0a0V1jiCKLbDyYjcLyGgS6O+KBPv5il0NEVkzlIMN7j4fjnw/2hFQCbD5yGRPXHECBtlrs0ojuCkMUNVuV3oBVP50HAMy4vysUcv4xIqLbk0gkeGZoZ6ydOhBuKjnSskvx4PJfsOdMvtilEVmM337UbBsOZqGwvAYdPBy5QjkRNcuw7j7YPmMIuvu5oKiiBn9ddwRztp6Ajgtzkg1iiKJmqdTXYfX1UaiZ93eFg4x/hIioeTp5O2P7jCFIGFJ/V+9/D2XjgQ9+xpFLxSJXRtQ8/AakZvnP3vMoqtAj2NMJY/txFIqILKNykGHuQ72w8ZloBLo7Iru4Eo99lIK52zJQotOLXR5RkzBEUZNdLNJhzb4LAIDXHuzJUSgiumuDu3hj1wv3Yly/DhAE4P8OZGH4uz9i7a8XUWswil0e0W3xW5CaRBAEvPHNSegNRgzt7oO43n5il0REdsJN5YClj4dj4zPRCNW4oqyqFm98cwoPfPAz9p4p4LpSZLXkYhdAtuG7k3n4MbMQDjIJFvy5Fx80TERNsvFgdrPaPzmoIw5fKkbSqXycK6jA1HWHEeCuwrDuvugd4AZpE/7ueSI62NJyiZqFIYruqEBbjTlbTwAAnrm3Mzr7uIhcERHZK6lEgugQL/QNdMePmQU4cPEackqr8d9D2fB2UWBoNx+EB7lzOgFZBYYoui2jUcA/thxDSWUtevm7YVZsN7FLIqJ2wFEhwwNh/hja3QcpF64h5fw1FFXosfXoVezMyEVEkDuiOnoiQK3iyDiJhiGKbuuTXy7g57NFUDlIsXxiBJRymdglEVE74qyUI7anH+7t6o1Dl4qx//w1lFXV4sCFYhy4UAx/tQqRwR7o5e8GT2eF2OVSO8MQRbf0w6l8vLPrDABg7kO90NXXVeSKiKi9UjrIcG83H9zT1RvnCypwJKsEp3K1yC2rRu6JXOw8kQuNmwqh/q7oFeCGsEA1ZFKOUFHrYoiiRp24UoaZ/z0KowBMHBiEJwZyoiYRiU8qkaCbnyu6+bmiUl+HY5dLkZGjRdY1HfK01cjTVuPHzEK4quQY0MkTAzp5YmCIB8IC3fmIKmpxDFF0kzN5WkxddxhVtQbc280bbz7ch3MOiMjqOCnkiOnijZgu3qjU1+G3/HKczi3HpSIdyqvrsOdMAfacKQAAKGRSdPNzQS9/N/QKcEMvfzd09XWBp7OCf7+RxRiiyEz65VJM+ewQyqrqJ5L/Z1I/3gVDRFbPSSFHRJAHIoI88Hj/DjidW45Dl4px6OI1HLpYjJLKWpzM0eJkjhZI/f19rio5QrydEeLtjI6eTvBTq6BxU8Hv+svLWQEpLwvSLTBEkcnujFz848tj0OkNiAx2x7q/DISrykHssoiImkUukyKsgxphHdRIGBICQRBwubgKp3LLcCpHi1O5WpzOLcfV0iqUV9fh+JUyHL9S1uixHGQS+Lqq4O2igLuTAu5ODnB3dPj9904OcFU6wEkpg4tSDieFHM5KWf2vChnk/EeoXWOIItQajFi06ww++eUiAOCerl5Y81R/OCv5x4OIbM/tFvjUqB2hUTvi/lA/1BqMuKbT41pFDa5V6FFcqYe2qhbl1XXQVtWioqYOtQYBV0urcLW0yqJa5FIJFHIplHIpHGRSKOTXX7I//NrYthv2Ocjqj6FykEEpl5ouQXJhUXHxW7KdO3SxGK9vO4Hf8isAAM/cG4JXRoXyEh4R2T0HmRQat/rLd40xGAWUV9dCW10HXU0dKvUGVOnrf62sNdT/qq+Dvs6Imjoj9NdfNXUGGK8/qabOKKBOX9+2pcikEjgrZHBWyrErIxeezgp4OSvh56aEv7sjAtQqBLg7wtdVyZGwVsYQ1U79ll+OD/ecwzfHcgAAHk4OWDi2L0b10YhcGRGRdZBJJdcv2zVv/SlBEGAwCvWBylAfsGqvB61aw+9hS2+4/rrx5z/+3mD+3jpj/bG11XXQVtcht6z6lnVIJYCfW32g6uDhiCAPJwR5NvzqBH+1iiHrLjFEtSO1BiN+zCzE5sPZ+OF0gWn7xIFBeCUuFB5cqI6I6K5JJBLIZRLIZVI4tfCxaw1G6GrqoKsxoKKmDn07qFGs06NIV4P8smrklFUjp7QK+dpq1BqE+nW0yqqRmlVy07FkUgn81aqbwlXD731clbxz8Q6sIkStXLkSS5YsQV5eHsLDw/Hhhx9i4MCBt2y/ZcsWzJ07F5cuXUK3bt2waNEiPPjgg6b9giBg/vz5+Pjjj1FaWop77rkHq1atQrduvz+ypLi4GDNnzsQ333wDqVSKcePG4YMPPoCLy+/PhTt+/DimT5+Ow4cPw8fHBzNnzsQrr7zSOh9CK7lWUYODF4ux9/qtvtd0egCARAI80EeD6fd1Re8AtchVEhFRUzjIpNdHx+p/HhfVodF2RqOAoooa5JRV42pJFa6UVOJySSUuF1fhckklrpRUQV9nxJWSKlwpqULKhZuPoZRL60ewPJ0aCVpOUDvyxiPRQ9TmzZuRmJiI1atXIzo6GsuWLUNcXBwyMzPh6+t7U/v9+/dj4sSJWLhwIR566CFs3LgR8fHxSEtLQ58+fQAAixcvxvLly7F+/XqEhIRg7ty5iIuLw6lTp6BS1V/7njRpEnJzc5GUlITa2lpMnToV06ZNw8aNGwEAWq0WI0eORGxsLFavXo0TJ07gr3/9K9zd3TFt2rS2+4CaQBAElFbW4tI1HS4W1b8uFOpwMqcMl65VmrX1dlEgPiIQEwYGo6svHyRMRGSPpFIJfN1U8HVTISLI/ab9RqOAwooaXC6uD1fZ16quh6z6gJVbVoWaOiPOF+pwvlDX6DncVHJTwOrg4QhvVyU8nRTwcFbA09kBHk4KeDor4KZysNtlIiSCIAhiFhAdHY0BAwZgxYoVAACj0YigoCDMnDkTs2fPvqn9+PHjodPpsGPHDtO2QYMGISIiAqtXr4YgCAgICMA//vEPvPTSSwCAsrIy+Pn5Yd26dZgwYQJOnz6NXr164fDhw+jfvz8AYPfu3XjwwQdx5coVBAQEYNWqVfjnP/+JvLw8KBT1l7lmz56Nbdu24cyZM03qm1arhVqtRllZGdzc3O7qc2pQazDihc3pKNHpUazT45pOjxKdHnXGW/9n7OrrgmHdfXB/qC8GhnjaxaTx2919Q0TUXrTW3Xm1BiNySqtMI1f1YavqesiqRFGFvsnHkkgAJ4f6ifD1r/olIFyUcjg6yK7ffSgx3YXYcGdiw+/lUglkUgmkEgmkUglkEgmkEph+Hx8Z2OKP+Gnq97eoI1F6vR6pqamYM2eOaZtUKkVsbCxSUlIafU9KSgoSExPNtsXFxWHbtm0AgIsXLyIvLw+xsbGm/Wq1GtHR0UhJScGECROQkpICd3d3U4ACgNjYWEilUhw8eBCPPPIIUlJSMHToUFOAajjPokWLUFJSAg8Pj5tqq6mpQU1NjennsrL6dUe0Wm0zPpXbEwQB36dfRE2t8aZ9vq5KdPJyRkdvJ3TyckJnHxeEBarNJkVW6Spg2Y261qVSVy52CUREomvJ75c/8nAAPPwU6OunAOButq9SX2cKWVdLK5FTWo2SSj1KK/UoqaxD6fXfV9TU35VYXg2Ut9Jf28NC/tTij/Rp+FzvNM4kaogqKiqCwWCAn5+f2XY/P79bjvbk5eU12j4vL8+0v2Hb7dr88VKhXC6Hp6enWZuQkJCbjtGwr7EQtXDhQrzxxhs3bQ8KCmq0Ly3tMswW4iUiIjv3jNgFWAGfZa137PLycqjVt543LPqcKHsyZ84cs1Eyo9GI4uJieHl5tdkdDlqtFkFBQbh8+XKLXUK0JvbeP4B9tBf23kd77x/APtoLS/ooCALKy8sREBBw23aihihvb2/IZDLk5+ebbc/Pz4dG0/h6RRqN5rbtG37Nz8+Hv7+/WZuIiAhTm4KCArNj1NXVobi42Ow4jZ3nxnP8kVKphFKpNNvm7u7eaNvW5ubmZrf/QwD23z+AfbQX9t5He+8fwD7ai+b28XYjUA1EnWGsUCgQFRWF5ORk0zaj0Yjk5GTExMQ0+p6YmBiz9gCQlJRkah8SEgKNRmPWRqvV4uDBg6Y2MTExKC0tRWrq7xe/9uzZA6PRiOjoaFObffv2oba21uw8PXr0aPRSHhEREbUvot+mlZiYiI8//hjr16/H6dOn8dxzz0Gn02Hq1KkAgMmTJ5tNPJ81axZ2796NpUuX4syZM1iwYAGOHDmCGTNmAKhf5OyFF17Av/71L2zfvh0nTpzA5MmTERAQgPj4eABAz549MWrUKDzzzDM4dOgQfv31V8yYMQMTJkwwDd098cQTUCgUSEhIwMmTJ7F582Z88MEHN01qJyIionZKsAIffvihEBwcLCgUCmHgwIHCgQMHTPuGDRsmTJkyxaz9l19+KXTv3l1QKBRC7969hW+//dZsv9FoFObOnSv4+fkJSqVSGDFihJCZmWnW5tq1a8LEiRMFFxcXwc3NTZg6dapQXl5u1ubYsWPCkCFDBKVSKQQGBgrvvPNOy3a8FVRXVwvz588XqqurxS6lVdh7/wSBfbQX9t5He++fILCP9qI1+yj6OlFEREREtkj0y3lEREREtoghioiIiMgCDFFEREREFmCIIiIiIrIAQ5SduHTpEhISEhASEgJHR0d06dIF8+fPh15v/pDI48eP495774VKpUJQUBAWL14sUsWWWblyJTp16gSVSoXo6GgcOnRI7JIssnDhQgwYMACurq7w9fVFfHw8MjMzzdpUV1dj+vTp8PLygouLC8aNG3fTArC25J133jEtQdLAHvp49epVPPnkk/Dy8oKjoyPCwsJw5MgR035BEDBv3jz4+/vD0dERsbGxOHv2rIgVN4/BYMDcuXPN/m556623zJ4pZkt93LdvH/785z8jICAAEonE9NzVBk3pS3FxMSZNmgQ3Nze4u7sjISEBFRUVbdiL27tdH2tra/Hqq68iLCwMzs7OCAgIwOTJk5GTk2N2DFvu4x89++yzkEgkWLZsmdn2lugjQ5SdOHPmDIxGIz766COcPHkS77//PlavXo3XXnvN1Ear1WLkyJHo2LEjUlNTsWTJEixYsABr1qwRsfKm27x5MxITEzF//nykpaUhPDwccXFxN60+bwt++uknTJ8+HQcOHEBSUhJqa2sxcuRI6HQ6U5sXX3wR33zzDbZs2YKffvoJOTk5GDt2rIhVW+7w4cP46KOP0LdvX7Pttt7HkpIS3HPPPXBwcMCuXbtw6tQpLF261GxB3sWLF2P58uVYvXo1Dh48CGdnZ8TFxaG6ulrEyptu0aJFWLVqFVasWIHTp09j0aJFWLx4MT788ENTG1vqo06nQ3h4OFauXNno/qb0ZdKkSTh58iSSkpKwY8cO7Nu3D9OmTWurLtzR7fpYWVmJtLQ0zJ07F2lpadi6dSsyMzMxZswYs3a23Mcbff311zhw4ECjj29pkT62+KIJZDUWL14shISEmH7+z3/+I3h4eAg1NTWmba+++qrQo0cPMcprtoEDBwrTp083/WwwGISAgABh4cKFIlbVMgoKCgQAwk8//SQIgiCUlpYKDg4OwpYtW0xtTp8+LQAQUlJSxCrTIuXl5UK3bt2EpKQkYdiwYcKsWbMEQbCPPr766qvCkCFDbrnfaDQKGo1GWLJkiWlbaWmpoFQqhf/+979tUeJdGz16tPDXv/7VbNvYsWOFSZMmCYJg230EIHz99demn5vSl1OnTgkAhMOHD5va7Nq1S5BIJMLVq1fbrPam+mMfG3Po0CEBgJCVlSUIgv308cqVK0JgYKCQkZEhdOzYUXj//fdN+1qqjxyJsmNlZWXw9PQ0/ZySkoKhQ4dCoVCYtsXFxSEzMxMlJSVilNhker0eqampiI2NNW2TSqWIjY1FSkqKiJW1jLKyMgAw/fdKTU1FbW2tWX9DQ0MRHBxsc/2dPn06Ro8ebdYXwD76uH37dvTv3x+PPfYYfH19ERkZiY8//ti0/+LFi8jLyzPro1qtRnR0tM30cfDgwUhOTsZvv/0GADh27Bh++eUXPPDAAwDso48NmtKXlJQUuLu7o3///qY2sbGxkEqlOHjwYJvX3BLKysogkUhMz3q1hz4ajUY89dRTePnll9G7d++b9rdUH0V9ADG1nnPnzuHDDz/Eu+++a9qWl5eHkJAQs3Z+fn6mfdb8TMCioiIYDAZTvQ38/Pxw5swZkapqGUajES+88ALuuece9OnTB0D9fw+FQnHTA6z9/PyQl5cnQpWW2bRpE9LS0nD48OGb9tlDHy9cuIBVq1YhMTERr732Gg4fPoznn38eCoUCU6ZMMfWjsT+3ttLH2bNnQ6vVIjQ0FDKZDAaDAf/+978xadIkALCLPjZoSl/y8vLg6+trtl8ul8PT09Pm+gvUz0t89dVXMXHiRNPDee2hj4sWLYJcLsfzzz/f6P6W6iNDlJWbPXs2Fi1adNs2p0+fRmhoqOnnq1evYtSoUXjsscfwzDPPtHaJdJemT5+OjIwM/PLLL2KX0qIuX76MWbNmISkpCSqVSuxyWoXRaET//v3x9ttvAwAiIyORkZGB1atXY8qUKSJX1zK+/PJLbNiwARs3bkTv3r2Rnp6OF154AQEBAXbTx/aqtrYWjz/+OARBwKpVq8Qup8Wkpqbigw8+QFpaGiQSSauei5fzrNw//vEPnD59+ravzp07m9rn5OTgvvvuw+DBg2+aMK7RaG6686nhZ41G0/qduQve3t6QyWSN1m/ttd/OjBkzsGPHDuzduxcdOnQwbddoNNDr9SgtLTVrb0v9TU1NRUFBAfr16we5XA65XI6ffvoJy5cvh1wuh5+fn8330d/fH7169TLb1rNnT2RnZwP4/f8rW/5z+/LLL2P27NmYMGECwsLC8NRTT+HFF1/EwoULAdhHHxs0pS8ajeamm1nq6upQXFxsU/1tCFBZWVlISkoyjUIBtt/Hn3/+GQUFBQgODjb93ZOVlYV//OMf6NSpE4CW6yNDlJXz8fFBaGjobV8Nc5yuXr2K4cOHIyoqCmvXroVUav6fNyYmBvv27UNtba1pW1JSEnr06GHVl/IAQKFQICoqCsnJyaZtRqMRycnJiImJEbEyywiCgBkzZuDrr7/Gnj17brrMGhUVBQcHB7P+ZmZmIjs722b6O2LECJw4cQLp6emmV//+/TFp0iTT7229j/fcc89NS1P89ttv6NixIwAgJCQEGo3GrI9arRYHDx60mT5WVlbe9HeJTCaD0WgEYB99bNCUvsTExKC0tBSpqammNnv27IHRaER0dHSb12yJhgB19uxZ/PDDD/Dy8jLbb+t9fOqpp3D8+HGzv3sCAgLw8ssv47vvvgPQgn20fD48WZMrV64IXbt2FUaMGCFcuXJFyM3NNb0alJaWCn5+fsJTTz0lZGRkCJs2bRKcnJyEjz76SMTKm27Tpk2CUqkU1q1bJ5w6dUqYNm2a4O7uLuTl5YldWrM999xzglqtFn788Uez/1aVlZWmNs8++6wQHBws7NmzRzhy5IgQExMjxMTEiFj13bvx7jxBsP0+Hjp0SJDL5cK///1v4ezZs8KGDRsEJycn4YsvvjC1eeeddwR3d3fhf//7n3D8+HHh4YcfFkJCQoSqqioRK2+6KVOmCIGBgcKOHTuEixcvClu3bhW8vb2FV155xdTGlvpYXl4uHD16VDh69KgAQHjvvfeEo0ePmu5Ma0pfRo0aJURGRgoHDx4UfvnlF6Fbt27CxIkTxerSTW7XR71eL4wZM0bo0KGDkJ6ebvb3z413bttyHxvzx7vzBKFl+sgQZSfWrl0rAGj0daNjx44JQ4YMEZRKpRAYGCi88847IlVsmQ8//FAIDg4WFAqFMHDgQOHAgQNil2SRW/23Wrt2ralNVVWV8Pe//13w8PAQnJychEceecQsFNuiP4Yoe+jjN998I/Tp00dQKpVCaGiosGbNGrP9RqNRmDt3ruDn5ycolUphxIgRQmZmpkjVNp9WqxVmzZolBAcHCyqVSujcubPwz3/+0+wL15b6uHfv3kb/35syZYogCE3ry7Vr14SJEycKLi4ugpubmzB16lShvLxchN407nZ9vHjx4i3//tm7d6/pGLbcx8Y0FqJaoo8SQbhh2VkiIiIiahLOiSIiIiKyAEMUERERkQUYooiIiIgswBBFREREZAGGKCIiIiILMEQRERERWYAhioiIiMgCDFFEREREFmCIIiIiIrIAQxQRERGRBRiiiIjsSG1trdglELUbDFFEZBOGDx+O559/Hq+88go8PT2h0WiwYMEC0/7S0lI8/fTT8PHxgZubG+6//34cO3YMAFBWVgaZTIYjR44AAIxGIzw9PTFo0CDT+7/44gsEBQUBAPR6PWbMmAF/f3+oVCp07NgRCxcuNLWVSCRYtWoVHnjgATg6OqJz58746quvzOp99dVX0b17dzg5OaFz586YO3euWcBZsGABIiIi8NFHHyEoKAhOTk54/PHHUVZWZnacTz75BD179oRKpUJoaCj+85//mPZdunQJEokEmzdvxrBhw6BSqbBhw4a7/KSJqKkYoojIZqxfvx7Ozs44ePAgFi9ejDfffBNJSUkAgMceewwFBQXYtWsXUlNT0a9fP4wYMQLFxcVQq9WIiIjAjz/+CAA4ceIEJBIJjh49ioqKCgDATz/9hGHDhgEAli9fju3bt+PLL79EZmYmNmzYgE6dOpnVMnfuXIwbNw7Hjh3DpEmTMGHCBJw+fdq039XVFevWrcOpU6fwwQcf4OOPP8b7779vdoxz587hyy+/xDfffIPdu3fj6NGj+Pvf/27av2HDBsybNw///ve/cfr0abz99tuYO3cu1q9fb3ac2bNnY9asWTh9+jTi4uJa5LMmoiYQiIhswLBhw4QhQ4aYbRswYIDw6quvCj///LPg5uYmVFdXm+3v0qWL8NFHHwmCIAiJiYnC6NGjBUEQhGXLlgnjx48XwsPDhV27dgmCIAhdu3YV1qxZIwiCIMycOVO4//77BaPR2GgtAIRnn33WbFt0dLTw3HPP3bL+JUuWCFFRUaaf58+fL8hkMuHKlSumbbt27RKkUqmQm5trqn/jxo1mx3nrrbeEmJgYQRAE4eLFiwIAYdmyZbc8LxG1HrnYIY6IqKn69u1r9rO/vz8KCgpw7NgxVFRUwMvLy2x/VVUVzp8/DwAYNmwYPv30UxgMBvz0008YOXIkNBoNfvzxR/Tt2xfnzp3D8OHDAQB/+ctf8Kc//Qk9evTAqFGj8NBDD2HkyJFmx46Jibnp5/T0dNPPmzdvxvLly3H+/HlUVFSgrq4Obm5uZu8JDg5GYGCg2TGMRiMyMzPh6uqK8+fPIyEhAc8884ypTV1dHdRqtdlx+vfv34RPj4haGkMUEdkMBwcHs58lEgmMRiMqKirg7+9vulx3I3d3dwDA0KFDUV5ejrS0NOzbtw9vv/02NBoN3nnnHYSHhyMgIADdunUDAPTr1w8XL17Erl278MMPP+Dxxx9HbGzsTfOebiUlJQWTJk3CG2+8gbi4OKjVamzatAlLly5tcl8bLjN+/PHHiI6ONtsnk8nMfnZ2dm7ycYmo5TBEEZHN69evH/Ly8iCXy2+au9TA3d0dffv2xYoVK+Dg4IDQ0FD4+vpi/Pjx2LFjh2k+VAM3NzeMHz8e48ePx6OPPopRo0ahuLgYnp6eAIADBw5g8uTJpvYHDhxAZGQkAGD//v3o2LEj/vnPf5r2Z2Vl3VRTdnY2cnJyEBAQYDqGVCpFjx494Ofnh4CAAFy4cAGTJk26q8+HiFoHQxQR2bzY2FjExMQgPj4eixcvRvfu3ZGTk4Nvv/0WjzzyiOly1/Dhw/Hhhx/i0UcfBQB4enqiZ8+e2Lx5M1auXGk63nvvvQd/f39ERkZCKpViy5Yt0Gg0plEtANiyZQv69++PIUOGYMOGDTh06BA+/fRTAEC3bt2QnZ2NTZs2YcCAAfj222/x9ddf31S3SqXClClT8O6770Kr1eL555/H448/Do1GAwB444038Pzzz0OtVmPUqFGoqanBkSNHUFJSgsTExNb6OImoiXh3HhHZPIlEgp07d2Lo0KGYOnUqunfvjgkTJiArKwt+fn6mdsOGDYPBYDDNfQLqg9Uft7m6umLx4sXo378/BgwYgEuXLmHnzp2QSn//K/ONN97Apk2b0LdvX3z++ef473//i169egEAxowZgxdffBEzZsxAREQE9u/fj7lz595Ud9euXTF27Fg8+OCDGDlyJPr27Wu2hMHTTz+NTz75BGvXrkVYWBiGDRuGdevWISQkpAU/PSKylEQQBEHsIoiIbIlEIsHXX3+N+Ph4i4+xYMECbNu2zWwyOhHZFo5EEREREVmAIYqIiIjIArycR0RERGQBjkQRERERWYAhioiIiMgCDFFEREREFmCIIiIiIrIAQxQRERGRBRiiiIiIiCzAEEVERERkAYYoIiIiIgv8fwWF6nOdLaLjAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "sns.distplot(df[\"newspaper\"])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "id": "f1VioZBIa85Q"
      },
      "outputs": [],
      "source": [
        "iqr=df.newspaper.quantile(0.75)-df.newspaper.quantile(0.25)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "id": "8Bgs_gOebQDs",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "24781146-280b-46f8-fd14-2e37009e3ab7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "-35.775000000000006\n",
            "93.625\n"
          ]
        }
      ],
      "source": [
        "lower_bridge=df['newspaper'].quantile(0.25)-(iqr*1.5)\n",
        "upper_bridge=df['newspaper'].quantile(0.75)+(iqr*1.5)\n",
        "print(lower_bridge)\n",
        "print(upper_bridge)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "id": "QQa6CO9Vw2nz"
      },
      "outputs": [],
      "source": [
        "data=df.copy()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "id": "ipevBwuEw7ea"
      },
      "outputs": [],
      "source": [
        "data.loc[data['newspaper']>=93, 'newspaper']=93"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 428
        },
        "id": "HRhLSTJzxMIP",
        "outputId": "a28651bd-4551-4ef9-8e96-ca96720a1bcc"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: ylabel='newspaper'>"
            ]
          },
          "metadata": {},
          "execution_count": 14
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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H584cWJ+/OMf99o4AIA9qShknnvuuZxyyimvOV5bW5utW7e+4VEAAHujopAZO3bsLn8g3ooVKzJhwoQ3ugkAYK9U9KqlpqamzJkzJ9u2bUtXV1eefPLJfPWrX83ChQtz55139vZGAIBdqihkLr744gwYMCDXXXddXn755Vx00UUZOXJk/vZv/7b7h+UBAOxvFYVMksycOTMzZ87Myy+/nJdeeinDhg3rzV0AAK+r4pBJkhdeeCHr169P8upbFLz5zW/ulVEAAHujopt9t2zZkg9+8IMZOXJkpkyZkilTpmTkyJGZNWtW2tvbe3sjAMAuVRQyF198cdasWZOHHnoomzdvzubNm/Pggw/mBz/4QT7+8Y/39kYAgF2q6FtLDz74YB5++OGcffbZ3cemT5+eZcuW5Q//8A97bRwAwJ5UdEXm6KOPTn19/WuO19fX58gjj3zDowAA9kZFIXPdddelqakpra2t3cdaW1tz1VVXZd68eb02DgBgTyr61tKSJUvyH//xH2lsbExjY2OSpKWlJbW1tfnlL3+ZL3zhC93PXbduXe8sBQD4LRWFzHnnndfLMwAA9l1FIXPDDTf09g4AgH1W0T0yAAB9QUVXZHbu3Jnbb7899913X1paWrJjx44ej7/44ou9Mg4AYE8quiIzf/783HbbbbngggvS3t6epqamnH/++enXr1/+6q/+qpcnAgDsWkUhc++992bZsmX5i7/4ixx++OH5kz/5k9x55525/vrrs3r16t7eCACwSxWFTGtra0444YQkyaBBg7rfX+mP/uiP8tBDD/XeOgCAPagoZI455pj84he/SJIce+yx+ad/+qckyVNPPZXa2treWwcAsAcVhcwf//EfZ+XKlUmSyy67LPPmzcu4cePyoQ99KB/96Ed7dSAAwO5U9KqlT3/6092/vuCCC9LY2JhVq1Zl3Lhxee9739tr4wAA9qSikPltkyZNyqRJk3rjVAAAe63ikFm/fn3uuOOO/PSnP02STJgwIZdddll+53d+p9fGAQDsSUX3yDzwwAM5/vjjs3bt2px00kk56aSTsm7duhx//PF54IEHensjAMAuVXRF5uqrr87cuXNz44039jh+ww035Oqrr86MGTN6ZRwAwJ5UdEXmF7/4RT70oQ+95visWbO6X5YNALC/VRQyU6dOzT//8z+/5vgTTzyR3//933/DowAA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\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "sns.boxplot(data[\"newspaper\"])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 411
        },
        "id": "PF3clDq2xSXD",
        "outputId": "3dedd0ff-9b93-4a7d-b666-a2b78c3bfa19"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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4/jjjz/o55kzZ07MmTPnAx9TVVUVjY2NpcwEAEa4kl6Ruf/+++PRRx+NGTNmxDXXXBNTpkyJiIhnn322+JbTUHn55Zejvr4+PvrRj8aNN94Yb7311gc+vq+vL/L5/IADABiZSnpFZsaMGbF79+7I5/Nx3HHHFc8vXLgwjjnmmCEbN3v27Jg3b15MnDgxtmzZErfffnvMmTMnXn311TjqqKMO+DFtbW1xzz33DNkGAKB8lRQyERGFQiHWr18fW7ZsiQULFkRNTU2MHj16SEPm6quvLv7+zDPPjLPOOitOPvnkePnll+OSSy454McsWbIkFi9eXLydz+ejubl5yDYBAOWjpJDp6OiI2bNnR2dnZ/T19cVll10WNTU1cf/990dfX1888sgjQ70zIiJOOumkGDt2bGzevHnQkKmqqipeiAwAjGwlXSPzla98JT7xiU/EP/7xjxgzZkzx/FVXXRUvvfTSkI3737Zt2xZvvfVWjBs37rD9GQBAOkp6Rea3v/1tvPLKKzF69OgB50888cT429/+dtDPs3fv3ti8eXPx9tatW2PDhg1RV1cXdXV1cc8998T8+fOjsbExtmzZErfddluccsopMWvWrFJmAwAjTEkh09/fH//617/ed37btm1RU1Nz0M/z+uuvx8UXX1y8/d61Ldddd10sW7YsNm7cGI8//nh0d3dHU1NTzJw5M+677z5vHQEAEVFiyMycOTMefPDB4s9WqqioiL1798bdd98dl19++UE/z4wZM6JQKAx6//PPP1/KPADgCFFSyHz3u9+NWbNmxemnnx779u2LBQsWxJtvvhljx471nXcBgGFTUsiMHz8+/vznP8eTTz4ZGzdujL1798YNN9wQ11577YCLfwEADqeSv4/MqFGj4vOf//xQbgEAOCQHHTLPPvvsQT/pez9EEgDgcDrokJk7d+5BPa6iouKAX9EEADDUDjpk+vv7D+cOAIBDVtJ39gUAKAclX+zb29sb7e3t0dnZGe+8886A+7785S//x8MAAD5MSSHzpz/9KS6//PJ4++23o7e3N+rq6mL37t1xzDHHRH19vZABAIZFSW8t3XLLLXHFFVcUf2jkunXroqOjI84555z4zne+M9QbAQAOqKSQ2bBhQ3z1q1+NysrKOOqoo6Kvry+am5vjgQceiNtvv32oNwIAHFBJIXP00UdHZeW7H1pfXx+d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\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "sns.boxplot(data['sales']);"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 392
        },
        "id": "lqgHXHXaxnvX",
        "outputId": "f0d667d3-35fa-410e-e33d-b19c43cfae3f"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1200x400 with 3 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAABJ4AAAGOCAYAAADW/cnWAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAACsWklEQVR4nO39eXxU5d0//r+yTZIhZBISw6IEIokLshiLWkhYFOu+IbWK3vcXxba/VpG2dnHFDS1qrXeLVrsJen9uRWtVVKptFSsCbgWDgFpLMBIsYExMJiSTZLKc3x844yznnDlz5izXOef1fDx8PCSTmVznzDnv93WuNUuSJAlEREREREREREQGy7a7AERERERERERE5E5seCIiIiIiIiIiIlOw4YmIiIiIiIiIiEzBhiciIiIiIiIiIjIFG56IiIiIiIiIiMgUbHgiIiIiIiIiIiJTsOGJiIiIiIiIiIhMwYYnIiIiIiIiIiIyhesbniRJQmdnJyRJsrsoRERkIMZ3IiJ3YnwnInIX1zc8HThwAIFAAAcOHLC7KEREZCDGdyIid2J8JyJyF9c3PBERERERERERkT3Y8ERERERERERERKZgwxMREREREREREZmCDU9ERERERERERGQKNjwREREREREREZEp2PBERERERERERESmYMMTERERERERERGZgg1PRERERERERERkCjY8ERERERERERGRKdjwREREREREREREpsi1uwBERGSNYCiM1q4wOnv7UVyYh/JhPgT8PruLReR4vLeIiIhIVCLUU9jwRETkAXs7enDt09uwYWdr9Gezaspx1/wpGFNSaGPJiJyN9xYRERGJSpR6CqfaERG5XDAUTko4APD6zlZc9/Q2BENhm0pG5Gy8t4iIiEhUItVT2PBERORyrV3hpIQT8frOVrR28eGYSA/eW0RERCQqkeopbHgiInK5zt5+1dcPpHidiOTx3iIiIiJRiVRPYcMTEZHLFRfkqb4+PMXrRCSP9xYRERGJSqR6ChueiIhcrrzIh1k15bKvzaopR3kRd98i0oP3FhEREYlKpHoKG56IiFwu4PfhrvlTkhLPrJpy3D1/Crd9J9KJ9xYRERGJSqR6SpYkSZJlf80GnZ2dCAQCCAaDKC4utrs4RES2CYbCaO0K40BvP4YX5KG8yOfoB2PGdxKF2+4tIrsxvhMRGUeEekqupX+N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UVxcnNFnBUNhtHaFcaC3H8ML8lBe5GMwJiKyiZHxPVPMD0RExhEpvnsF8xgRmSnX7gI4ScDPAExERMmYH4iIyMmYx4jITJxqR0REREREREREpmDDExERERERERERmYINT0REREREREREZAo2PBERERERERERkSnY8ERERERERERERKZgwxMREREREREREZmCDU9ERERERERERGQKNjwREREREREREZEp2PBERERERERERESmYMMTERERERERERGZItfuAogsGAqjtSuMzt5+FBfmoXyYDwG/z+5iERGRQzGvEBEREdmD9TD7sOFJwd6OHlz79DZs2Nka/dmsmnLcNX8KxpQU2lgyIiJyIuYVIiIiInuwHmYvTrWTEQyFky5KAHh9Zyuue3obgqGwTSUjIiInYl4hIiIisgfrYfZjw5OM1q5w0kUZ8frOVrR28cIkIiLtmFeIiIiI7MF6mP3Y8CSjs7df9fUDKV4nIiKKxbxCREREZA/Ww+zHhicZxQV5qq8PT/E6ERFRLOYVIiIiInuwHmY/NjzJKC/yYVZNuexrs2rKUV7Ele+JiEg75hUiIiIie7AeZj82PMkI+H24a/6UpItzVk057p4/hVsuEhFRWphXiIiIiOzBepj9siRJkuwuhJk6OzsRCAQQDAZRXFyc1nuDoTBau8I40NuP4QV5KC/y8aIkIhJEJvHdLswrRESpOTG+E5H4WA+zT67dBRBZwM8LkYiIjMO8QkRERGQP1sPsw6l2RERERERERERkCjY8ERERERERERGRKdjwREREREREREREpmDDExERERERERERmYINT0REREREREREZAo2PBERERERERERkSnY8ERERERERERERKZgwxMREREREREREZki1+4CmE2SJABAZ2enzSUhIqJUhg8fjqysLE2/y/hOROQcjO9ERO6kJb67vuHpwIEDAICxY8faXBIiIkolGAyiuLhY0+8yvhMROQfjOxGRO2mJ71lSpEvBpYaGhrB37960ellidXZ2YuzYsdizZ4/mZOkUbj42gMfndDw+58rk2NKJ1ZnEdzeffyPw/CjjuVHGc6OM58a6+B7Bc34Qz8NXeC4O4nn4Cs/FQZmeB454ApCdnY3DDjss488pLi527cXo5mMDeHxOx+NzLrOPzYj47ubzbwSeH2U8N8p4bpTx3GhjVP0d4DmP4Hn4Cs/F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IiIiIiIiU7DhiYiIiIiIiIiITMGGJyIiIiIiIiIiMgUbnoiIiIiIiIiIyBRseCIiIiIiIiIiIlOw4YmIiIiIiIiIiEzBhiciIiIiIiIiCzzyyCMoKSmJ/vvWW2/Fsccea1t5iKzAhiciwWRlZan+d8455yArKwtvvfWW7Pvnzp2LCy64wOJSExERERFRun7yk59g3bp1dheDyFS5dheAiOLt27cv+v9PPvkkbr75Znz00UfRnxUVFaG+vh4rV67E17/+9bj3fvLJJ/jHP/6BF154wbLyEhGR+/X39yMvL8/uYhARCSMcDsPn82X8OUVFRSgqKjKgRETi4ognIsGMGjUq+l8gEEBWVlbcz4qKinDFFVfgySefRCgUinvvI488gtGjR+P000+3qfRERM4yZ84cLFmyBD/72c8wYsQIjBo1Crfeemv09Y6ODnz729/GIYccguLiYpx88sl47733AADBYBA5OTnYvHkzAGBoaAgjRoyI6xT4v//7P4wdOxbAwYeUxYsXY/To0SgoKMC4ceOwfPny6O9mZWXhoYcewhlnnIHCwkIcfvjh+POf/xxX3muvvRZHHHEE/H4/Dj/8cCxduhT9/f3R1yNTNn73u99h7Nix8Pv9+Na3voVgMBj3OX/84x9x9NFHo6CgAEcddRQefPDB6GuffPIJsrKy8OSTT2L27NkoKCjAY489luGZJiJytjlz5mDx4sX44Q9/iPLycpx22mm47777MHnyZAwbNgxjx47FlVdeia6urrj3PfLII6isrITf78e8efPQ1tYW93riVLuhoSHcfvvtOOyww5Cfn49jjz0Wf/3rX604RCLTsOGJyIEuvfRS9PX1xT2QSJKERx99FJdddhlycnJsLB0RkbM8+uijGDZsGN5++23cc889uP322/Hyyy8DAC688EK0tLTgpZdewpYtW3Dcccdh7ty5+OKLLxAIBHDsscfitddeAwBs374dWVlZaGhoiD54rF+/HrNnzwYArFixAs8//zz+9Kc/4aOPPsJjjz2G8ePHx5Vl6dKlmD9/Pt577z1ceumluPjii/Hhhx9GXx8+fDgeeeQRfPDBB/j1r3+NP/zhD/if//mfuM9obGzEn/70J7zwwgv461//ioaGBlx55ZXR1x977DHcfPPNuPPOO/Hhhx/i5z//OZYuXYpHH3007nOuu+46/OAHP8CHH36I0047zZBzTUTkZI8++ih8Ph82bdqE3/72t8jOzsaKFSvw/vvv49FHH8Wrr76Kn/3sZ9Hff/vtt3HFFVdg8eLF2Lp1K0466STccccdqn/j17/+NX75y1/i3nvvxbZt23Daaafh3HPPxc6dO80+PCLzSEQkrFWrVkmBQED2tYsvvliaPXt29N/r1q2TAEg7d+60pnBERC4we/Zsqb6+Pu5nxx9/vHTttddKGzZskIqLi6Xe3t641ydMmCD97ne/kyRJkq655hrprLPOkiRJkn71q19JF110kTR16lTppZdekiRJkqqrq6Xf//73kiRJ0tVXXy2dfPLJ0tDQkGxZAEjf+9734n524oknSt///vcVy/+LX/xC+trXvhb99y233CLl5ORIn376afRnL730kpSdnS3t27cvWv7HH3887nOWLVsmTZ8+XZIkSWpqapIASL/61a8U/y4RkdfMnj1bqq2tVf2dp556SiorK4v+e8GCBdKZZ54Z9zsXXXRRXP3+lltukaZOnRr995gxY6Q777wz7j3HH3+8dOWVV+ovPJHNOOKJyKEWLVqE119/Hbt27QIArFy5ErNnz0Z1dbXNJSMicpYpU6bE/Xv06NFoaWnBe++9h66uLpSVlUXX4CgqKkJTU1M09s6ePRsbN27E4OAg1q9fjzlz5mDOnDl47bXXsHfvXjQ2NmLOnDkAgMsuuwxbt27FkUceiSVLluDvf/97UlmmT5+e9O/YEU9PPvkk6urqolOvb7rpJjQ3N8e9p7KyEoceemjcZwwNDeGjjz5Cd3c3du3ahSuuuCLumO64447oMUVMmzYt/ZNJRORiX/va1+L+/corr2Du3Lk49NBDMXz4cPz3f/832traosthfPjhhzjxxBPj3pMY52N1dnZi7969qKuri/t5XV1dXC4gcho2PBE51Ny5c1FZWYlHHnkEnZ2deOaZZ3DFFVfYXSwiIsdJXDQ7KysLQ0ND6OrqwujRo7F169a4/z766CP89Kc/BQDMmjULBw4cwLvvvovXX389ruFp/fr1GDNmDGpqagAAxx13HJqamrBs2TL09PTgW9/6Fr75zW9qLuebb76JSy+9FGeeeSbWrl2LhoYG3HjjjQiHw5o/IzIF8A9/+EPcMe3YsSNpt9Rhw4Zp/lwiIi+IjYuffPIJzj77bEyZMgVPP/00tmzZgt/85jcAkFZcJvIC7mpH5FDZ2dm4/PLL8fDDD+PQQw+Fz+dL6wGGiIjUHXfccdi/fz9yc3OT1mKKKCkpwZQpU/DAAw8gLy8PRx11FCoqKnDRRRdh7dq10fWdIoqLi3HRRRfhoosuwje/+U2cfvrp+OKLLzBixAgAwFtvvYX/7//7/6K//9Zbb6G2thYA8MYbb2DcuHG48cYbo6/v3r07qUzNzc3Yu3cvxowZE/2M7OxsHHnkkRg5ciTGjBmDjz/+GJdeemlG54eIyMu2bNmCoaEh/PKXv0R29sHxHH/605/ifufoo4/G22+/HfezxEb+WMXFxRgzZgw2bdoUlz82bdqEE044wcDSE1mLDU9EDnb55Zfj9ttvxw033IAFCxagsLDQ7iIREbnGKaecgunTp+P888/HPffcgyOOOAJ79+7FX/7yF8ybNy86FW3OnDm4//77o43/I0aMwNFHH40nn3wy2vsNAPfddx9Gjx6N2tpaZGdn46mnnsKoUaNQUlIS/Z2nnnoK06ZNQ319PR577DG88847ePjhhwEANTU1aG5uxhNPPIHjjz8ef/nLX/Dss88mlbugoAALFy7Evffei87OTixZsgTf+ta3MGrUKADAbbfdhiVLliAQCOD0009HX18fNm/ejPb2dlxzzTVmnU4iIleprq5Gf38/7r//fpxzzjnRBcdjLVmyBHV1dbj33ntx3nnn4W9/+1vKHep++tOf4pZbbsGECRNw7LHHYtWqVdi6dSt3FyVH41Q7IgerrKzEKaecgvb2dixatMju4hARuUpWVhZefPFFzJo1C5dffjmOOOIIXHzxxdi9ezdGjhwZ/b3Zs2djcHAwupYTcLAxKvFnw4cPxz333INp06bh+OOPxyeffIIXX3wx2lMOHGwUeuKJJzBlyhT87//+L1avXo2JEycCAM4991z86Ec/wuLFi3HsscfijTfewNKlS5PKXV1djQsuuABnnnkmTj31VEyZMgUPPvhg9PVvf/vb+OMf/4hVq1Zh8uTJmD17Nh555BFUVVUZePaIiNxt6tSpuO+++3D33Xdj0qRJeOyxx7B8+fK43/n617+OP/zhD/j1r3+NqVOn4u9//ztuuukm1c9dsmQJrrnmGvz4xz/G5MmT8de//hXPP/98dNo2kRNlSZIk2V0IIiIiIq/LysrCs88+i/PPP1/3Z9x6661Ys2YNtm7dali5iIiIiDLBEU9ERERERERERGQKNjwREREREREREZEpONWOiIiIiIiIiIhMwRFPRERERERERERkCjY8ERERERERERGRKdjwREREREREREREpmDDExERERERERERmYINT0REREREREREZAo2PBERERERERERkSnY8ERERERERERERKZgwxMREREREREREZmCDU9ERERERERERGSK/z9+a6s3iPU0XwAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "sns.pairplot(data, x_vars=['TV', 'newspaper', 'radio'],\n",
        "             y_vars='sales', height=4, aspect=1, kind='scatter')\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 435
        },
        "id": "8eGk54A5yIvd",
        "outputId": "444e0440-596f-4386-a0df-0fbd6711ba59"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "sns.heatmap(data.corr(), cmap='YlGnBu',annot=True)\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "id": "MLf9ErKcye-P"
      },
      "outputs": [],
      "source": [
        "important_features=list(df.corr()['sales'][(df.corr()['sales']>+0.5)|(df.corr()['sales']<-0.5)].index)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FRvfB8_TzyPj",
        "outputId": "58d20fe5-8ded-4118-ea13-36430446b709"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['TV', 'radio', 'sales']\n"
          ]
        }
      ],
      "source": [
        "print(important_features)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "id": "ZAwO6Szkz30j"
      },
      "outputs": [],
      "source": [
        "x=data['TV']\n",
        "y=data['sales']"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6kPK4vLC0pIF",
        "outputId": "912a1967-ae85-4041-a674-6e41aefb7109"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0      230.1\n",
              "1       44.5\n",
              "2       17.2\n",
              "3      151.5\n",
              "4      180.8\n",
              "       ...  \n",
              "195     38.2\n",
              "196     94.2\n",
              "197    177.0\n",
              "198    283.6\n",
              "199    232.1\n",
              "Name: TV, Length: 200, dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ],
      "source": [
        "x"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 22,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6UMFwZSg1lpY",
        "outputId": "50183562-3ef5-4bb8-cc41-258ca9274d4a"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0      22.1\n",
              "1      10.4\n",
              "2       9.3\n",
              "3      18.5\n",
              "4      12.9\n",
              "       ... \n",
              "195     7.6\n",
              "196     9.7\n",
              "197    12.8\n",
              "198    25.5\n",
              "199    13.4\n",
              "Name: sales, Length: 200, dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ],
      "source": [
        "y"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3mD9OdBS10y4",
        "outputId": "bef2af04-1cd0-4692-d66b-8bdc1641737e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(200,) (200,)\n"
          ]
        }
      ],
      "source": [
        "print(x.shape,y.shape)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 24,
      "metadata": {
        "id": "9y-HI6n62DZt"
      },
      "outputs": [],
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.33)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 25,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WK_bxKVv2swb",
        "outputId": "053cb9fc-01e6-4794-c9a4-b01e3522eb84"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(134,) (134,)\n"
          ]
        }
      ],
      "source": [
        "print(x_train.shape,y_train.shape)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 26,
      "metadata": {
        "id": "ILHkW3R-21jJ"
      },
      "outputs": [],
      "source": [
        "from sklearn.metrics import mean_squared_error, r2_score\n",
        "from sklearn.model_selection import cross_val_score,GridSearchCV\n",
        "from sklearn.neighbors import KNeighborsRegressor\n",
        "from sklearn.svm import SVR\n",
        "from sklearn.tree import DecisionTreeRegressor\n",
        "from sklearn.ensemble import RandomForestRegressor"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x_train_reshaped = np.reshape(x_train.values, (-1, 1))\n",
        "x_test_reshaped = x_test.values.reshape(-1, 1)"
      ],
      "metadata": {
        "id": "c83YuDjQmvTN"
      },
      "execution_count": 27,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 28,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 74
        },
        "id": "s0uWaqtk3whc",
        "outputId": "c573e79b-6366-43b9-b984-b70ff482bd38"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "KNeighborsRegressor()"
            ],
            "text/html": [
              "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>KNeighborsRegressor()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">KNeighborsRegressor</label><div class=\"sk-toggleable__content\"><pre>KNeighborsRegressor()</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 28
        }
      ],
      "source": [
        "knn=KNeighborsRegressor().fit(x_train_reshaped, y_train)\n",
        "knn"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 29,
      "metadata": {
        "id": "Je_CV0RY4IhE"
      },
      "outputs": [],
      "source": [
        "knn_train_pred=knn.predict(x_train_reshaped)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 30,
      "metadata": {
        "id": "oeDMe1Fh4WoX"
      },
      "outputs": [],
      "source": [
        "knn_test_pred=knn.predict(x_test_reshaped)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 31,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1PhVYTYR8SuU",
        "outputId": "6b6484ce-3ec7-4a7e-fc7c-23a0be2ab88d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[16.52 12.9   7.72 15.46 10.98 11.14 17.9   8.28  7.18 17.54 11.42 15.36\n",
            "  9.26 18.82 10.94 11.62  7.18  7.18 17.78 15.1  17.54 10.22 16.52 12.92\n",
            " 19.78 12.56  9.66  7.72 14.82 18.3   9.18 11.08 16.4   5.96 16.34 17.04\n",
            "  5.96 10.98 19.78 16.64 17.96 17.48 18.34 17.78 14.04 13.28 14.04 16.86\n",
            " 19.78 18.3  11.78 12.98  7.38 18.34 11.22  9.62 10.22 19.62 13.28 15.1\n",
            "  9.8  15.14 15.92 16.86 12.92 15.14 11.14 15.14 11.42 16.52 12.92 10.98\n",
            " 15.14  9.78 10.66 10.82 17.04 18.3  14.66 14.66  9.64 19.02 10.46  9.32\n",
            "  5.96 17.72 18.34 11.22 17.78 13.26 11.22 12.92 12.98  9.64 11.42 18.3\n",
            "  8.28 11.42 19.78 18.82 16.28  8.86 18.34 14.66  5.96 12.9  18.3  16.86\n",
            " 13.78  4.52 15.1   7.18 18.82 17.04  4.52 12.6  18.34 14.66 15.1  11.1\n",
            " 16.64 14.82 11.22 18.3  18.98 17.54 17.72 16.28  5.96  9.78 11.42  7.72\n",
            "  7.34 16.34] [12.98 18.22 18.82  7.34 17.08 12.6  10.98 21.2  18.22  8.86 12.92 13.3\n",
            " 16.16 17.78  8.86 17.72 12.6  18.82 16.38  8.28 17.04 12.6  17.78 19.68\n",
            " 16.84  5.98 18.9  18.   17.68  5.16 18.3  17.46 16.86  9.78  9.5  18.\n",
            " 19.78 19.18 16.86  9.58 16.54 13.28 16.86 12.56 18.34 11.42 16.86 17.04\n",
            " 11.42  9.26 10.98 17.96 18.82 13.26  9.8  14.04 18.98 11.14 16.86 10.66\n",
            " 11.64 17.52  9.32 15.04 17.9  15.36]\n"
          ]
        }
      ],
      "source": [
        "print(knn_train_pred, knn_test_pred)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 32,
      "metadata": {
        "id": "uZDQ9VfF8bvO"
      },
      "outputs": [],
      "source": [
        "Results=pd.DataFrame(columns=[\"Model\",\"Train R2\",\"Test R2\"\"Test RMSE\",\"Variance\"])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 33,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jjiwCnMf81qe",
        "outputId": "7a8e1710-3dba-4c4c-b1f8-a294a9f5d7f5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "R2: 0.5325612534333353\n",
            "RMSE: 3.6321852509157204\n"
          ]
        }
      ],
      "source": [
        "r2=r2_score(y_test,knn_test_pred)\n",
        "r2_train=r2_score(y_train,knn_train_pred)\n",
        "rmse=np.sqrt(mean_squared_error(y_test,knn_test_pred))\n",
        "variance=r2_train-r2\n",
        "Results=Results.append({\"Model\":\"K-Nearest Neighbors\",\"Train R2\":r2_train,\"Test R2\":r2_train,\"Test R2\":r2,\"Test RMSE\":rmse,\"variance\":variance},ignore_index=True)\n",
        "print(\"R2:\",r2)\n",
        "print(\"RMSE:\",rmse)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 34,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 81
        },
        "id": "PyEW0T7-Av9m",
        "outputId": "c07321ea-6f2d-42ec-fba5-5273ec945954"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                 Model  Train R2 Test R2Test RMSE Variance   Test R2  \\\n",
              "0  K-Nearest Neighbors  0.643538              NaN      NaN  0.532561   \n",
              "\n",
              "   Test RMSE  variance  \n",
              "0   3.632185  0.110977  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-1ef3ff2c-6e8e-44a2-b0b6-6c8f3e00f202\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Model</th>\n",
              "      <th>Train R2</th>\n",
              "      <th>Test R2Test RMSE</th>\n",
              "      <th>Variance</th>\n",
              "      <th>Test R2</th>\n",
              "      <th>Test RMSE</th>\n",
              "      <th>variance</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>K-Nearest Neighbors</td>\n",
              "      <td>0.643538</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0.532561</td>\n",
              "      <td>3.632185</td>\n",
              "      <td>0.110977</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-1ef3ff2c-6e8e-44a2-b0b6-6c8f3e00f202')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-1ef3ff2c-6e8e-44a2-b0b6-6c8f3e00f202 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-1ef3ff2c-6e8e-44a2-b0b6-6c8f3e00f202');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "Results",
              "repr_error": "'str' object has no attribute 'empty'"
            }
          },
          "metadata": {},
          "execution_count": 34
        }
      ],
      "source": [
        "Results.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 35,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 74
        },
        "id": "DooJw01iCTwu",
        "outputId": "bdd5365f-97fd-4870-cc92-ce7dcfde4abb"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "SVR()"
            ],
            "text/html": [
              "<style>#sk-container-id-2 {color: black;background-color: white;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>SVR()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" checked><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">SVR</label><div class=\"sk-toggleable__content\"><pre>SVR()</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 35
        }
      ],
      "source": [
        "svr=SVR().fit(x_train_reshaped,y_train)\n",
        "svr"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 36,
      "metadata": {
        "id": "slpoNjnxCejJ"
      },
      "outputs": [],
      "source": [
        "svr_train_pred=svr.predict(x_train_reshaped)\n",
        "svr_test_pred=svr.predict(x_test_reshaped)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 37,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aeTSBhuHCxsF",
        "outputId": "d6fac96c-e8e2-4371-a960-1a07f393c08b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[16.88984344 12.42703114  7.87930617 16.77938402 10.29436367 11.45362068\n",
            " 16.52537646  8.17581367  7.93428992 15.88015446 10.61162751 17.02899885\n",
            "  9.37061256 16.71362631 11.44092057 11.29190223  7.95561497  7.9628068\n",
            " 16.22502769 13.85894217 15.88015446 11.59275579 16.81558867 13.45272853\n",
            " 17.32377226 12.14773246  8.71074279  7.86930939 15.2183251  17.5114699\n",
            "  8.45523487 11.71444767 16.9900454   7.63787503 16.49981916 14.72603313\n",
            "  7.63104285 10.26534412 17.31875407 16.05871338 17.58974092 17.16101483\n",
            " 17.21369154 16.06680522 13.08426683 13.55257323 12.9761799  17.58471538\n",
            " 17.27164575 17.47954345 10.39992669 12.80551678  7.90301937 17.24993871\n",
            " 11.08863035  9.54989879 11.58014302 17.49992674 13.63328909 14.07897439\n",
            "  9.09978266 16.5581236  15.0927341  17.58105374 13.46265978 16.56699293\n",
            " 11.53805482 16.59781918 10.6717236  16.88601065 12.00818131 10.2216344\n",
            " 16.59781918  8.838417   10.84473133 10.18260284 14.90661295 17.44052409\n",
            " 15.39213899 15.3596558   9.01365113 16.59624836  9.99503611  9.75369513\n",
            "  7.61774581 17.22399562 17.31999003 11.15396269 16.32271417 13.30032761\n",
            " 11.26188155 13.44776737 12.10955729  9.01870231 10.62090384 17.53697358\n",
            "  8.12295313 10.66711757 17.30601843 16.88567376 16.02845928  8.19652707\n",
            " 17.35804804 15.46231233  7.6355841  12.37491412 17.46600933 17.58967355\n",
            " 13.25178488  7.49912041 13.98940672  7.93077261 16.89300529 14.7151048\n",
            "  7.54683972 12.55864176 17.26076739 15.46231233 13.98415886 11.81082394\n",
            " 16.19282485 15.15284959 11.20158857 17.50288313 17.55903673 15.76034667\n",
            " 17.1825059  16.03351243  7.60704203  8.77426802 10.6717236   7.87930617\n",
            "  7.75456863 16.49981916] [12.10955729 17.12303705 16.7607747   7.751695   17.47488804 12.57191374\n",
            " 10.32328566 16.99945655 17.11980822  8.27707422 11.89048557 13.20835543\n",
            " 14.35128436 16.36657351  8.24706932 17.21234637 12.59408089 16.74123608\n",
            " 16.71344517  8.17169606 14.84090639 12.68784921 16.19363507 17.53778983\n",
            " 16.31851741  7.71277417 17.40442993 17.369253   17.56118763  7.56954448\n",
            " 17.48442451 15.66542642 17.590252    8.76445242  8.32496577 17.369253\n",
            " 17.26892697 17.24959961 17.58105374  9.85980864 14.99423208 13.50250346\n",
            " 17.590252   12.24149778 17.32489032 10.63016896 17.58846299 14.78070965\n",
            " 10.5930411   9.28351716 10.33290446 17.59146458 16.62500347 13.38354435\n",
            "  9.08962285 13.05591912 17.56248785 11.51698117 17.58987869 10.75416078\n",
            " 10.53232369 16.39867514  9.68766602 16.29462798 16.45742209 17.03248488]\n"
          ]
        }
      ],
      "source": [
        "print(svr_train_pred,svr_test_pred)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 38,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gmgE4Us0DCAN",
        "outputId": "e508e8ab-a69a-4015-9f01-25954ed392fa"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "R2: 0.5131223034119103\n",
            "RMSE: 3.706940168337255\n"
          ]
        }
      ],
      "source": [
        "r2=r2_score(y_test,svr_test_pred)\n",
        "r2_train=r2_score(y_train,svr_train_pred)\n",
        "rmse=np.sqrt(mean_squared_error(y_test,svr_test_pred))\n",
        "variance=r2_train-r2\n",
        "Results=Results.append({\"Model\":\"Support Vector Machine\",\"Train R2\":r2_train,\"Test R2\":r2_train,\"Test R2\":r2,\"Test RMSE\":rmse,\"variance\":variance},ignore_index=True)\n",
        "print(\"R2:\",r2)\n",
        "print(\"RMSE:\",rmse)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 39,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 112
        },
        "id": "AwplHcd9ED6S",
        "outputId": "59fc922a-8485-49bd-bcee-3556b5910e94"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                    Model  Train R2 Test R2Test RMSE Variance   Test R2  \\\n",
              "0     K-Nearest Neighbors  0.643538              NaN      NaN  0.532561   \n",
              "1  Support Vector Machine  0.589520              NaN      NaN  0.513122   \n",
              "\n",
              "   Test RMSE  variance  \n",
              "0   3.632185  0.110977  \n",
              "1   3.706940  0.076398  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-a715b510-4f10-48ee-9f03-544edf24c997\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Model</th>\n",
              "      <th>Train R2</th>\n",
              "      <th>Test R2Test RMSE</th>\n",
              "      <th>Variance</th>\n",
              "      <th>Test R2</th>\n",
              "      <th>Test RMSE</th>\n",
              "      <th>variance</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>K-Nearest Neighbors</td>\n",
              "      <td>0.643538</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0.532561</td>\n",
              "      <td>3.632185</td>\n",
              "      <td>0.110977</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Support Vector Machine</td>\n",
              "      <td>0.589520</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0.513122</td>\n",
              "      <td>3.706940</td>\n",
              "      <td>0.076398</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a715b510-4f10-48ee-9f03-544edf24c997')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-a715b510-4f10-48ee-9f03-544edf24c997 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-a715b510-4f10-48ee-9f03-544edf24c997');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-c96dd08b-1923-4f19-b9e5-537c6bc341c0\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-c96dd08b-1923-4f19-b9e5-537c6bc341c0')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-c96dd08b-1923-4f19-b9e5-537c6bc341c0 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "Results",
              "repr_error": "'str' object has no attribute 'empty'"
            }
          },
          "metadata": {},
          "execution_count": 39
        }
      ],
      "source": [
        "Results.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 40,
      "metadata": {
        "id": "_uq_dbpDEKfX"
      },
      "outputs": [],
      "source": [
        "import statsmodels.api as sm"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 41,
      "metadata": {
        "id": "amLDgwTBEV7w"
      },
      "outputs": [],
      "source": [
        "x_train_constant=sm.add_constant(x_train)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 42,
      "metadata": {
        "id": "ykUbcC5yEesG"
      },
      "outputs": [],
      "source": [
        "model=sm.OLS(y_train, x_train_constant).fit()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 43,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DGU7O3AEEscS",
        "outputId": "6b64a8c8-ada8-4093-a1f1-157140f22eb1"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "const    7.043069\n",
              "TV       0.046977\n",
              "dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 43
        }
      ],
      "source": [
        "model.params"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 44,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fVnlihODEwED",
        "outputId": "00fad146-b896-4f5c-a58b-4439b43233d8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                            OLS Regression Results                            \n",
            "==============================================================================\n",
            "Dep. Variable:                  sales   R-squared:                       0.604\n",
            "Model:                            OLS   Adj. R-squared:                  0.601\n",
            "Method:                 Least Squares   F-statistic:                     201.4\n",
            "Date:                Sat, 24 Feb 2024   Prob (F-statistic):           2.47e-28\n",
            "Time:                        06:40:38   Log-Likelihood:                -346.46\n",
            "No. Observations:                 134   AIC:                             696.9\n",
            "Df Residuals:                     132   BIC:                             702.7\n",
            "Df Model:                           1                                         \n",
            "Covariance Type:            nonrobust                                         \n",
            "==============================================================================\n",
            "                 coef    std err          t      P>|t|      [0.025      0.975]\n",
            "------------------------------------------------------------------------------\n",
            "const          7.0431      0.541     13.011      0.000       5.972       8.114\n",
            "TV             0.0470      0.003     14.191      0.000       0.040       0.054\n",
            "==============================================================================\n",
            "Omnibus:                        0.394   Durbin-Watson:                   2.043\n",
            "Prob(Omnibus):                  0.821   Jarque-Bera (JB):                0.295\n",
            "Skew:                          -0.115   Prob(JB):                        0.863\n",
            "Kurtosis:                       2.993   Cond. No.                         317.\n",
            "==============================================================================\n",
            "\n",
            "Notes:\n",
            "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n"
          ]
        }
      ],
      "source": [
        "print(model.summary())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 45,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 430
        },
        "id": "_c-xHoyRE_BC",
        "outputId": "a850bcb7-90fd-4b74-ea36-a31400e37472"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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kGKJgacJtSZ0zHrJTktSs1lERERhLaSDjwizCasWpgOAJABx/rxqYTrrfRAREakopIMPAMjLSMHauybDanEdWrFaYrD2rsms80FERKSysCgylpeRgrnpVlY4JSIi0oGwCD6AjiGYnBH9tG4GERFR2Av5YRciIiLSFwYfREREpCoGH0RERKQqBh9ERESkKgYfREREpCoGH0RERKQqBh9ERESkKgYfREREpCoGH0RERKQq3VU4FUIAAOrr6zVuCREREfnKed12Xse90V3w0dDQAAAYPHiwxi0hIiIifzU0NMBisXg9xiR8CVFU5HA4cPbsWcTHx8Nkkm/ht/r6egwePBinTp1CQkKCbI8bqni+/MPz5T+eM//wfPmH58s/cpwvIQQaGhqQmpoKs9l7Vofuej7MZjMGDRqk2OMnJCTwg+gHni//8Hz5j+fMPzxf/uH58k+w56unHg8nJpwSERGRqhh8EBERkarCJviIjo7GqlWrEB0drXVTDIHnyz88X/7jOfMPz5d/eL78o/b50l3CKREREYW2sOn5ICIiIn1g8EFERESqYvBBREREqmLwQURERKoKi+DjlVdewbBhwxATE4Np06Zh165dWjdJF55++mmYTCaXf2PGjOnc39zcjGXLlqFfv37o06cP7rjjDpw7d07DFqtv69atWLhwIVJTU2EymfDhhx+67BdC4Je//CVSUlIQGxuLOXPm4NixYy7HXLx4EUuWLEFCQgISExNx//33o7GxUcVXoZ6eztc999wj+czl5eW5HBNO52v16tWYOnUq4uPjMXDgQNx66604cuSIyzG+/B2ePHkSt9xyC+Li4jBw4ED87Gc/Q3t7u5ovRRW+nK/c3FzJZ+yhhx5yOSZcztfatWsxYcKEzsJhOTk5+OSTTzr3a/nZCvng4/3338djjz2GVatWYc+ePcjMzMT8+fNx/vx5rZumC+PGjUN1dXXnv23btnXue/TRR7Fp0yb8+c9/RlFREc6ePYvbb79dw9aqr6mpCZmZmXjllVfc7n/hhRfw0ksv4Q9/+AN27tyJ3r17Y/78+Whubu48ZsmSJTh48CA2b96Mjz76CFu3bsWDDz6o1ktQVU/nCwDy8vJcPnPvvvuuy/5wOl9FRUVYtmwZduzYgc2bN6OtrQ3z5s1DU1NT5zE9/R3a7XbccsstaG1txZdffom33noL69atwy9/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\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "plt.scatter(x_train, y_train)\n",
        "plt.plot(x_train, 6.9955+0.0541*x_train,\"y\")\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 46,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BiH4WhiWFXg3",
        "outputId": "37ea0ab9-1357-4795-d4d8-178f396638db"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "43    -3.862617\n",
              "164   -0.648777\n",
              "192   -1.951074\n",
              "14     2.368918\n",
              "83     3.343702\n",
              "         ...   \n",
              "195   -1.237592\n",
              "80     1.167886\n",
              "2      1.448926\n",
              "22    -2.063166\n",
              "152    0.274269\n",
              "Length: 134, dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 46
        }
      ],
      "source": [
        "y_train_pred=model.predict(x_train_constant)\n",
        "res=(y_train-y_train_pred)\n",
        "res"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 47,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "H3a7GpYXFnla",
        "outputId": "d883f1e6-9b86-402c-c7bc-7d71a9d540b5"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "43     16.762617\n",
              "164    12.548777\n",
              "192     7.851074\n",
              "14     16.631082\n",
              "83     10.256298\n",
              "         ...    \n",
              "195     8.837592\n",
              "80     10.632114\n",
              "2       7.851074\n",
              "22      7.663166\n",
              "152    16.325731\n",
              "Length: 134, dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 47
        }
      ],
      "source": [
        "y_train_pred"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 48,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 504
        },
        "id": "me29Y6GlGdID",
        "outputId": "b9dd4091-d2f1-4c51-edb6-e958857a796e"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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wqVLl5qs/+abbwAAQ4cObdOVkbt17733AgC2bdvWac+pDaamppg9ezZcXV1RUFCA/Px8sUsi6pIYgIioQ1lYWODJJ5+EWq3GrFmzoFQqNetSU1Px3nvvAQBeeumlTq3r1VdfhZmZGWbPno2tW7c2WV9dXY3vv/8e165d69S6/mr79u04cuRIk+VJSUnIy8uDpaVlo8Emiaj1eAuMyEDdbsb37t2745133tHac8XFxeHIkSPYvXs3fHx8EBERoRkIsaqqCi+99NIde5hpm6+vLzZu3IjHHnsMkyZNgq+vL/r06QMLCwtkZ2cjOTkZSqUSJ06cQLdu3Tq1tgb79u3Dp59+Cnd3dwwcOBDW1tbIycnBwYMHoVar8e9//xtyuVyU2oi6OgYgIgO1fv36FtcFBARoNQBZWVlh//79WLx4MTZv3owff/wRcrkcQUFB+Oc//4kpU6Zo7bna4uGHH8apU6ewZMkS7N69G7t374axsTHc3Nzw0EMPYeLEifD39xelNqA+pBoZGeHAgQNITExESUkJXFxc8MADD+Dll1/G6NGjRauNqKvjbPBERERkcNgGiIiIiAwOAxAREREZHAYgIiIiMjgMQERERGRwGICIiIjI4DAAERERkcFhACIiIiKDwwBEREREBocBiIiIiAwOAxAREREZHAYgIiIiMjgMQERERGRwGICIiIjI4DAAERERkcFhACIiIiKDwwBEREREBocBiIiIiAwOAxAREREZHAYgIiIiMjgMQERERGRwGICIiIjI4DAAERERkcFhACIiIiKDwwBEREREBocBiIiIiAwOAxAREREZHAYgIiIiMjgMQERERGRwGICIiIjI4BiJXYAuUqvVyMnJgZWVFSQSidjlEBERUSsIgoCysjK4ublBKr39NR4GoGbk5OTAw8ND7DKIiIioHbKystCtW7fbbsMA1AwrKysA9T9Aa2trkashIiKi1igtLYWHh4fme/x2GICa0XDby9ramgGIiIioi2lN8xU2giYiIiKDwwBEREREBocBiIiIiAwOAxAREREZHAYgIiIiMjgMQERERGRwGICIiIjI4IgegFasWAEvLy+YmpoiNDQUiYmJLW579uxZTJo0CV5eXpBIJFi6dGmz22VnZ+Pxxx+Hvb09zMzM0L9/fxw/fryDzoCIiIi6GlED0ObNmxEbG4uFCxciOTkZAQEBiIqK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440O/WOnvdRqNV588UVUVFRoliUlJWH58uWQSCR4/vnnW32s0NBQ3HvvvTh06BBmzZqF0tLSJtucPHkSO3fu1Py7o94f+oa3wAxQQxsFtVqN0tJSpKam4sKFCxAEAX5+ftiwYQP69+/f4XU89thjOHv2LD744AMMHjwYgYGB6NGjBwRBwJUrV3Dq1ClYWlq26Qu3I47ZnGnTpuH48eNYtmwZBg0ahLCwMHh4eOD69etISUmBp6enJoAZGRlh+/btiIqKwoIFC7B8+XIMGDAATk5OKCwsREpKCvLz8/Gf//wHQ4cOvau6OsIDDzwADw8PZGVlISgoCAMHDrzrY44bN07zswsPD4epqSl69eqF1157rVX7v/7669i5cyfmzJmDLVu2oGfPnrh06RKOHz+O2bNnY9GiRXddY3uMGzcOffv2xfHjx+Hr64uhQ4eiqqoKe/fuRWBgIMLDw3H48OG7fp6GKWsmTZqE6dOn44svvoCPjw9OnjyJS5cuYebMme0O+s8++yz+85//QBAExMTEaK7gtJeXlxcGDBiA48ePIyQkBH379oVMJsO4cePu2MsPqP/9ef311/HWW28hIiICo0aNgp2dHY4ePYq8vDzMmjULK1asuKsata2hwXaPHj0wYsQIlJSUYM+ePaitrcW8efNu29utOd988w3GjBmDzz//HBs2bEBgYCDc3NxQUlKCU6dOISsrCy+//DLGjBkDoGPfH/qEV4AM0Pr167F+/Xps3LgRBw8ehEwmw7Rp07B161acP3++zb+cd+P999/H/v37MWnSJOTm5mL79u3Yu3cvVCoVnn/+efz44486cczmfPbZZ/jf//6HyMhInDt3Dj/88AMuX76MYcOGNZkywM/PDydOnMB7772Hbt264ciRI9i6dStSU1MxcOBArFixAo8//rhW6tI2mUymmfJCW42f4+Li8MILL6Curg6bN2/G6tWr8fPPP7d6/xEjRuCPP/7AqFGjkJaWhh07dkAul+OHH37ArFmztFJje8jlchw8eBDPP/88TE1NsWPHDpw/fx4vvvgidu/e3exkwu318MMPY+/evRg5ciTOnDmDn3/+Ga6urti/f/9tp7W4k549ezZqt6YNP/zwA8aPH4+0tDR8/fXXWL16dZO5Bm/nzTffxPr16zFgwAAcOnQIv//+OwICAnDkyJFO/bxqLXt7exw5cgSRkZHYu3cv9u3bB39/f6xduxbvvvtum4/n5OSEw4cP47PPPoO/vz9OnDiB77//HqdOnYKPjw8++eQTzJ49u9E+HfX+0CcSoa1N54nIoFRUVMDd3R11dXXIycnRdBUm/ZSQkIDw8HBEREQ0mUeLbm/fvn0YOXIkYmJiOrQjBmkHrwAR0W2tWLECxcXFiImJYfgxAO+//z4A4IUXXhC5EqKOxTZARNTEjRs38MYbbyAvLw+//PILLC0tNQ2/Sf8cPnwYq1evxpkzZ5CYmIhBgwa1OHI5kb5gACKiJsrKyrB69WrI5XIMHDgQixYtanGk4q+++gp//PFHq447Z84c9O7dW5ulkhakpqZizZo1sLKywtixY7FixYoWBwqcPXt2q0ct7+q3gQzpXA0R2wAR0V2ZPn16o662t7N3717cc889HVsQdSgvL69WD6TX1b9eDOlcDREDEBERERkcNoImIiIig8MARERERAaHAYiIiIgMDgMQERERGRwGICIiIjI4DEBERERkcBiAiIiIyOAwABEREZHB+X/wgsGZAXLA/gAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "fig=plt.figure()\n",
        "sns.distplot(res, bins=15)\n",
        "fig.suptitle(\"Error Terms\", fontsize=15)\n",
        "plt.xlabel(\"Difference in y_train and y_train_pred\", fontsize=15)\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 49,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 433
        },
        "id": "7heRkkIFHQME",
        "outputId": "eed3a0ce-bf80-4051-93f2-a45a138f6be9"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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tbXp0Ucf1Z49e1RbW+v7tWX06rtO+vjjj9XW1pZxEiWpf//+2rBhg09HZY4xY8booYce0imnnKKmpibNnTtXf//3f69169apublZpaWlOu644zJ+pn///mpubvbngA2TOg8dXV+p7zU3N6tfv34Z3z/qqKPUq1evSJ7Huro6fe1rX9OQIUO0efNm3X777brsssvU2NioLl26RPp8JZNJfe9739N5552n4cOHS1Je92Fzc3OH12Dqe2HV0fmSpG984xsaPHiwBgwYoDfffFMzZ87Uxo0b9Z//+Z+Sone+3nrrLdXW1mrfvn069thjtXjxYtXU1Gjt2rW+XluRCUTQucsuuyz97zPOOENjxozR4MGD9ac//UndunXz8cgQVl//+tfT/z799NN1xhlnaNiwYXr++ed10UUX+Xhk/psxY4bWrVuXkaeF7LKdr8PziU4//XRVVVXpoosu0ubNmzVs2DCvD9N3p5xyitauXavW1lb9+c9/1rXXXqvly5f7fVjRSVbt06ePunTp0i4L+MMPP1RlZaVPR2Wu4447TieffLI2bdqkyspK7d+/X59++mnGNpy7L6TOQ2fXV2VlZbvE6IMHD2rXrl2cR0lDhw5Vnz59tGnTJknRPV833nijnnzyST333HMaOHBg+uv53IeVlZUdXoOp74VRtvPVkTFjxkhSxjUWpfNVWlqqE088UaNGjVJ9fb1GjBih3/zmN75fW5EJREpLSzVq1Cg9++yz6a8lk0k9++yzqq2t9fHIzPTZZ59p8+bNqqqq0qhRo3T00UdnnLuNGzdq69atnLv/M2TIEFVWVmaco3g8rldeeSV9jmpra/Xpp59q9erV6W0aGhqUTCbTD8go++CDD9TS0qKqqipJ0TtflmXpxhtv1OLFi9XQ0KAhQ4ZkfD+f+7C2tlZvvfVWRgC3bNkylZeXq6amxpv/iEdyna+OrF27VpIyrrGonK+OJJNJJRIJ/6+tolJdA+bRRx+1ysrKrIceeshav3699e1vf9s67rjjMrKAo+rWW2+1nn/+eWvLli3WSy+9ZI0fP97q06ePtXPnTsuyLOuGG26wBg0aZDU0NFivvfaaVVtba9XW1vp81N7avXu39frrr1uvv/66Jcm65557rNdff93629/+ZlmWZd11113WcccdZy1ZssR68803rYkTJ1pDhgyxPv/88/TvqKurs84880zrlVdesVasWGGddNJJ1uTJk/36L7mqs/O1e/du6/vf/77V2NhobdmyxXrmmWess846yzrppJOsffv2pX9HlM7X9OnTrYqKCuv555+3mpqa0h979+5Nb5PrPjx48KA1fPhw65JLLrHWrl1rLV261Orbt681e/ZsP/5Lrsp1vjZt2mT95Cc/sV577TVry5Yt1pIlS6yhQ4da559/fvp3ROl8zZo1y1q+fLm1ZcsW680337RmzZplxWIx6+mnn7Ysy99rK1KBiGVZ1r333msNGjTIKi0ttc455xxr5cqVfh+SEa6++mqrqqrKKi0ttY4//njr6quvtjZt2pT+/ueff2794z/+o9WzZ0/rmGOOsb761a9aTU1NPh6x95577jlLUruPa6+91rKsQ1N4f/SjH1n9+/e3ysrKrIsuusjauHFjxu9oaWmxJk+ebB177LFWeXm5NXXqVGv37t0+/G/c19n52rt3r3XJJZdYffv2tY4++mhr8ODB1rRp09q9FETpfHV0riRZDz74YHqbfO7D999/37rsssusbt26WX369LFuvfVW68CBAx7/b9yX63xt3brVOv/8861evXpZZWVl1oknnmjddtttVmtra8bvicr5+ta3vmUNHjzYKi0ttfr27WtddNFF6SDEsvy9tmKWZVnF9akAAAAUJjI5IgAAwDwEIgAAwDcEIgAAwDcEIgAAwDcEIgAAwDcEIgAAwDcEIgAAwDcEIgAAwDcEIgAAwDcEIgAAwDcEIgAAwDf/H/kVsN0wvviQAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "plt.scatter(x_train,res)\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 50,
      "metadata": {
        "id": "gX8NhslnHaJ6"
      },
      "outputs": [],
      "source": [
        "x_test_constant=sm.add_constant(x_test)\n",
        "y_pred=model.predict(x_test_constant)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 51,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EZBSkks_HoXU",
        "outputId": "6567df05-9cef-450a-a263-ee18f1fc9ad8"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "89     12.201147\n",
              "84     17.072666\n",
              "102    20.206034\n",
              "108     7.658468\n",
              "109    19.041004\n",
              "         ...    \n",
              "15     16.222382\n",
              "182     9.683178\n",
              "85     16.119032\n",
              "183    20.553664\n",
              "58     16.945828\n",
              "Length: 66, dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 51
        }
      ],
      "source": [
        "y_pred"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}