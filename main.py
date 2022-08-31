from Assignment1 import *

if __name__ == '__main__':
    # affine chiffre
    cipher1 = "KQEREJEBCPPCJCRKIEACUZBKRVPKRBCIBQCARBJCVFCUP" \
             "KRIOFKPACUZQEPBKRXPEIIEABDKPBCPFCDCCAFIEABDKP" \
             "BCPFEQPKAZBKRHAIBKAPCCIBURCCDKDCCJCIDFUIXPAFF" \
             "ERBICZDFKABICBBENEFCUPJCVKABPCYDCCDPKBCOCPERK" \
             "IVKSCPICBRKIJPKABI"
    # french letter frequency
    # e: 15.1; a: 8.1; t: 7.3; s: 7.0 (depending on source s before t)
    # english letter frequency
    # e: 12.7; t: 9.06; a: 8.1; o: 7.5
    frequ1 = letter_frequ(cipher1)
    print('Freq:', frequ1)
    encoded1 = encode_num(cipher1)
    keys = hack_affine((4,2), (19, 1))
    # test all possible keys
    for key in keys:
        decrypted1 = decode_num(decrypt_affine(key, encoded1))
        print(decrypted1)


    # general substitution
    cipher2 = "EMGLOSUDCGDNCUSWYSFHNSFCYKDPUMLWGYICOXYSIPJCK" \
              "QPKUGKMGOLICGINCGACKSNISACYKZSCKXECJCKSHYSXCG" \
              "OIDPKZCNKSHICGIWYGKKGKGOLDSILKGOIUSIGLEDSPWZU" \
              "GFZCCNDGYYSFUSZCNXEOJNCGYEOWEUPXEZGACGNFGLKNS" \
              "ACIGOIYCKXCJUCIUZCFZCCNDGYYSFEUEKUZCSOCFZCCNC" \
              "IACZEJNCSHFZEJZEGMXCYHCJUMGKUCY"
    frequ_subs = letter_frequ(cipher2)
    
