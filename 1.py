from progressbar import ProgressBar
import time
progress=ProgressBar().start()
for i in range(7):
    time.sleep(1)
    progress.update(int((i)/7*100))
progress.finish()