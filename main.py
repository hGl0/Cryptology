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
    key = hack_affine((4,2), (19, 1))
    print(key)
    decrypted1 = decode_num(decrypt_affine(key, encoded1))
    print(decrypted1)
    '''
    # to continue later, maybe when language is known?
    # general substitution
    cipher2 = "EMGLOSUDCGDNCUSWYSFHNSFCYKDPUMLWGYICOXYSIPJCK" \
              "QPKUGKMGOLICGINCGACKSNISACYKZSCKXECJCKSHYSXCG" \
              "OIDPKZCNKSHICGIWYGKKGKGOLDSILKGOIUSIGLEDSPWZU" \
              "GFZCCNDGYYSFUSZCNXEOJNCGYEOWEUPXEZGACGNFGLKNS" \
              "ACIGOIYCKXCJUCIUZCFZCCNDGYYSFEUEKUZCSOCFZCCNC" \
              "IACZEJNCSHFZEJZEGMXCYHCJUMGKUCY"
    cipher2 = cipher2.lower()
    frequ_subs = letter_frequ(cipher2)
    print(frequ_subs)
    # known: (plain, cipher)
    # (w, f) - given; (e, c) - frequency, (g, t) - frequency
    frq_pairs_subs = frequ_pair(cipher2)
    print(sorted(frq_pairs_subs.items(), key=lambda x:x[1], reverse=True))
    frq_tri_subs = frequ_triple(cipher2)
    print(sorted(frq_tri_subs.items(), key=lambda x: x[1], reverse=True))
    doubles = double_letters(cipher2)
    print(sorted(doubles.items(), key=lambda x: x[1], reverse=True))
    perm_eng = {'w':'f', 'e':'c', 't':'g', 'a':'s'}
    perm_fr = {'w':'f', 'e':'c', 's':'g', 'a':'s', 'l': 'z'}
    print()
    print(cipher2)
    print(dec_perm(perm_eng, cipher2))
    print(dec_perm(perm_fr, cipher2))
    '''



