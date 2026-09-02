def nilaiakhir(nilai_tugas , nilai_uts, nilai_uas):
    nilai_akhir = 0.3 * nilai_tugas + 0.3 * nilai_uts + 0.4 * nilai_uas
    return nilai_akhir

# ?a
def grades(nilai_akhir):
    
    if nilai_akhir >= 85 or nilai_akhir <= 100: 
        return 'A'
    elif nilai_akhir >= 79 or nilai_akhir <= 84:
        return 'B'
    elif nilai_akhir >= 60 or nilai_akhir  <= 69:
        return  'C'
    elif nilai_akhir >= 50 or nilai_akhir >= 59:
        return 'D'
    else:
        return 'E'
    

nama = input("Masukkan nama anda: ")
nilai_tugas= float(input("Masukkan nilai tugas anda: "))
nilai_uts= float(input("Masukkan nilai uts anda: "))
nilai_uas= float(input("Masukkan nilai uas anda: "))
nilai_akhir = nilaiakhir(nilai_tugas , nilai_uts, nilai_uas)

print(f"| {'Nama':11} :", nama, type(nama))
print(f"| {'Nilai Akhir':12}: {nilai_akhir:.2f}", type(nilai_akhir))


