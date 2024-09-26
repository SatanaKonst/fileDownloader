# Скачивает файлы в указанную дирректорию
import sys
import os.path
from pathlib import Path
import subprocess
import time
import threading

imagesPath = sys.argv
savePath = imagesPath[len(imagesPath)-1]

path = Path(savePath)
path.mkdir(parents=True)

# Удаляем имя скрипта и путь для сохранения
del imagesPath[0]
del imagesPath[len(imagesPath)-1]

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def uploadImages(images):
    for imageUrl in images:
            process = subprocess.run(['wget','-q','-O',savePath+'/'+os.path.basename(imageUrl),imageUrl],
                                 stdout=subprocess.PIPE,
                                 universal_newlines=True)

# Запускаем скачивание
startTime = time.time()

imagesChunks = chunks(imagesPath,10)
threads=[]
for imageUrls in imagesChunks:
    threads.append(threading.Thread(target=uploadImages, args=(imageUrls,)) )

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print('Время выполнения скачивания: '+str(time.time()-startTime) )