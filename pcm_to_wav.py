import os

def write_txt(path,file):
    #filepath=os.path.join(path,file)
    #print("filepath: ",filepath)
    text=file.split('.')[0]
    file_txt=text+'.txt'
    filepath=os.path.join(path,file_txt)
    print("filepath: ", filepath)
    # text=str(text)
    # print(text)
    print(text)
    with open(filepath,'w',encoding='utf-8') as f:
        f.write(text)
    #pass
def handle_txt(path):
    for root,dirs,files in os.walk(path):
        print("root: ", root)
        print("dirs: ",dirs)
        print("files: ",files)
        for file in files:
            write_txt(root,file)
    print("txt生成完成..................")


def delete_pcm(path):
    files = []
    for root, dirs, files in os.walk(path):
        print("root: ", root)
        print("dirs: ", dirs)
        print("files: ", files)
        files = files
    for file in files:
        if 'pcm' in file:
            pathtmp=os.path.join(path,file)
            res=os.remove(pathtmp)
            print(res)


def check_pcm_wav(path):
    files=[]
    for root,dirs,files in os.walk(path):
        print("root: ", root)
        print("dirs: ",dirs)
        print("files: ",files)
        files=files
    print("files:  ",files)
    mp3_num=0
    wav_num=0
    for file in files:
        if "pcm" in file:
            mp3_num=mp3_num+1
        elif "wav" in file:
            wav_num=wav_num+1
        else:
            print("有其他格式的文件，忽略")

    if mp3_num==wav_num:
        print("mp3数量和wav格式数量相等 ")
    else:
        print("有转换失败的，请检查")
def pcm_to_wav(path):
    files=[]
    for root,dirs,files in os.walk(path):
        print("root: ", root)
        print("dirs: ",dirs)
        print("files: ",files)
        files=files
    print(files)
    for file in files:
        file_name=os.path.basename(file)
        #print(file_name)
        file_name_1=file_name.split('.')[0]
        #print(file_name_1)
        wav_name=file_name_1+ ".wav"
        #print(wav_name)

        filepath_pcm=os.path.join(path,file)
        print("filepath_pcm: ",filepath_pcm)
        filepath_wav=os.path.join(path,wav_name)

        #adbshell="ffmpeg -y -f u8 -ar 11025 -ss 00:00:10 -t 00:01:22 -i "+str(filepath_pcm) +" -c:a libmp3lame -q:a 8 "+str(filepath_wav)

        adbshell="ffmpeg.exe -f s16le -ar 16000 -ac 1 -i" +" "+ filepath_pcm+" " +filepath_wav

        res=os.system(adbshell)
        if res==0:
            print("转换成功")
        else:
            print("转换失败")

    check_pcm_wav(path)

if __name__=="__main__":
    path=os.getcwd()
    print(path)
    path1=os.path.join(path,'合成结果/英文')
    #path1=os.path.join(path,'pcm_to_wav')
    print(path1)
    # pcm_to_wav(path1)
    delete_pcm(path1)
    # handle_txt(path1)