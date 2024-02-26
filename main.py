meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ") #menginput kata yang diinginkan


if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print("kata yang kamu cari: ", word)
    print("terjemahannya adalah: ", meme_dict.get(word))
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("kata tidak ditemukan")
