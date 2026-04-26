filename = input('nama file soal: ')

try:
    handle = open(filename)
    for baris in handle:
        baris = baris.strip()
        if '||' in baris:
            bagian = baris.split('||')
            pertanyaan = bagian[0].strip()
            kunci = bagian[1].strip()
            print(pertanyaan)
            jawaban = input('Jawab: ')
            if jawaban.lower() == kunci.lower():
                print('Jawaban benar!')
            else:
                print('Jawaban salah!')
    handle.close()
except FileNotFoundError:
    print('File soal tidak ditemukan!')
