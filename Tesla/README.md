# Clap 'n Trade Tesla

I dette programmet trader vi Tesla ved å klappe!

Lim dette inn:

````python
def audio_callback(indata, frames, time, status):
    global BOUGHT
    volume_norm = np.linalg.norm(indata) * 10
    print("="*int(volume_norm))
    if volume_norm >= 12 and BOUGHT == False:
        pass

    if volume_norm >= 12 and BOUGHT:
        pass


stream = sd.InputStream(callback=audio_callback)
with stream:
    print("Starting....")
    sd.sleep(duration * 1000)
````