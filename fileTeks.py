file1 = input('Nama file pertama: ')
file2 = input('Nama file kedua: ')

try:
    h1 = open(file1)
    h2 = open(file2)
    baris_num = 1
    ada_beda = False
    for line1, line2 in zip(h1, h2):
        if line1.strip() != line2.strip():
            ada_beda = True
            print(f'Baris {baris_num} berbeda:')
            print(f'  File 1: {line1.strip()}')
            print(f'  File 2: {line2.strip()}')
        baris_num += 1
    if not ada_beda:
        print('Kedua file identik!')
    h1.close()
    h2.close()
except FileNotFoundError:
    print('Salah satu atau kedua file tidak ditemukan!')
