from pydoc import text
import sys
import time

def ketik_lirik(text, speed=0.07): # Speed dipercepat sedikit (0.07)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        
        # Jika ada koma, jeda dikit banget, selain itu lanjut ngebut
        if char == ',':
            time.sleep(0.15)
        else:
            time.sleep(speed)
    
    print() # Pindah baris

def main():
    # Format: ("Lirik", Jeda Istirahat SINGKAT)
    # Jeda di sini saya kurangi drastis dari versi sebelumnya
    lirik = [
        ("\nSecrets I have held in my heart", 0.6), 
        ("Are harder to hide than I thought", 0.7),
        ("Maybe I just wanna be yours", 0.4), # Jeda pendek biar nyambung ke reff
        ("I wanna be yours, I wanna be yours", 0.5),
        
        # Bagian "Wanna be yours" berulang
        # Di lagu, ini ada beat-nya. Ketik -> Jeda Beat -> Ketik
        ("Wanna be yours", 0.7),
        ("Wanna be yours", 0.7),
        ("Wanna be yours", 0.7),
        ("Wanna be yours", 0.7),
        ("Wanna be yours", 0.7),
        ("Wanna be yours", 0.7),
        ("Wanna be yours", 0.7),
        # Ending
        ("(Wanna be yours...)", 3.0)
    ]

    print("\n🎧 Play Music Now... (3 seconds to start)\n")
    time.sleep(3) # Waktu buat kamu tekan play di musik

    for baris, jeda in lirik:
        ketik_lirik(baris)
        time.sleep(jeda)

if __name__ == "__main__":
    main()

# --- Bagian Penutup Sedih (Plot Twist) ---
    # Kita buat jeda panjang seolah-olah lagu sudah habis
    print("\n----------------------------------") 
    time.sleep(1.5)
    
    # Kalimat sedih diketik dengan SANGAT LAMBAT (speed=0.15)
    kalimat_sedih = "Maaf sudah lancang mencintaimu, ...\n padahal kamu tidak minta."
    ketik_lirik(kalimat_sedih, speed=0.15)
    
    
        
     