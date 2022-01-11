import numpy as np

from utils import xml_to_dict, load_images_from_folder


class DataSet():
    def __init__(self, Images_dir: str, XML_dir: str):
        self.images_dir = Images_dir
        self.xml_dir = XML_dir

    def load_raw_data(self):
        ann_dict = xml_to_dict(self.xml_dir)

        keypoint_names = [ann_dict['annotations']['meta']['task']['labels']['label'][i]['name'] for i in
                          range(len(ann_dict['annotations']['meta']['task']['labels']['label']))]

        images_name = [ann_dict['annotations']['image'][i]['@name'] for i in
                       range(len(ann_dict['annotations']['image']))]
        images = load_images_from_folder(self.images_dir, images_name)

        keypoints = []
        for i in range(len(ann_dict['annotations']['image'])):
            kp = []
            for p in range(len(ann_dict['annotations']['image'][i]['points'])):
                xy = ann_dict['annotations']['image'][i]['points'][p]['@points']
                xy = xy.split(',')
                x = float(xy[0])
                y = float(xy[1])
                kp.append((x, y))
            keypoints.append(kp)

        return images, keypoints, keypoint_names

    def train_test_split_dataset(self, train_size: int, test_size: int):
        images, key_points, _ = self.load_raw_data()

        X_train = np.array(images[:train_size])
        Y_train = np.array(key_points[:train_size])

        X_test = np.array(images[train_size:train_size + test_size])
        Y_test = np.array(key_points[train_size:train_size + test_size])

        return X_train, X_test, Y_train, Y_test

# ['waistband_bottom_right', 'waistband_bottom_left', 'waistband_center', 'j_top_left', 'j_bottom', 'j_center_left', 'j_center_right', 'coinpkt_top_right', 'coinpkt_top_left', 'yoke_right', 'yoke_left', 'right_frontpkt_top_right', 'right_frontpkt_bottom_right', 'right_frontpkt_top_left', 'left_frontpkt_top_left', 'left_frontpkt_bottom_left', 'left_frontpkt_top_right', 'right_leghemming_right', 'right_leghemming_left', 'left_leghemming_left', 'left_leghemming_right', 'crotch', 'j_top_right', 'waistband_top_left', 'waistband_top_right', 'right_beltloop', 'left_beltloop', 'right_bartack', 'left_bartack', 'button_right', 'button_left', 'button_center', 'waistband_top_center']
# 'C:\\Users\\Seyed\\Desktop\\preimutils\\preimutils\\keypoint_detection\\cvat\\data\\images'
# 'C:\\Users\\Seyed\\Desktop\\preimutils\\preimutils\\keypoint_detection\\data\\annotations.xml'
