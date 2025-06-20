import pandas as pd

# Excel dosyasını oku
df = pd.read_excel("data/sales_data.xlsx")

# Çıktı dosyası adı
output_file = "data/sales_data.txt"

# Metin dosyasını yaz
with open(output_file, "w", encoding="utf-8") as file:
    # Her bir satırı oku
    for index, row in df.iterrows():
        araba_modeli = row["Row Labels"]
        satir = f"{araba_modeli} "

        # Her bir şehir için satış bilgilerini ekle
        for city in df.columns[1:]:
            satir += f"{city}'da {int(row[city])} tane,"

        # Satır sonuna nokta koy ve yeni bir satıra geç
        satir = satir[:-1]  # Son virgülü kaldır
        satir += " satın alınmıştır.\n"

        # Dosyaya yaz
        file.write(satir)

print(f"Veriler {output_file} adlı dosyaya yazıldı.")
