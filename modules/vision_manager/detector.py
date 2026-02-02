import numpy as np
import cv2

class Detector:
    """
    This class takes the current_frame and 
    detects the position of the dart to
    deliver it to the game_engine by comparing it 
    to a clean frame
    """
    def __init__(self, threshold=25):
        self.threshold = threshold
    def detect_dart(self, clean_frame, current_frame):
        """
        Compares the current frame with a clean frame to detect the dart.

        This method calculates the difference between the two frames.

        Logic:
        threshold = 25 (temporary value that needs to be tested)
        - If the difference is above 25 -> dart
        - If the difference it below 25 -> various kind of noise
        """
        pass
