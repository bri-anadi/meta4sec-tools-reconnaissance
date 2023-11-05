nama = 'Lemiel'
umur = 25
tinggi = 86.5
benar = True

print(type(nama))
print(type(umur))
print(type(tinggi))
print(type(benar))

if umur >= 18:
    print('Umur anda diatas 18')

def sapa(nama):
    return 'Halo ' + nama

print(sapa('Lemiel'))
