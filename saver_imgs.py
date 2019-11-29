import cv2
import os

#保存摄像头数据
def convert_video_img(video_name,save_path):
    reader = cv2.VideoCapture(video_name)
    # 视频的帧率
    fps = reader.get(cv2.CAP_PROP_FPS)
    img_name_pre = video_name.split('.')[0]
    floder_name_pre=img_name_pre+'_{}'.format(fps)
    try:
        os.mkdir(save_path+floder_name_pre)
    except Exception as e:
        return e
    img_name_tem=save_path+floder_name_pre+'/'+'{}'+'_'+img_name_pre+'.jpg'
    print(img_name_tem)
    i=1
    while True:
        ret, img_np = reader.read()
        # print(img_np)
        if not ret:
            break
        cv2.imshow('a', img_np)
        cv2.waitKey(10)
        ret, jpeg = cv2.imencode('.jpg',img_np)
        frame = jpeg.tobytes()
        #
        with open(img_name_tem.format(i),'wb') as f:
        #
            f.write(frame)
        i+=1


if __name__ == '__main__':
    convert_video_img('', save_path)

