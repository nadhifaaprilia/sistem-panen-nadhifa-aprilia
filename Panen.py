nama_komoditas = "Cabai"

jumlah_panen = 100

harga_per_kg = 15000

total = jumlah_panen * harga_per_kg


def hitung_diskon(total, diskon):
    return total - (total * diskon / 100)


diskon = 10

total_setelah_diskon = hitung_diskon(total, diskon)


print("Komoditas:", nama_komoditas)

print("Jumlah panen:", jumlah_panen, "kg")

print("Total nilai panen: Rp", total)

print("Diskon:", diskon, "%")

print("Total setelah diskon: Rp", total_setelah_diskon)