# Projekt 2: Kodiranje i kriptografija
Analiza prometa putem video snimki koristeći YOLOv8 model za detekciju i praćenje objekata. 
Korišten je javno dostupan dataset preuzet sa stranice https://www.kaggle.com/datasets/aryashah2k/highway-traffic-videos-dataset?fbclid=IwAR25M6RH8IJU2zIvbaxQllpTlrDqMWqwaVt2a610DgTheplERNs4G4hWAII.
Pokretano na Linux Ubuntu 22.04.3 OS-u, AMD Ryzen 7 procesoru s AMD Radeon RENOIR grafičkom karticom.

## Instalacija i pokretanje programa
- Kloniranje repozitorija
```
git clone https://github.com/ivanatus/KIK_projekt
```
- Promjena direktorija
```
cd KIK_projekt
```
- Instalacija potrebnih knjižica
```
pip install -e '.[dev]'
pip install pingouin
```
ili u slučaju rada na Windowsima:
```
pip install -r requirements.txt
pip install pingouin
```

- Prelazak u daljnji direktorij
```
cd ultralytics/yolo/v8/detect
```
- Preuzimanje DeepSort datoteka
```
https://drive.google.com/drive/folders/1kna8eWGrSfzaR6DtNJ8_GchGgPMv3VC8?usp=sharing
```
- Izdvajanje datoteka iz zip i pozicioniranje deep_sort_pytorch foldera u yolo/v8/detect folder

- Pokretanje koda u teminalu (command prompt-u, powershell prompt-u, anaconda promt-u...)

```
python predict.py model=yolov8l.pt show=False source=video
python analysis.py
```
ili u slučaju javljene greške

```
python3 predict.py model=yolov8l.pt show=False source=video
python3 analysis.py
```



# Project 2: Coding and Cryptography
Traffic analysis through video files using YOLOv8 model for object detection and tracking. 
Dataset used is open source public dataset downloaded from: https://www.kaggle.com/datasets/aryashah2k/highway-traffic-videos-dataset?fbclid=IwAR25M6RH8IJU2zIvbaxQllpTlrDqMWqwaVt2a610DgTheplERNs4G4hWAII.
The project was done using Linux Ubuntu 22.04.3 OS with AMD Ryzen 7 processor and AMD Radeon RENOIR graphics card.

## Installing and starting the program
- Cloning the repository
```
git clone https://github.com/ivanatus/KIK_projekt
```
- Go to directory
```
cd KIK_projekt
```
- Instal needed libraries and frameworks
```
pip install -e '.[dev]'
pip install pingouin
```
if using Windows
```
pip install -r requirements.txt
pip install pingouin
```

- Change to directrory detect
```
cd ultralytics/yolo/v8/detect
```
- Download DeepSort files
```
https://drive.google.com/drive/folders/1kna8eWGrSfzaR6DtNJ8_GchGgPMv3VC8?usp=sharing
```
- Extract files from downloaded zip and position them into deep_sort_pytorch directory within yolo/v8/detect (path: .../KIK_projekt/ultralytics/yolo/v8/detect/deep_sort_pytorch)

- Starting the program from terminal (or command prompt, powershell prompt, anaconda promt...)

```
python predict.py model=yolov8l.pt show=False source=video
python analysis.py
```
if there is an error

```
python3 predict.py model=yolov8l.pt show=False source=video
python3 analysis.py
```
