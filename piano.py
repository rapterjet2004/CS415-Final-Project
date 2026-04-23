from playsound import playsound


def play_note(instrument, array_pos):
    ##array_Pos should only be valid, but entering a checker regardless
    if array_pos > len(instrument) - 1 or array_pos < 0:
        return
    playsound(instrument[array_pos])
    return


#create an empty list and populate it with the piano notes in their proper order
piano = []
A0 = 'A0.mp3'
piano.append(A0)
Bb0 = 'Bb0.mp3'
piano.append(Bb0)
B0 = 'B0.mp3'
piano.append(B0)
C1 = 'C1.mp3'
piano.append(C1)
Db1 = 'Db1.mp3'
piano.append(Db1)
D1 = 'D1.mp3'
piano.append(D1)
Eb1 = 'Eb1.mp3'
piano.append(Eb1)
E1 = 'E1.mp3'
piano.append(E1)
F1 = 'F1.mp3'
piano.append(F1)
Gb1 = 'Gb1.mp3'
piano.append(Gb1)
G1 = 'G1.mp3'
piano.append(G1)
Ab1 = 'Ab1.mp3'
piano.append(Ab1)
A1 = 'A1.mp3'
piano.append(A1)
Bb1 = 'Bb1.mp3'
piano.append(Bb1)
B1 = 'B1.mp3'
piano.append(B1)

C2 = 'C2.mp3'
piano.append(C2)
Db2 = 'Db2.mp3'
piano.append(Db2)
D2 = 'D2.mp3'
piano.append(D2)
Eb2 = 'Eb2.mp3'
piano.append(Eb2)
E2 = 'E2.mp3'
piano.append(E2)
F2 = 'F2.mp3'
piano.append(F2)
Gb2 = 'Gb2.mp3'
piano.append(Gb2)
G2 = 'G2.mp3'
piano.append(G2)
Ab2 = 'Ab2.mp3'
piano.append(Ab2)
A2 = 'A2.mp3'
piano.append(A2)
Bb2 = 'Bb2.mp3'
piano.append(Bb2)
B2 = 'B2.mp3'
piano.append(B2)

C3 = 'C3.mp3'
piano.append(C3)
Db3 = 'Db3.mp3'
piano.append(Db3)
D3 = 'D3.mp3'
piano.append(D3)
Eb3 = 'Eb3.mp3'
piano.append(Eb3)
E3 = 'E3.mp3'
piano.append(E3)
F3 = 'F3.mp3'
piano.append(F3)
Gb3 = 'Gb3.mp3'
piano.append(Gb3)
G3 = 'G3.mp3'
piano.append(G3)
Ab3 = 'Ab3.mp3'
piano.append(Ab3)
A3 = 'A3.mp3'
piano.append(A3)
Bb3 = 'Bb3.mp3'
piano.append(Bb3)
B3 = 'B3.mp3'
piano.append(B3)

C4 = 'C4.mp3'
piano.append(C4)
Db4 = 'Db4.mp3'
piano.append(Db4)
D4 = 'D4.mp3'
piano.append(D4)
Eb4 = 'Eb4.mp3'
piano.append(Eb4)
E4 = 'E4.mp3'
piano.append(E4)
F4 = 'F4.mp3'
piano.append(F4)
Gb4 = 'Gb4.mp3'
piano.append(Gb4)
G4 = 'G4.mp3'
piano.append(G4)
Ab4 = 'Ab4.mp3'
piano.append(Ab4)
A4 = 'A4.mp3'
piano.append(A4)
Bb4 = 'Bb4.mp3'
piano.append(Bb4)
B4 = 'B4.mp3'
piano.append(B4)

C5 = 'C5.mp3'
piano.append(C5)
Db5 = 'Db5.mp3'
piano.append(Db5)
D5 = 'D5.mp3'
piano.append(D5)
Eb5 = 'Eb5.mp3'
piano.append(Eb5)
E5 = 'E5.mp3'
piano.append(E5)
F5 = 'F5.mp3'
piano.append(F5)
Gb5 = 'Gb5.mp3'
piano.append(Gb5)
G5 = 'G5.mp3'
piano.append(G5)
Ab5 = 'Ab5.mp3'
piano.append(Ab5)
A5 = 'A5.mp3'
piano.append(A5)
Bb5 = 'Bb5.mp3'
piano.append(Bb5)
B5 = 'B5.mp3'
piano.append(B5)

C6 = 'C6.mp3'
piano.append(C6)
Db6 = 'Db6.mp3'
piano.append(Db6)
D6 = 'D6.mp3'
piano.append(D6)
Eb6 = 'Eb6.mp3'
piano.append(Eb6)
E6 = 'E6.mp3'
piano.append(E6)
F6 = 'F6.mp3'
piano.append(F6)
Gb6 = 'Gb6.mp3'
piano.append(Gb6)
G6 = 'G6.mp3'
piano.append(G6)
Ab6 = 'Ab6.mp3'
piano.append(Ab6)
A6 = 'A6.mp3'
piano.append(A6)
Bb6 = 'Bb6.mp3'
piano.append(Bb6)
B6 = 'B6.mp3'
piano.append(B6)

C7 = 'C7.mp3'
piano.append(C7)
Db7 = 'Db7.mp3'
piano.append(Db7)
D7 = 'D7.mp3'
piano.append(D7)
Eb7 = 'Eb7.mp3'
piano.append(Eb7)
E7 = 'E7.mp3'
piano.append(E7)
F7 = 'F7.mp3'
piano.append(F7)
Gb7 = 'Gb7.mp3'
piano.append(Gb7)
G7 = 'G7.mp3'
piano.append(G7)
Ab7 = 'Ab7.mp3'
piano.append(Ab7)
A7 = 'A7.mp3'
piano.append(A7)
Bb7 = 'Bb7.mp3'
piano.append(Bb7)
B7 = 'B7.mp3'
piano.append(B7)

C8 = 'C8.mp3'
piano.append(C8)
Db8 = 'Db8.mp3'
piano.append(Db8)

