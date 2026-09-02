from soal1 import nilaiakhir, grades




nama = input("Masukkan nama anda: ")
nilai_tugas= float(input("Masukkan nilai tugas anda: "))
nilai_uts= float(input("Masukkan nilai uts anda: "))
nilai_uas= float(input("Masukkan nilai uas anda: "))
nilai_akhir = nilaiakhir(nilai_tugas , nilai_uts, nilai_uas)



grade = (grades(nilai_akhir))

print(f"| Nilai {nilai_akhir} -> Grade {grade}")
