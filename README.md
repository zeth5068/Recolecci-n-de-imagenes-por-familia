![Python](https://img.shields.io/badge/Python-3.10-blue)
# 🐝 Pollinator Dataset Builder (iNaturalist)

Script en Python para la **recolección masiva de imágenes de insectos polinizadores** desde la API de iNaturalist, organizadas automáticamente por **familia y género**, e incluyendo **metadata estructurada**.

---

## 📌 Descripción

Este proyecto permite construir datasets de alta calidad para aplicaciones de:

* 🤖 Visión artificial (Computer Vision)
* 🧬 Clasificación taxonómica automática
* 🌱 Agricultura de precisión
* 🐝 Estudios de polinizadores

Las imágenes se descargan directamente desde iNaturalist usando su API pública, filtrando por calidad **"research grade"**.

---

## 🧠 Enfoque del dataset

El dataset está orientado a insectos polinizadores clave:

### 🐝 Hymenoptera (abejas y avispas)

* Apidae
* Halictidae
* Megachilidae
* Colletidae
* Andrenidae

### 🐝 Hymenoptera (parasitoides y otros)

* Ichneumonidae
* Braconidae
* Chalcididae
* Pteromalidae
* Eulophidae
* Sphecidae
* Crabronidae
* Vespidae

### 🪰 Diptera

* Syrphidae
* Bombyliidae
* Tachinidae
* Muscidae

### 🦋 Lepidoptera

* Nymphalidae
* Pieridae
* Hesperiidae
* Lycaenidae

---

## ⚙️ Características

* ✔ Descarga automática desde API REST
* ✔ Filtrado por calidad científica ("research")
* ✔ Organización jerárquica: **familia → género → imágenes**
* ✔ Generación automática de metadata (`CSV`)
* ✔ Evita duplicados
* ✔ Escalable

---

## 🗂️ Estructura del dataset

```
dataset_pollinators/
│
├── Apidae/
│   ├── Apis/
│   │   ├── img1.jpg
│   │   └── ...
│   └── ...
│
├── Syrphidae/
│   ├── Eristalis/
│   └── ...
│
└── metadata.csv
```

---

## 📄 Metadata generada

| Campo    | Descripción        |
| -------- | ------------------ |
| family   | Familia taxonómica |
| genus    | Género             |
| species  | Nombre común       |
| filename | Nombre del archivo |
| url      | URL original       |

---

## 🚀 Cómo descargar y ejecutar

### 1. Clonar repositorio

```bash
git clone https://github.com/zeth5068/Recolecci-n-de-imagenes-por-familia.git
cd Recolecci-n-de-imagenes-por-familia
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

**Activar entorno:**

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

---

### 3. Instalar dependencias

```bash
pip install requests
```

---

### 4. Ejecutar

```bash
python script.py
```

---

## 📥 Resultado

Se generará automáticamente:

```
dataset_pollinators/
```

Incluye:

* Imágenes organizadas por **familia → género**
* Archivo `metadata.csv`

---

## ⚡ Tip rápido

Para pruebas rápidas:

```python
IMAGES_PER_FAMILY = 50
```

---

## 🔧 Configuración

```python
OUTPUT_DIR = "dataset_pollinators"
IMAGES_PER_FAMILY = 3000
QUALITY = "research"
```

### Personalización

* 📈 Aumentar número de imágenes
* 🎯 Cambiar familias (`taxon_id`)
* 📁 Cambiar rutas
* ⏱️ Ajustar velocidad (`time.sleep`)

---

## ⚠️ Consideraciones

* La API de iNaturalist tiene límites
* Algunas imágenes pueden fallar
* La calidad depende de las observaciones
* `"species"` corresponde al nombre común

---

## 🧪 Casos de uso

* Clasificación con CNN
* Detección en campo
* Estudios de biodiversidad
* Modelos YOLO / ResNet

---

## 📡 Fuente de datos

https://www.inaturalist.org/

---

## ✍️ Autor

**Angello Zuñiga**

---

## 📄 Licencia

Uso libre para fines académicos y de investigación.
