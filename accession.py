import gzip
import csv

#Aid2を開く
with gzip.open (r"C:\xxxxx\Download\xxxxx\Extras\Aid2GeneidAccessionUniProt.gz", "rt") as f:
  # lines = f.readlines()
  #tsvを読み込む
  reader = csv.reader(f, delimiter='\t')
  lines = []
  next(reader) #ヘッダーを飛ばす
  for line in reader:
    #[1]がgene[3]accessionnumber
    lines.append([line[1], line[3]])

  # lines = [line for line in reader]


#UniprotKBのFTPファイルを開く
with gzip.open (r"C:\Users\xxxxx\Desktop\idmapping_selected.tab.gz", "rt") as fi:
  # lines = f.readlines()
  paras=[]
  reader = csv.reader(fi, delimiter='\t')
  for line in reader:
    #[2]がgene[0]accessionnumber
    id_map = [line[2], line[0]]
  # lines = [line for line in reader]
  #id_mapを定義したら、Aid2のファイルを１行ずつ比べて、同じものがあったらプリントする。
    for row in lines:
      if id_map == row:
        print(id_map)
        paras.append(id_map)

        with open('out.csv', "w", encoding='UTF-8', newline='') as file:
          output = csv.writer(file)
          output.writerows(paras)
