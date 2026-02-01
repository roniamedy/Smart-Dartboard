import cv2

class Camera:
    """
    Manages access to the webcam and 
    ensures that we always have the correct resolution.
    """
    
    def __init__(self, device_id: int):
        """initiliazes the camera with a unique ID."""
        self.device_id = device_id
        self.cap = cv2.VideoCapture(device_id)
        # set the resolution to HD.
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


        if self.cap.isOpened():
            return
        raise Exception(f"Camera with ID {device_id} could not be opened!") 


    
    def get_frame(self):
        """
        Reads a single frame from the camera.

        Returns:
            - frame
        """
        success, frame = self.cap.read()
        
        if not success:
            return None
        
        return frame
    
    
    def release(self):
        """terminates the camera connection."""
        self.cap.release() 