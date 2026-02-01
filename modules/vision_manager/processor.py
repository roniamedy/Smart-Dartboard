import cv2
import numpy as np

class FrameProcessor:
    """
    This class takes the frame from camera.py and 
    turns it into a useable information (clean frame)
    """
    def warp_frame(self, frame, corners):
        self.frame = frame
        self.corners = corners
        # set source array with a correct format for openCV
        source_points = np.array(corners, dtype = np.float32)
        self.size = 800
        self.clean_corners = self.corners
        # set array with the corners that we are aming for
        destination_points = np.array([[0,0], [self.size, 0], 
                                    [self.size, self.size], [0, self.size]], dtype = np.float32)
        
        # get the math behind the warp
        Matrix = cv2.getPerspectiveTransform(source_points, destination_points)
        # warp the frame
        result = cv2.warpPerspective(frame, Matrix, self.size)
        return result
