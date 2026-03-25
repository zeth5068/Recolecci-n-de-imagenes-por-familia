import requests
import os
import time
import csv

# ========================
# CONFIGURACIÓN
# ========================

OUTPUT_DIR = "dataset_pollinators"
IMAGES_PER_FAMILY = 3000   # puedes aumentar luego
QUALITY = "research"

# taxon_id reales de familias clave
FAMILIES = {

    # Hymenoptera polinizadores principales
    "Apidae": 630955,
    "Halictidae": 630941,
    "Megachilidae": 630939,
    "Colletidae": 630937,
    "Andrenidae": 630944,

    # Hymenoptera parasitoides polinizadores
    "Ichneumonidae": 47199,
    "Braconidae": 47202,
    "Chalcididae": 47558,
    "Pteromalidae": 47557,
    "Eulophidae": 47561,
    "Sphecidae": 631084,
    "Crabronidae": 631083,
    "Vespidae": 631101,

    # Diptera
    "Syrphidae": 49944,
    "Bombyliidae": 49941,
    "Tachinidae": 52169,
    "Muscidae": 47895,

    # Lepidoptera
    "Nymphalidae": 48662,
    "Pieridae": 48508,
    "Hesperiidae": 47648,
    "Lycaenidae": 48666
}

# ========================
# CREAR CARPETAS
# ========================

os.makedirs(OUTPUT_DIR, exist_ok=True)

# metadata
csv_file = open(os.path.join(OUTPUT_DIR, "metadata.csv"), "w", newline='', encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["family","genus","species","filename","url"])


# ========================
# FUNCIÓN DESCARGA
# ========================

def download_family(family, taxon_id):

    print(f"\nDescargando familia: {family}")

    family_dir = os.path.join(OUTPUT_DIR, family)
    os.makedirs(family_dir, exist_ok=True)

    downloaded = 0
    page = 1

    while downloaded < IMAGES_PER_FAMILY:

        url = "https://api.inaturalist.org/v1/observations"

        params = {
            "taxon_id": taxon_id,
            "photos": "true",
            "per_page": 200,
            "page": page,
            "quality_grade": QUALITY
        }

        r = requests.get(url, params=params)

        if r.status_code != 200:
            break

        data = r.json()

        if len(data["results"]) == 0:
            break

        for obs in data["results"]:

            taxon = obs.get("taxon")
            if not taxon:
                continue

            genus = taxon.get("name","unknown")
            species = taxon.get("preferred_common_name","unknown")

            genus_dir = os.path.join(family_dir, genus)
            os.makedirs(genus_dir, exist_ok=True)

            for photo in obs.get("photos",[]):

                img_url = photo["url"].replace("square","original")

                filename = img_url.split("/")[-1]
                filepath = os.path.join(genus_dir, filename)

                if os.path.exists(filepath):
                    continue

                try:

                    img = requests.get(img_url, timeout=10)

                    with open(filepath,"wb") as f:
                        f.write(img.content)

                    csv_writer.writerow([family,genus,species,filename,img_url])

                    downloaded += 1

                    print(f"{family} | {genus} | {downloaded}")

                    if downloaded >= IMAGES_PER_FAMILY:
                        break

                except:
                    pass

            if downloaded >= IMAGES_PER_FAMILY:
                break

        page += 1
        time.sleep(1)


# ========================
# EJECUTAR DESCARGA
# ========================

for family, taxon_id in FAMILIES.items():

    download_family(family, taxon_id)

csv_file.close()

print("\nDESCARGA COMPLETA")
