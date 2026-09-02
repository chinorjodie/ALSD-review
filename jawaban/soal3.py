
def hitung_rata2(list_nilai):
    nambah = 0
    for idx,i in enumerate(list_nilai):
        nambah += i
        
        print(f"Nilai ke-{idx+1}: {i}")
    rata2 = nambah / len(list_nilai)
    print(f"Rata-rata: {rata2}")



nilai_mhs = [80, 75, 90, 65, 88]
hitung_rata2(nilai_mhs)
