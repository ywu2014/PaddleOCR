import cv2
import math
import numpy as np

def draw_sequence(Text, Bounding_boxes, canvas):
    test_seq = []
    for i, text in enumerate(Text):
        # 序号
        seq = i + 1

        test_seq.append((seq, text))

        # 圆形气泡
        Bounding_box = Bounding_boxes[i].astype("int32")
        # print(Bounding_box.shape)
        # print(Bounding_box)

        right_upper = Bounding_box[1]
        # print(type(right_upper))
        # print(right_upper)

        bubble_pt = (right_upper[0] + 20,right_upper[1] - 20)
        # print(bubble_pt)
        # print(type(bubble_pt))

        cv2.circle(canvas, bubble_pt, 10, color=(250,125,120), thickness=-1)

        if seq < 10:
            text_pt = (bubble_pt[0] - 5, bubble_pt[1] + 5)
        else:
            text_pt = (bubble_pt[0] - 10, bubble_pt[1] + 5)
        cv2.putText(canvas, str(seq), text_pt, cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), thickness=1, lineType=cv2.LINE_AA, bottomLeftOrigin=None)

    return test_seq

def drawBoxes(image, boxes, color=(255, 0, 0), thickness=5, boxes_format="boxes"):
    """Draw boxes onto an image.

    Args:
        image: The image on which to draw the boxes.
        boxes: The boxes to draw.
        color: The color for each box.
        thickness: The thickness for each box.
        boxes_format: The format used for providing the boxes. Options are
            "boxes" which indicates an array with shape(N, 4, 2) where N is the
            number of boxes and each box is a list of four points) as provided
            by `keras_ocr.detection.Detector.detect`, "lines" (a list of
            lines where each line itself is a list of (box, character) tuples) as
            provided by `keras_ocr.data_generation.get_image_generator`,
            or "predictions" where boxes is by itself a list of (word, box) tuples
            as provided by `keras_ocr.pipeline.Pipeline.recognize` or
            `keras_ocr.recognition.Recognizer.recognize_from_boxes`.
    """
    if len(boxes) == 0:
        return image
    boxes = np.array(boxes)
    canvas = image.copy()
    if boxes_format == "lines":
        revised_boxes = []
        for line in boxes:
            for box, _ in line:
                revised_boxes.append(box)
        boxes = revised_boxes
    if boxes_format == "predictions":
        revised_boxes = []
        for _, box in boxes:
            revised_boxes.append(box)
        boxes = revised_boxes
    for box in boxes:
        cv2.polylines(
            img=canvas,
            pts=box[np.newaxis].astype("int32"),
            color=color,
            thickness=thickness,
            isClosed=True,
        )
    return canvas

def draw_ocr_seq(
    image,
    boxes,
    txts=None,
    scores=None,
    drop_score=0.5,
    font_path="./doc/fonts/simfang.ttf",
):
    """
    Visualize the results of OCR detection and recognition
    args:
        image(Image|array): RGB image
        boxes(list): boxes with shape(N, 4, 2)
        txts(list): the texts
        scores(list): txxs corresponding scores
        drop_score(float): only scores greater than drop_threshold will be visualized
        font_path: the path of font which is used to draw text
    return(array):
        the visualized img
    """
    if scores is None:
        scores = [1] * len(boxes)

    box_num = len(boxes)
    seq = 1
    text_seq = []
    boxes = np.array(boxes)
    for i in range(box_num):
        if scores is not None and (scores[i] < drop_score or math.isnan(scores[i])):
            continue

        # 画气泡
        # Bounding_box = boxes[i].astype("int32")
        Bounding_box = boxes[i].astype("int32")
        print(Bounding_box.shape)
        print(Bounding_box)

        right_upper = Bounding_box[1]
        # print(type(right_upper))
        # print(right_upper)

        bubble_pt = (right_upper[0] + 20,right_upper[1] - 20)
        # print(bubble_pt)
        # print(type(bubble_pt))

        cv2.circle(image, bubble_pt, 10, color=(250,125,120), thickness=-1)

        if seq < 10:
            text_pt = (bubble_pt[0] - 5, bubble_pt[1] + 5)
        else:
            text_pt = (bubble_pt[0] - 10, bubble_pt[1] + 5)
        cv2.putText(image, str(seq), text_pt, cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), thickness=1, lineType=cv2.LINE_AA, bottomLeftOrigin=None)

        # 输出内容
        if txts is not None:
            text_seq.append((seq, txts[i]))

        seq = seq + 1

    return text_seq