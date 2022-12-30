from wsgiref.util import FileWrapper
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
import cv2
import threading


def index(request: WSGIRequest):
    return render(request=request, template_name="detect/index.html")


def looking_one(request: WSGIRequest):
    return render(request=request, template_name="detect/video.html")


def stream_video(request: WSGIRequest):
    #连接断开后无法关闭子线程
    import sys
    sys.path.append("..")
    from YOLOv5.django_detect import RunDetect
    detect = RunDetect()
    t = threading.Thread(target=detect.run)
    t.start()
    def gen_display(detect):
        """
        视频流生成器功能。
        """

        # detect.run()
        while True:
            frame = detect.getimg()
            ret, frame = cv2.imencode(".png", frame)
            if ret:
                # 转换为byte类型的，存储在迭代器中
                yield (
                    b"--frame\r\n"
                    b"Content-Type: image/png\r\n\r\n" + frame.tobytes() + b"\r\n"
                )

    return StreamingHttpResponse(
        gen_display(detect), content_type="multipart/x-mixed-replace; boundary=frame"
    )
