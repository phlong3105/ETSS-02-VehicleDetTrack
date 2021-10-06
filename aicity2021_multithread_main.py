# ==================================================================== #
# File name: aicity2021_main.py
# Author: Automation Lab - Sungkyunkwan University
# Date created: 03/27/2021
#
# The main run script.
# ==================================================================== #
import argparse
import os
from timeit import default_timer as timer

from tss.camera import CameraMultithread
from tss.io import compress_all_result
from tss.utils import data_dir
from tss.utils import prints
from tss.utils import process_config


# MARK: - Args

parser = argparse.ArgumentParser(description="Config parser")
parser.add_argument(
    "--dataset",
    default="aicity2021_final",
    help="The dataset to run on."
)
parser.add_argument(
    "--queue_size",
    default=10,
    type=int,
    help="The max queue size"
)
parser.add_argument(
    "--visualize",
    default=False,
    help="Should visualize the processed images"
)
parser.add_argument(
    "--write_video",
    default=False,
    help="Should write processed images to video"
)

config_files = [
    "cam_1.yaml",
    "cam_1_dawn.yaml",
    "cam_1_rain.yaml",
    "cam_2.yaml",
    "cam_2_rain.yaml",
    "cam_3.yaml",
    "cam_3_rain.yaml",
    "cam_4.yaml",
    "cam_4_dawn.yaml",
    "cam_4_rain.yaml",
    "cam_5.yaml",
    "cam_5_dawn.yaml",
    "cam_5_rain.yaml",
    "cam_6.yaml",
    "cam_6_snow.yaml",
    "cam_7.yaml",
    "cam_7_dawn.yaml",
    "cam_7_rain.yaml",
    "cam_8.yaml",
    "cam_9.yaml",
    "cam_10.yaml",
    "cam_11.yaml",
    "cam_12.yaml",
    "cam_13.yaml",
    "cam_14.yaml",
    "cam_15.yaml",
    "cam_16.yaml",
    "cam_17.yaml",
    "cam_18.yaml",
    "cam_19.yaml",
    "cam_20.yaml"
]


# MARK: - Main Function

def main():
    args = parser.parse_args()
    
    # TODO: Start timer
    process_start_time     = timer()
    total_camera_init_time = 0
    
    for config_file in config_files:
        camera_start_time = timer()
        # TODO: Get camera config
        config_path   = os.path.join(data_dir, args.dataset, "configs", config_file)
        camera_hprams = process_config(config_path=config_path)
        # TODO: Define camera
        camera = CameraMultithread(config=camera_hprams, queue_size=args.queue_size, visualize=args.visualize, write_video=args.write_video)
        total_camera_init_time += timer() - camera_start_time
        # TODO: Process
        camera.run()
        
    # TODO: End timer
    total_process_time = timer() - process_start_time
    prints(f"Total processing time: {total_process_time} seconds.")
    prints(f"Total camera init time: {total_camera_init_time} seconds.")
    prints(f"Actual processing time: {total_process_time - total_camera_init_time} seconds.")
    
    # # TODO: Compress result from tss.io import compress_all_result
    # print("Compressing result")
    # output_dir = os.path.join(data_dir, args.dataset, "outputs")
    # compress_all_result(output_dir=output_dir)


# MARK: - Entry point

if __name__ == "__main__":
    main()
