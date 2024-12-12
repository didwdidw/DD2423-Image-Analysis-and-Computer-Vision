import numpy as np
import matplotlib.pyplot as plt

from homography import *


task = "1"


if task == "1":
    num_run = 5
    noise_level = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    focal = 1000

    for _ in range(num_run):
        for i, noise in enumerate(noise_level):
            pts1, pts2, H = generate_2d_points(num = 100, noutliers = 0, noise=noise, focal = focal)
            # draw_matches(pts1, pts2)
  
            print("Run %s, Error rate: %s" % (_+1, noise))            
            # print('True H =\n', H)
            H2 = find_homography(pts1, pts2)
            # print('Estimated H =\n', H2)
            print('Error =', homography_error(H, H2, focal))
            print("---------------------------------------")